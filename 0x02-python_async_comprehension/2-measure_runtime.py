#!/usr/bin/env python3
"""
Module: 2-measure_runtime.py

This modle contains a function that will measure runtime and return it.
"""


import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This function executes async_comprehension four times
    is parallel using asyncio.gather

    It will also measure the total runtime and return it
    """
    start_time = time()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    end_time = time()
    total_runtime = end_time - start_time
    return total_runtime
