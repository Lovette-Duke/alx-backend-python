#!/usr/bin/env python3
'''measures total execution time for wait_n function'''


import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''mearsures average runtime of wait_n'''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    return (end_time() - start_time) / n
