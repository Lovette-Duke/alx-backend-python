#!/usr/bin/env python3
"""creates an async generator and uses the yield keyword"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ loop 10 times, wait 1 second and yields a random number b/w 0 and 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
