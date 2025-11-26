#!/usr/bin/env python3
"""Module that defines a function to sum a list of floats."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of float numbers.

    Args:
        input_list: A list of float numbers

    Returns:
        The sum of all floats in the list as a float
    """
    return sum(input_list)
