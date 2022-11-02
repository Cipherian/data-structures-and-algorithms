# Stack and Queue

- Worked on by Daniel Brott

## Assignment

- Implement a Stack and Queue Class

- Code: [Stack](../stack.py)
- Code: [Queue](../queue.py)

## Approach and efficiency

- O(1)

## Methods of Stack

- Is_empty: Verifies that the top of the stack is empty

- Push: Assigns a value to a Node, if there is no top value then assigns the new_node value to self.top. Then assigns new_node next to the self.top, then the self.top is assigned to the new node

- Pop: If "self.top" is none, returns an error. Then checks for ```self.top.next```, then reassigns "self.top" to "self.top.next" then assigns the temp value to be None. Otherwise assigns self.top to be none. Then returns the temp.value.

- Peek: Checks to see if the top of the stack has a value, if it doesn't returns an error.

## Methods of Queue

- is_empty: Checks to see if the front is None, then returns True if it is.

- Enqueue: Assigns a value to Node(value) if the front is none, then assigns the front to the node value. If self.back is not a NONE or a NULL value then assigns self.back.next to the new_node. Otherwise self.back is assigned to the new node.

- Peek: If the front is None or has no value, throws an error, otherwise returns the front value

- Dequeue if the front is none or has no value, raises an error, otherwise assigns a temporary value to self.front. If self.front.next is not none or has a vlaue, reassign self.front to self.front.next and assign temp.next to NONE or NULL. Otherwise self.front is None and return the temporary value.

