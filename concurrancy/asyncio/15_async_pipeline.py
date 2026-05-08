"""
Asyncio Example 15: Async ETL Pipeline

Real-time Use Case:
Build a small Extract -> Transform -> Load pipeline.
"""

import asyncio


async def extract(raw_queue):
    for item in [" raw_user_1 ", " raw_user_2 ", " raw_user_3 "]:
        print("Extracted:", item)
        await raw_queue.put(item)
        await asyncio.sleep(0.5)

    await raw_queue.put(None)


async def transform(raw_queue, clean_queue):
    while True:
        item = await raw_queue.get()

        if item is None:
            await clean_queue.put(None)
            break

        cleaned = item.strip().replace("raw_", "").upper()
        print("Transformed:", cleaned)
        await clean_queue.put(cleaned)


async def load(clean_queue):
    while True:
        item = await clean_queue.get()

        if item is None:
            break

        print("Loaded:", item)


async def main():
    raw_queue = asyncio.Queue()
    clean_queue = asyncio.Queue()

    await asyncio.gather(
        extract(raw_queue),
        transform(raw_queue, clean_queue),
        load(clean_queue),
    )


asyncio.run(main())
