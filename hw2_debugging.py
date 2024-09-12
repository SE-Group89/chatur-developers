"""
This module contains an implementation of merge sort and a function
to generate a random array using the 'rand' module.
"""

import rand

def merge_sort(array):
    """
    Perform merge sort on the given array.
    
    Args:
        array (list): The list of elements to be sorted.
        
    Returns:
        list: A sorted list.
    """
    if len(array) <= 1:
        return array

    midpoint = len(array) // 2
    left_half = merge_sort(array[:midpoint])
    right_half = merge_sort(array[midpoint:])
    return recombine(left_half, right_half)

def recombine(left_half, right_half):
    """
    Merge two sorted lists into a single sorted list.
    
    Args:
        left_half (list): The first sorted list.
        right_half (list): The second sorted list.
        
    Returns:
        list: A merged and sorted list.
    """
    left_index = 0
    right_index = 0
    merged_array = [None] * (len(left_half) + len(right_half))
    merge_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            merged_array[merge_index] = left_half[left_index]
            left_index += 1
        else:
            merged_array[merge_index] = right_half[right_index]
            right_index += 1
        merge_index += 1

    # Copy remaining elements
    while left_index < len(left_half):
        merged_array[merge_index] = left_half[left_index]
        left_index += 1
        merge_index += 1

    while right_index < len(right_half):
        merged_array[merge_index] = right_half[right_index]
        right_index += 1
        merge_index += 1

    return merged_array

# Generate a random array and sort it using merge sort
array = rand.random_array([None] * 20)
sorted_array = merge_sort(array)

print(sorted_array)
