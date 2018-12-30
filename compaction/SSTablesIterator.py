from SSTable import SSTable

class SSTablesIterator:
    def __init__(self, sstables=[]):
        self._sstables = sstables

    def __iter__(self):
        self._values_and_iters = []
        for sstable in self._sstables:
            sstable_iter = iter(sstable)
            try:
                value = next(sstable_iter)
                self._values_and_iters.append((value, sstable_iter))
            except StopIteration:
                pass
        return self

    def next(self):
        if len(self._values_and_iters) == 0:
            raise StopIteration

        self._values_and_iters = sorted(self._values_and_iters, key=lambda x: x[0])
        return_value = self._values_and_iters[0][0]
        sstable_iter = self._values_and_iters[0][1]
        self._values_and_iters = self._values_and_iters[1:]
        try:
            next_value = next(sstable_iter)
            self._values_and_iters.append((next_value, sstable_iter))
        except StopIteration:
            pass
        return return_value
