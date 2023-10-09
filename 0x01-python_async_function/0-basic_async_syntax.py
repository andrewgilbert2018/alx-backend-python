#!/usr/bin/env python3
"""
The basics of async:
Basic async syntax
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random amount of time
    """
    waiting_time = random.uniform(0, max_delay)
    await asyncio.sleep(waiting_time)
    return (waiting_time)
