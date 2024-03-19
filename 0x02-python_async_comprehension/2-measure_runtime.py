#!/usr/bin/env python3
"""
Module: 2-measure_runtime.py

This module contains a function that will measure runtime and return it.
"""


import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This function executes async_comprehension four times
    is parallel using asyncio.gather

    It will also measure the total runtime and return it
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
