#!/usr/bin/env python3
"""
Module: 7-to_kv.py

This module contains a function that returns a tuple
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This method takes a tring k and an int OR float v as args
    and returns a tuple.

    The first element of the tuple is the string k.

    The second element is the square of the int/float v and should
    be annotated as float
    """
    return (k, v**2)
