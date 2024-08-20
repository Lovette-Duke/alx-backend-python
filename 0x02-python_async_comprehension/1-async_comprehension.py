#!/usr/bin/env python3
""" create an async comprehension """


from typing import List
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ creates async comprehension for 10 random numbers b/w 0 and 10"""
    result = [i async for i in async_generator()]
    return result
