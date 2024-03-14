#!/usr/bin/env python3
"""
Module: 102-type_checking.py

This module contains a function that returns values with
the appropriate types
"""


from typing import Tuple, Any, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    this method returbs values with appropriate types
    """
    zoomed_in: List = (
            item for item in lst for _ in range(factor)
    )
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
