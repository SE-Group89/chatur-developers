"""
This module implements the merge sort algorithm and a function to recombine
subarrays during the sorting process.
"""

import rand


def merge_sort(arr):
    """
    Sorts the input array using the merge sort algorithm.

    Args:
        arr (list): The list of numbers to be sorted.

    Returns:
        list: A sorted version of the input list.
    """
    if len(arr) == 1:  # Removed unnecessary parentheses
        return arr

    half = len(arr) // 2
    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """
    Recombines two sorted arrays into a single sorted array.

    Args:
        left_arr (list): The left sublist.
        right_arr (list): The right sublist.

    Returns:
        list: The recombined sorted array.
    """
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            right_index += 1
            merge_arr[left_index + right_index] = left_arr[left_index]
        else:
            left_index += 1
            merge_arr[left_index + right_index] = right_arr[right_index]

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]

    return merge_arr


# Create an array with random numbers
arr = rand.random_array([None] * 20)

# Sort the array using merge sort
arr_out = merge_sort(arr)

# Print the sorted array
print(arr_out)
