#!/usr/bin/env python3
"""
Module: 8-make_multiplier.py

This module contains a function that returns a function that
multiplies a float bya multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This method takes a floa 'multiplier' as an argumrnt and returns
    a function that multiplies float by a multiplier.
    """
    def multiply_float(value: float) -> float:
        return value * multiplier

    return multiply_float
