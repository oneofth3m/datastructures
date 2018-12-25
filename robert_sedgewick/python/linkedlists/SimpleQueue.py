class SimpleQueue:
    def __init__(self):
        self._a = []

    def enqueue(self, a):
        self._a.append(a)

    def dequeue(self):
        if len(self._a) == 0:
            return None

        value = self._a[0]
        # del self._a[0]
        self._a = self._a[1:]
        return value

    def __str__(self):
        return str(self._a)