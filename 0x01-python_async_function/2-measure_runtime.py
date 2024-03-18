#!/usr/bin/env python3
"""
Module: 2-measure_runtime.py

This module contains a function that returns a float
"""

from asyncio import Task, run, gather
from typing import Any
from random import uniform
from itertools import repeat
from time import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This method takes 2 inegers n and max_delay as arguments
    that measures the total execution time for wait_n(n, max_delay)
    and returns total_time
    """
    start_time = time()
    run(wait_n(n, max_delay))
    end_time = time()
    total_time = end_time - start_time
    return total_time / n
