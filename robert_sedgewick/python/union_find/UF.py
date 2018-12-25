class UF:
    def __init__(self):
        pass

    def connected(self, p, q):
        raise NotImplementedError("Subclasses should implement this!")

    def union(self, p, q):
        raise NotImplementedError("Subclasses should implement this!")