#!/usr/bin/env python3
"""
Module: 6-sum_mixed_list.py

This module contains a function that returns sum of a mixed
listof dloats and intergers as a float
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    this function takes a mixed list of integers and floats,
    mxd_lst and returns their sum as float
    """
    return sum(mxd_lst)
