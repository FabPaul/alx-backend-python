#!/usr/bin/env python3
""" Function with 2 int args that measures total exec time for wait_n()"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measures total exec time for wait_n() and returns total_time /n """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    average_time_per_operation = total_time / n

    return average_time_per_operation
