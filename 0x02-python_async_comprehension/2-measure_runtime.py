#!/usr/bin/env python3
""" measures the total runtime of the async_comprehension script"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measures async_comprehension runtime, returns it"""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    return time.time() - start_time
