class SimpleStack:
    def __init__(self):
        self._a = []

    def push(self, a):
        self._a.append(a)

    def pop(self):
        return self._a.pop() if len(self._a) > 0 else None

    def __str__(self):
        return str(self._a)

