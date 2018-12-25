class Node:
    def __init__(self, value=None, next_node=None):
        self._value = value
        self._next_node = next_node

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def next(self):
        return self._next_node

    @next.setter
    def next(self, next_node):
        assert isinstance(next_node, Node)
        self._next_node = next_node

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return 'Value : %s, Next Node: %s' % (str(self._value) % repr(self._node))