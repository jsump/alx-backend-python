#!/usr/bin/env python3
"""
Module: 1-async_comprehension.py

This module contains a function that returns 10 random numbers
using an async
"""


import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    This function takes no arguments.

    This couritine will collect 10 random numbers
    using async comprehension over async_generator,
    then return the 10 random numberrs
    """
    random_floats = [num async for num in async_generator()]
    return random_floats
