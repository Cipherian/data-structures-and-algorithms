# Tree Intersection

- Author Daniel Brott

- Code: [tree_code](../tree_intersection.py)

- Whiteboard: [tree_whiteboard](./images/hash_intersect.jpg)

## Functionality

- First checks to make sure that the tree is not empty, if it is, it returns an empty set

- Then declares a variable to Queue data structure

- Then enqueues the root

- Then uses a python dictionary/hashmap

- Traverses through the first tree

- Dequeues all the values in the tree into the hashmap

- A second variable is declared to a second queue

- A variable duplicates is declared to an empty set

- Traverse through the second tree and dequeue it's value

- Check if the dequeued values are in the hashmap, add them to the duplicates value

- Return the final duplicates value
