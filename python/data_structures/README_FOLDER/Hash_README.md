# Hash Tables

- Author: Daniel Brott

- Code: [Hash_Tables](../hashtable.py)

## Challenge: Implement a hash table with Python

## Approach & Efficiency

- hash_function: returns the sum of the unicode value of each character primed 31

- set: O(1) Sets a value at at an index with the provided key

- get: O(1) Searches for the index with the provided key, if it is there returns the value

- delete: O(1) Searches for the specific index and turns the value to None

- has: O(1) Searches for the specific index and if it is not a None value it then returns true, otherwise returns false.

- keys: O(n): Iterates through the buckets list and appends any None values to the keys list.
