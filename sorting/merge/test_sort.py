from merge_sort import merge_sort


def test_merge_sort_list():
    arr = [3, 7, 4, 9, 5, 2, 6, 1]
    expected_output = [1, 2, 3, 4, 5, 6, 7, 9]
    merge_sort(arr)
    assert arr == expected_output


def test_merge_sort_negative_numbers():
    arr = [-5, 0, 6, -3, 2, -1]
    expected_output = [-5, -3, -1, 0, 2, 6]
    merge_sort(arr)
    assert arr == expected_output

def test_merge_sort_empty_list():
    arr = []
    expected_output = []
    merge_sort(arr)
    assert arr == expected_output


def test_merge_sort_one_element_list():
    arr = [1]
    expected_output = [1]
    merge_sort(arr)
    assert arr == expected_output





