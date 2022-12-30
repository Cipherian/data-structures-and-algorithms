# Insertion-sort

```Pseudo Code:
  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp

## Walkthrough/Blog

- The first line declares a function insertionsort which takes in
an array of integers as a parameter.

- Then it starts a for loop and iterates through the array that is passed in through the parameter.

- The next line declares an integer variable j, and sets the value to i-1, it will be used to keep track of the position in the array where the index i should be inserted.

- The next line, the variable temp is initialized to the value of the element at index i in the array passed in through the parameter. Temp will hold the index

- After that we iterate while j >= 0 and the temp variable is less than the index of the array

- During that while loop we point the array at the index of j + 1 to the array at i

- then the index is pointed to j - 1

- then we point array at j + 1 to the temp variable

