#!/usr/bin/env python3
"""
Module: 2-floor.py

This module contains a function that returns the floor of the float
"""


def floor(n: float) -> float:
    """
    This method takes n as argumrnt and returns the floor
    of the float.
    """
    return int(n) if n > 0 else int(n) - 1
