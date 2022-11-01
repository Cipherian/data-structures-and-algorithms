from data_structures.invalid_operation_error import InvalidOperationError

class Stack:
    """
    Put docstring here
    """


    def __init__(self, top=None):
        self.top = top

    def __str__(self):
        if self.top is None:
            return str(self)

    def __repr__(self):
        if self.top is None:
            return repr(self)

    def is_empty(self):

        if self.top is None:
            return True
        return False

    def push(self, value):
        """Assigns a value to a Node, if there is no top value then assigns the new_node value to self.top. Then assigns new_node next to the self.top, then the self.top is assigned to the new node"""""
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top is None:
            raise InvalidOperationError('Method not allowed on empty collection')

        temp = self.top

        if self.top.next:
            self.top = self.top.next
            temp.next = None
        else:
            self.top = None
        return temp.value

    def peek(self):

        if not self.top:
            raise InvalidOperationError("Stack is empty! Can't peek.")

        return self.top.value


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next



