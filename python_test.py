"""
Test cases for mergeSort function from hw2_debugging.

This module includes tests to verify if the mergeSort function works correctly
for different types of input arrays:
- A sorted array
- A reverse sorted array
- An array with duplicate values
"""

from hw2_debugging import merge_sort

def test_sorted_array():
    """
    Test mergeSort with an already sorted array.
    """
    arr = [1, 2, 3, 4, 5]
    sorted_arr = merge_sort(arr)
    assert sorted_arr == [1, 2, 3, 4, 5], (
        f"Test failed! Expected [1, 2, 3, 4, 5], got {sorted_arr}"
    )

def test_reverse_sorted_array():
    """
    Test mergeSort with a reverse sorted array.
    """
    arr = [5, 4, 3, 2, 1]
    sorted_arr = merge_sort(arr)
    assert sorted_arr == [1, 2, 3, 4, 5], (
        f"Test failed! Expected [1, 2, 3, 4, 5], got {sorted_arr}"
    )

def test_array_with_duplicates():
    """
    Test mergeSort with an array containing duplicate values.
    """
    arr = [8, 7, 3, 6, 4, 2, 1]
    sorted_arr = merge_sort(arr)
    assert sorted_arr == [1, 2, 3, 4, 6, 7, 8], (
        f"Test failed! Expected [1, 2, 3, 4, 6, 7, 8], got {sorted_arr}"
    )
