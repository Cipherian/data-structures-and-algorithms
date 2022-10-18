class Node:
    """initialization of node class"""

    def __init__(self, value):
        self.value = value
        self.next = None
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

        while current:
            if current.next is None:
                current.next = node
            else:
                current = current.next

    # def insert_before(self, value, new_value):
    #     # inserts new_value before the specified value
    #     current = self.head
    #     node = Node(new_value)
    #
    #     if current is None:
    #         self.head = node
    #     while current:
    #         if current.next == value:
    #             current = node
    #         else:
    #             current = current.next

    def insert_before(self, value, new_value):
        # create new node
        new_node = Node(new_value)
        # find target node to insert
        current = self.head
        if current is None:
            self.head = new_node
        else:
            # search nodes
            if current.value == value:
                new_node.next = self.head
                self.head = new_node

            while current.next is not None:
                if current.next.value == value:
                    new_node.next = current.next
                    current.next = new_node
                    return
                else:
                    current = current.next

    # def insert_after(self, new_value, position):
    #
    #     # 1. allocate node to new element
    #     new_node = Node(new_value)
    #
    #     # 2. check if the position is > 0
    #     if position < 1:
    #         print("\nposition should be >= 1.")
    #     elif position == 1:
    #
    #         # 3. if the position is 1, make next of the
    #         #   new node as head and new node as head
    #         new_node.next = self.head
    #         self.head = new_node
    #     else:
    #
    #         # 4. Else, make a temp node and traverse to the
    #         #   node previous to the position
    #         temp = self.head
    #         for i in range(1, position - 1):
    #             if temp is None:
    #                 temp = temp.next
    #
    #                 # 5. If the previous node is not null, make
    #         #   new_node next as temp next and temp next
    #         #   as new_node.
    #         if temp is None:
    #             new_node.next = temp.next
    #             temp.next = new_node
    #         else:
    #
    #             # 6. When the previous node is null
    #             print("\nThe previous node is null.")

                # def insert_after(self, value, new_value):
    #     # inserts new_value after the specified value
    #     current = self.head
    #     node = Node(new_value)
    #
    #     if current is None:
    #         self.head = node
    #     while current:
    #         if current == value:
    #             node.next = current.next
    #             current.next = node
    #             return
    #         else:
    #             current = current.next

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
