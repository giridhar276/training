"""
Asyncio Example 12: Semaphore Rate Limit

Concept:
Semaphore limits the number of concurrent async tasks.

Use Case:
Avoid hitting API rate limits.
"""

import asyncio


async def call_api(task_id, semaphore):
    async with semaphore:
        print(f"Calling API for task {task_id}")
        await asyncio.sleep(1)
        print(f"Completed API for task {task_id}")


async def main():
    semaphore = asyncio.Semaphore(3)

    tasks = [call_api(task_id, semaphore) for task_id in range(1, 11)]
    await asyncio.gather(*tasks)


asyncio.run(main())
