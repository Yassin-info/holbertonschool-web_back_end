#!/usr/bin/env python3
"""Module that defines a function to get element lengths from an iterable."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Get the length of each element in an iterable.

    Args:
        lst: An iterable of sequences (strings, lists, tuples, etc.)

    Returns:
        A list of tuples where each tuple contains the element and its length
    """
    return [(i, len(i)) for i in lst]
