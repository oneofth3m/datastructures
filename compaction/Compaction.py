from SSTable import SSTable
from SSTablesIterator import SSTablesIterator

import os

class Compaction:
    def __init__(self, file_names=[]):
        self._sstable_files = file_names
        self._sstables = []
        for f in self._sstable_files:
            sstable = SSTable()
            sstable.load_file(f)
            self._sstables.append(sstable)

    def do_compaction(self, new_file_name=None):
        sstables_iter = SSTablesIterator(self._sstables)
        new_sstable = SSTable()
        for k in sstables_iter:
            new_sstable.append(k)
        new_sstable.flush(new_file_name)

        for f in self._sstable_files:
            os.remove(f)
