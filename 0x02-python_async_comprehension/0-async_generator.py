#!/usr/bin/env python3
"""
Module: 0-async_generator.py
This module contains a fucntion that takes no arguments
"""


import asyncio
import random


async def async_generator():
    """
    This method takes no arguments.

    The coroutine will loop 10 times,
    each time asynchronously wait 1 second,
    then yield a random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
