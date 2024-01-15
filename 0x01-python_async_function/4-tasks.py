#!/usr/bin/env python3
""" async routint that takes 2 args """


import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Spawns wait_Return n times with the specified max_delay """
    # Create a list of coroutine objects using a generator expression
    coroutines = (task_wait_random(max_delay) for _ in range(n))

    # Wait for coroutines using asyncio.gather
    gatheredResults = asyncio.gather(*coroutines)

    # Await results and store in delays
    delays = sorted(await gatheredResults)
    return delays
