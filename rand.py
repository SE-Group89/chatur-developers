"""
This module provides a function to populate an array with random integers
using the 'shuf' command-line utility.
"""

import subprocess


def random_array(arr):
    """
    Fill the provided array with random integers between 1 and 20.

    Args:
        arr (list): A list to be filled with random integers.

    Returns:
        list: The list filled with random integers.
    """
    for i, _ in enumerate(arr):
        result = subprocess.run(
            ["shuf", "-i1-20", "-n1"],
            capture_output=True,
            check=True,  # Ensure subprocess raises an error on failure
            text=True    # Return output as a string
        )
        arr[i] = int(result.stdout.strip())
    return arr
