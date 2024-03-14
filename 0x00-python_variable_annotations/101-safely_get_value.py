#!/usr/bin/env python3
"""
Module: 101-safely_get_value.py

This module contains a function that returns values with
the appropriate types
"""


from typing import Mapping, Any, Union, Dict, TypeVar


T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
) -> Union[Any, T]:
    """
    this method returbs values with appropriate types
    """
    if key in dct:
        return dct[key]
    else:
        return default
