# Binary Tree and Binary Search Tree

- Worked on by Daniel Brott

- 11/19/2022

- find maximum 11/21/2022

## Class Binary Tree

- pre_order method:

  - Declare a variable to an empty list

  - Uses a walk method which takes in a root parameter

  - If it is not the root node then it returns, otherwise it appends the value of the root node.

  - Utilizes recursion to check the left most node and then append those values to the empty array. Then uses recursion on the right nodes to append those values. Then appends the initial root value.

- in_order method:

  - follows the first two steps as above

  - Uses recursion to walk left, then appends the left most value on the tree, then goes to the right of the tree and appends those values, then returns to the root of the tree to append that value.

- post_order method:

  - Does the same as bove

  - Uses recursion to walk left, then to the right in the tree then append the root value.

- Then returns to the root of the tree and appends that value.

- find_maximum value: Traverses the tree and returns the highest numeric value of that tree

[find_maximum](./images/find_maximum.jpg)

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
