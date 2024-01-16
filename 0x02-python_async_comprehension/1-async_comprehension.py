#!/usr/bin/env python3
""" coroutine that collects 10 rand nubers using async over async_generator"""

import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Returns 10 rand numbers using async_generator from the prev task """
    result = [i async for i in async_generator() if i % 2]
    return result
