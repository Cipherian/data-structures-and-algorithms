# Binary Tree and Binary Search Tree

- Worked on by Daniel Brott

- 11/19/2022

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
