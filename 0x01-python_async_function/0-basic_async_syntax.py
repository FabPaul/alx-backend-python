#!/usr/bin/env python3
""" Async coroutinf that takes an int as arg """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ waits for a random delay between 0 and max_delay and returns  it"""
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
