import pytest
from hw2_debugging import mergeSort

def test_sorted_array():
    arr = [1, 2, 3, 4, 5]
    sorted_arr = mergeSort(arr)
    assert sorted_arr == [1, 2, 3, 4, 5], f"Test failed! Expected [1, 2, 3, 4, 5], got {sorted_arr}"

def test_reverse_sorted_array():
    arr = [5, 4, 3, 2, 1]
    sorted_arr = mergeSort(arr)
    assert sorted_arr == [1, 2, 3, 4, 5], f"Test failed! Expected [1, 2, 3, 4, 5], got {sorted_arr}"

def test_array_with_duplicates():
    arr = [4, 1, 2, 2, 5, 3, 1]
    sorted_arr = mergeSort(arr)
    assert sorted_arr == [1, 1, 2, 2, 3, 4, 5], f"Test failed! Expected [1, 1, 2, 2, 3, 4, 5], got {sorted_arr}"