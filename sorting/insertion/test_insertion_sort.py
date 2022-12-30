from insertion_sort import insertion_sort_function
import inspect


def test_insertion_sort_function():
    assert insertion_sort_function([6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6]
    assert insertion_sort_function([]) == []
    assert insertion_sort_function([5]) == [5]


def test_length_of_insertion_sort_function():
    assert len(insertion_sort_function([])) == 0
    assert len(insertion_sort_function([1, 2, 3])) == 3
    assert len(insertion_sort_function([1, 2, 3, 4])) == 4


def test_insertion_sort_function_arguments():
    assert inspect.getfullargspec(insertion_sort_function).annotations == {'arr': list[int], 'return': list[int]}


def test_insertion_sort_function_is_a_function():
    assert inspect.isroutine(insertion_sort_function)



