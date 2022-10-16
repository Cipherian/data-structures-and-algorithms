class Node:
    """
    Put docstring here
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    # def __str__(self):
    #     return str(self.value)


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        string = ""
        current = self.head
        while current is not None:
            string += f'{{ {current.value} }} -> '
            current = current.next
        string += 'NULL'
        return string

    def insert(self, value):
        node_item = Node(value)

        if self.head is not None:
            node_item.next = self.head
        self.head = node_item

    def includes(self, value)  :
        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

class TargetError:
    pass
