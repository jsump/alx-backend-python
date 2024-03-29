#!/usr/bin/env python3
"""
Module: 9-element_length.py

This module contains a function that returns values with
the appropriate types
"""


from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    this method returbs values with appropriate types
    """
    return [(i, len(i)) for i in lst]
