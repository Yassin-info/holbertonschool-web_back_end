#!/usr/bin/env python3
"""Module that defines an asynchronous coroutine for random delays."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds.

    Args:
        max_delay: Maximum delay in seconds (default: 10)

    Returns:
        The actual delay that was waited
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return max_delay
