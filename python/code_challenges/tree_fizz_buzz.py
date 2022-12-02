from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue
from data_structures.kary_tree import KaryTree, Node

def fizz_buzz_function(num):
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

def fizz_buzz_tree(tree):
    k_tree = KaryTree()
    k_tree.root = Node()
    queue = Queue()

    queue.enqueue((tree.root, k_tree.root))
    while not queue.is_empty():
        old_node, new_node = queue.dequeue()
        new_node.value = fizz_buzz_function(old_node.value)

        for child in old_node.children:
            new_child = Node()
            new_node.children.append(new_child)
            queue.enqueue((child, new_child))

    return k_tree




