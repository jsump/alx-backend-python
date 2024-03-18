#!/usr/bin/env python3
"""
Module: 3-tasks.py

This module contains a function that returns asyncio.Task"""


from asyncio import Task
from typing import Any
from random import uniform
from time import sleep

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    This method takes an integer max_delay and returns asyncio.Task
    """
    async def wait_random_wrapper(max_delay: int) -> Any:
        delay = await wait_random(max_delay)
        await sleep(delay)
        return f"Waited for {delay: .2f} seconds"

    return wait_random_wrapper(max_delay)
