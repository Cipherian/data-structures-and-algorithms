class Node:
    """initialization of node class"""

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    # def __str__(self):
    #     return str(self.value)


class LinkedList:
    """initialization of linkedlist class"""
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        string = ""
        current = self.head
        while current is not None:
            string += f'{{ {current.value} }} -> '
            current = current.next
        string += 'NONE'
        return string

    def delete(self):
        if self.head is None:
            raise TargetError('Empty list')

        current = self.head
        while current.next is not None:
            current = current.next
        current.value = current.next.value
        current.next = current.next.next

    def reverse(self):
        current = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insert(self, value):
        node_item = Node(value)

        if self.head is not None:
            node_item.next = self.head
        self.head = node_item

    def add_one_to_ll(self):
        self.reverse()
        current = self.head
        carry = 1
        while current is not None and carry > 0:
            current.value += carry
            if current.value >= 10:
                current.value -= 10
                carry = 1
            else:
                carry = 0
            current = current.next
        if carry > 0:
            node = Node(1)
            if self.head is None:
                self.head = node
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = node
        self.reverse()

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



class TargetError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


