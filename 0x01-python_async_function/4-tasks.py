#!/usr/bin/env python3
"""
Concurrent coroutines using async wait and asyncio.gather
"""
from asyncio import gather
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Wait for a random amount of time
    """
    gather_list = await gather(
        *[task_wait_random(max_delay) for _ in range(n)]
        )
    return gather_list
