#!/usr/bin/env python3
"""
Module: 4-tasks.py

This module contains a function that returns the list
of random defualt values in ascending order
"""


import asyncio
from typing import List
from random import uniform
from itertools import repeat

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    This method takes 2 int arguments in this order:n and max_delay.
    wait_n should return the list of the delays(float values)
    The list of delays should be in ascending order
    """
    delays = await asyncio.gather(
            *(task_wait_random(max_delay) for _ in repeat(None, n))
            )
    return sorted(delays)
