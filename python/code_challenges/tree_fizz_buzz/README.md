# Fizz_Buzz_Tree

- Author: Daniel Brott

- Whiteboard: [Whiteboard](./images/fizz_buzz_tree.jpg)

- Code: [Fizz_Buzz_tree](../tree_fizz_buzz.py)

## functionality

- The fizz_buzz_function takes in a number as input and returns a string based on the following conditions:

- If the number is divisible by 15, return "FizzBuzz"

- If the number is divisible by 3, return "Fizz"

- If the number is divisible by 5, return "Buzz"

- If the number is not divisible by 3, 5, or 15, return the number as a string

- The fizz_buzz_tree function takes in a tree as input and returns a new tree where the values of the nodes are replaced with the output of the fizz_buzz_function

- k_tree is instantiated as a kary tree

- A queue is created and the root node of the input tree and the root node of k_tree are added to the queue

- A loop is entered that continues until the queue is empty

- The first node in the queue is removed and its value is replaced with the output of fizz_buzz_function

- For each child of the node, a new child node is added to the corresponding node in k_tree and the child node and its corresponding node in k_tree are added to the queue

-The modified k_tree is returned
