from unittest import TestCase

from Compaction import Compaction
from SSTable import SSTable

import os
import random
import tempfile


class TestCompaction(TestCase):
    def test_compaction(self):
        sstable_files = []

        all_random_data = []
        for i in xrange(5):
            random_data = [random.randint(1, 1000) for i in xrange(5)]
            all_random_data.extend(random_data)

            sstable = SSTable()
            for data in sorted(random_data):
                sstable.append(data)

            tmp_file = tempfile.mkstemp()[1]
            sstable.flush(tmp_file)

            sstable_files.append(tmp_file)

        for f in sstable_files:
            self.assertTrue(os.path.exists(f))

        new_sstable_file = tempfile.mkstemp()[1]
        os.remove(new_sstable_file)

        c = Compaction(sstable_files)
        c.do_compaction(new_sstable_file)
        self.assertTrue(os.path.exists(new_sstable_file))

        for f in sstable_files:
            self.assertFalse(os.path.exists(f))

        new_sstable = SSTable()
        new_sstable.load_file(new_sstable_file)
        new_data = [k for k in new_sstable]

        self.assertEqual(sorted(all_random_data), new_data)

        os.remove(new_sstable_file)
