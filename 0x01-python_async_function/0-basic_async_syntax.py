#!/usr/bin/env python3
''' an async function that waits for a random delay and returns it'''


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''waits for a random delay in secornds'''
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
