#!/usr/bin/env python3
"""
A python script
Concurrent coroutines using async wait and asyncio.gather
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    Wait for a random amount of time
    """
    return asyncio.create_task(wait_random(max_delay))
