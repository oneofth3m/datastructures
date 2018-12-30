import Node

class Stack:
    def __init__(self):
        self._head = None

    def push(self, value):
        new_node = Node.Node(value, None)

        if not self._head:
            self._head = new_node
            return

        new_node.next = self._head
        self._head = new_node

    def pop(self):
        if not self._head:
            return None

        value = self._head.value
        self._head = self._head.next
        return value

    def __str__(self):
        tmp = self._head
        ret_str = ""
        while tmp:
            ret_str += ("%s -> " % tmp)
            tmp = tmp.next

        ret_str = "Stack : " + ret_str
        return ret_str
