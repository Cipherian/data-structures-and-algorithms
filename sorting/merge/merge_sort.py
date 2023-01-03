"""
1: Declare a function which takes in a list of integers.
2: if the length of the list is greater than 1, then sorts the list, otherwise it will just return the list.
3: In the if statement, mid is assigned to the length of the list and floor division is used to find the midpoint.
4: left is assigned to the left side of the array slicing with the midpoint variable.
5: right is assigned to the right side of the array slicing with the midpoint variable.
6: Then recursion is used on the left and right until the entire array is sorted.
"""


def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, arr)

    return arr


def merge(left, right, arr):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    if i == len(left):
        arr[k:] = right[j:]
    else:
        arr[k:] = left[i:]
