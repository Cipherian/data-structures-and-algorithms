from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
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

    def contains(self, value):
        contains_list = []

        def walk(root, node):
            if root is None:
                return

            if root:
                if root.value == value:
                    contains_list.append(node)
                else:
                    if value < root.value:
                        if root.left:
                            walk(root.left, node)
                    else:
                        if root.right:
                            walk(root.right, node)

        walk(self.root, None)

        return len(contains_list) == 1


