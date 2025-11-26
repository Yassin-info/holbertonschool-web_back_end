#!/usr/bin/env python3
"""Module that defines a function to sum a mixed list of integers and floats."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing integers and floats.

    Args:
        mxd_lst: A list of integers and/or float numbers

    Returns:
        The sum of all numbers in the list as a float
    """
    return sum(mxd_lst)
