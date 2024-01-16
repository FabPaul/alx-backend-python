#!/usr/bin/env python3
""" A coroutine that takes no args, loops 10 times and waits 1 secs"""

import asyncio
import random


async def async_generator():
    """ yields a random number between 0-10 """
    for _ in range(10):
        await asyncio.sleep(1)
        rand_num = random.uniform(0, 10)  # or random.random() * 10
        yield rand_num
