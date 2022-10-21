class Node:
    """initialization of node class"""

    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        self.prev = None

    # def __str__(self):
    #     return str(self.value)


class LinkedList:
    """initialization of linkedlist class"""
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
        string += 'NONE'
        return string

    def insert(self, value):
        node_item = Node(value)

        if self.head is not None:
            node_item.next = self.head
        self.head = node_item

    def includes(self, value):
        ## checks if current value equals target value
        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def append(self, value):
        #appends the value to the end of the linked list
        node = Node(value)
        current = self.head

        if current is None:
            self.head = node
        else:
            while current.next is not None:
                current = current.next
            current.next = node

    def insert_before(self, value, new_value):
        #insert before specified value
        new_node = Node(new_value)
        current = self.head
        if self.head is None:
            raise TargetError('Empty list')

        if not self.includes(value):
            raise TargetError('Value not found')

            # search nodes
        if current.value == value:
            new_node.next = self.head
            self.head = new_node

        else:
            while current.next:
                if current.next.value == value:
                    new_node.next = current.next
                    current.next = new_node
                    return
                else:
                    current = current.next

    def insert_after(self, value, new_value):
        ## inserts new value after specified value
        current = self.head
        if current is None:
            raise TargetError('Empty list')

        if not self.includes(value):
            raise TargetError('Value not found')

        while current:
            if current.value is value:
                node = Node(new_value, current.next )
                current.next = node
                break
            else:
                current = current.next

    def kth_from_end(self, k):
        length = 0
        current = self.head

        while current:
            length += 1
            current = current.next

        if k > length or k < 0 or k == length:
            raise TargetError('Invalid k input')

        temp = self.head

        for i in range(1, length - k):
            temp = temp.next

        return temp.value


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


class TargetError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
