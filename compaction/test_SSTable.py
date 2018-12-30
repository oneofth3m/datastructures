from unittest import TestCase

from SSTable import SSTable

import os
import random
import tempfile

class TestSSTable(TestCase):
    def test_iter(self):
        tmp_file = tempfile.mkstemp()[1]

        test_data = [random.randint(1, 1000) for i in xrange(10)]

        s1 = SSTable()
        for key in sorted(test_data):
            s1.append(key)
        s1.flush(tmp_file)

        s2 = SSTable()
        s2.load_file(tmp_file)
        read_data = [k for k in s2]

        self.assertEqual(sorted(test_data), read_data)

        os.remove(tmp_file)

    def test_append(self):
        s = SSTable()
        s.append(10)
        s.append(11)
        try:
            s.append(9)
        except AssertionError:
            pass
        else:
            raise AssertionError("Assertion Error Expected")

    def test_flush(self):
        tmp_file = tempfile.mkstemp()[1]

        test_data = [random.randint(1, 1000) for i in xrange(10)]

        s = SSTable()
        for key in sorted(test_data):
            s.append(key)
        s.flush(tmp_file)

        os.remove(tmp_file)

    def test_load_file(self):
        tmp_file = tempfile.mkstemp()[1]

        test_data = [random.randint(1, 1000) for i in xrange(10)]

        s1 = SSTable()
        for key in sorted(test_data):
            s1.append(key)
        s1.flush(tmp_file)

        s2 = SSTable()
        s2.load_file(tmp_file)

        os.remove(tmp_file)
