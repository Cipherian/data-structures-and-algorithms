from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    values = []
    queue = Queue()
    queue.enqueue(tree.root)

    while not queue.is_empty():
        deq = queue.dequeue()

        if deq:
            values.append(deq.value)
            queue.enqueue(deq.left)
            queue.enqueue(deq.right)

    return values
