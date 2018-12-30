from unittest import TestCase

from SSTable import SSTable
from SSTablesIterator import SSTablesIterator
import random

class TestSSTablesIterator(TestCase):
    def test_iter(self):
        sstables = []

        all_random_data = []
        for i in xrange(5):
            random_data = [random.randint(1, 1000) for i in xrange(5)]
            all_random_data.extend(random_data)

            sstable = SSTable()
            for data in sorted(random_data):
                sstable.append(data)
            sstables.append(sstable)

        sstable_i = SSTablesIterator(sstables)

        new_data = []
        prev_k = None
        for k in sstable_i:
            if prev_k:
                self.assertLessEqual(prev_k, k)
            prev_k = k
            new_data.append(k)

        self.assertEqual(sorted(all_random_data), new_data)


