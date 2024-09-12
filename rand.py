"""
This module provides a function to generate a random array of integers.
"""

import subprocess


def random_array(arr):
    """
    Fills the input array with random integers between 1 and 20 using the 'shuf' command.

    Args:
        arr (list): A list to be populated with random integers.

    Returns:
        list: The array populated with random integers.
    """
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True
        )
        arr[i] = int(shuffled_num.stdout)
    return arr
