from data_structures.invalid_operation_error import InvalidOperationError

class Queue:
    """
    Put docstring here
    """

    def __init__(self, front=None, back=None):
        self.front = front
        self.back = back

    def is_empty(self):
        if self.front is None:
            return True

    def enqueue(self, value):
        new_node = Node(value)

        if self.front is None:
            self.front = new_node
        if self.back:
            self.back.next = new_node
        self.back = new_node

    def peek(self):
        if self.front is None:
            raise InvalidOperationError
        return self.front.value

    def dequeue(self):
        if self.front is None:
            raise InvalidOperationError
        temp = self.front

        if self.front.next:
            self.front = self.front.next
            temp.next = None
        else:
            self.front = None
        return temp.value


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self)

    def __repr__(self):
        return repr(self)
