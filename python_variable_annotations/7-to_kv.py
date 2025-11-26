#!/usr/bin/env python3
"""Module that defines a function to create a tuple from a string and a number."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple from a string and the square of an int or float.

    Args:
        k: A string
        v: An integer or float number

    Returns:
        A tuple where the first element is k and the second is v squared as float
    """
    return (k, v ** 2)
