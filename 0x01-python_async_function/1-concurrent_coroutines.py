#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
Concurrent coroutines using async wait and asyncio.gather
"""
from asyncio import gather
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Wait for a random amount of time
    """
    gather_list = await gather(*[wait_random(max_delay) for _ in range(n)])
    return sorted(gather_list)
