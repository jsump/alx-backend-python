#!/usr/bin/env python3
"""
Module: 100-safe_first_element.py

This module contains a function that returns values with
the appropriate types
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    this method returbs values with appropriate types
    """
    if lst:
        return lst[0]
    else:
        return None
