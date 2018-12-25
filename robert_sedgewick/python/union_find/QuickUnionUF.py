import UF

class QuickUnionUF(UF.UF):
    def __init__(self, size):
        UF.UF.__init__(self)
        self._a = [i for i in xrange(size)]

    def root(self, i):
        while i != self._a[i]:
            i = self._a[i]

        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        idx_p = self._a[p]
        idx_q = self._a[q]
        self._a[idx_p] = idx_q

