#!/usr/bin/env python3
"""
Measure the runtime
Function to measure the time execution of a program
"""
from time import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Measure the time execution of a program
    """
    start = time()
    asyncio.run(wait_n(n, max_delay))
    end = time()
    return (end - start) / n
