class UF:
    def __init__(self, size):
        self._a = [i for i in xrange(size)]

    def find(self, p, q):
        return self._a[p] == self._a[q]

    def union(self, p, q):
        idx_p = self._a[p]
        idx_q = self._a[q]

        self._a = map(lambda x: idx_p if x == idx_q else x, self._a)







