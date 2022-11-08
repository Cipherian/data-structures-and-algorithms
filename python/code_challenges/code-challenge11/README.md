# Pseudo Queue

## 11/07/2022

## Worked on by Daniel Brott

## Functionality

- Replicates Queue functionality with stack database structure using two methods

### Enqueue

- Create a value that holds a temporary stack

- Move all nodes from the original stack into the temp stack

- Add a new node with the given value into the original stack

- Remove all items from the temporary stack and add them to the original stack

### Dequeue

- Checks to see if the top of the stack is empty

- If it is not empty, removes the top of the stack

Visuals: [PseudoQueue](./images/PseudoQueue.jpg)
Code: [PseudoQueueCode](../stack_queue_pseudo.py)
