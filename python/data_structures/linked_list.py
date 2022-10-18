class Node:
    """
    Put docstring here
    """

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    # def __str__(self):
    #     return str(self.value)


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        # print(LinkedList)
        # LinkedList.__str__()
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

    def includes(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

class DoublyLinkedList:
    def __init__(self,):
        self.head = None

    def __str__(self):
        current = self.head
        txt = ""
        while current is not None:
            txt += current.value
            current = current.next
        return txt

## puts to the beginning of the linked list
    def push(self, new_val):
        new_node = Node(new_val)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node


    # def insert_node(self,prev_node, new_val):
    #     if prev_node is None:
    #         return
    #     new_node = Node(new_val)
    #     new_node.next = prev_node.next
    #     prev_node.next = new_node
    #     new_node.prev = prev_node
    #     if new_node.next is not None:
    #         new_node.next.prev = new_node


## puts to the end of the linked list
    def append(self, value):
        new_node = Node(value)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last
        return

    @staticmethod
    def list_print(node):
            while node is not None:
                print(node.value)
                node = node.next

    def includes(self, value)  :
        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False





class TargetError:
    pass
