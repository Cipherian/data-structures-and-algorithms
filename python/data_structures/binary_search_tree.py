from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    ## Class Binary Search Tree

- add method:

  - creates a node value

  - if the root is none, then the new root becomes the node value

  - recursive walk method that checks if the node value is less than the root value, if the root left is not none, then uses recursion to return back to the start of the loop if the root left is none, assigns the left to the node value.

  - if the node value is greater than the root value goes to the right of the tree and then if the root.right is not none, then it continues traversing, otherwise if the root.right is none then it assigns that value to the node value.

- contains method:

  - create an empty array

  - has a walk method which checks if the root is none.

  - if the root is not none, it then traverses the tree and looks for that value and then appends it to the array.

  - If the item is contained in the list, then it returns true, otherwise if the list is empty, it evaluates to false.
    """

    def __init__(self, root=None):
        self.root = root

    def add(self, value):
        node = Node(value)

        if self.root is None:
            self.root = node
            return

        def walk(root, node):
            if node.value < root.value:
                if root.left:
                    walk(root.left, node)
                else:
                    root.left = node

            else:
                if root.right:
                    walk(root.right, node)
                else:
                    root.right = node

        walk(self.root, node)

    def contains(self, value = None):

        def walk(root, node):
            if root is None:
                return

            if root:
                if root.value == value:
                  value = root.value
                else:
                    if value < root.value:
                        if root.left:
                            walk(root.left, node)
                    else:
                        if root.right:
                            walk(root.right, node)

        walk(self.root, None)

        if value is not None:
            return True
        else:
            return False


