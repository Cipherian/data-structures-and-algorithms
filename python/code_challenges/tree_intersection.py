from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue

def tree_intersection(tree1, tree2):
    if not tree1.root or not tree2.root:
        return set()

    q1 = Queue()
    q1.enqueue(tree1.root)
    hash_table = {}
    while not q1.is_empty():
        dequeued = q1.dequeue()
        if dequeued:
            if dequeued.value not in hash_table:
                hash_table[dequeued.value] = True
            q1.enqueue(dequeued.left)
            q1.enqueue(dequeued.right)

    q2 = Queue()
    q2.enqueue(tree2.root)
    duplicates = set()
    while not q2.is_empty():
        dequeued = q2.dequeue()
        if dequeued:
            if dequeued.value in hash_table:
                duplicates.add(dequeued.value)
            q2.enqueue(dequeued.left)
            q2.enqueue(dequeued.right)
    return duplicates
