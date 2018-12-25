import Node

class Queue:
    def __init__(self):
        self._head = None
        self._tail = None

    def enqueue(self, value):
        new_node = Node.Node(value)

        if not self._head:
            assert self._tail is None
            self._head = new_node
            self._head.next = None
            self._tail = self._head
            return

        assert self._tail is not None

        self._tail.next = new_node
        self._tail = new_node

    def dequeue(self):
        if not self._head:
            assert self._tail is None
            return None

        value = self._head.value

        self._head = self._head.next
        if self._head is None:
            assert self._tail.next is None
            self._tail = self._head

        return value

    def __str__(self):
        ret_str = ""

        tmp = self._head
        while tmp:
            ret_str += tmp.value
            tmp = tmp.next

        return "Queue : " + ret_str