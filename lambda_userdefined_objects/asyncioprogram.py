

import asyncio


async def task1():
    print("task1 is started")
    await asyncio.sleep(3)
    print("task1 copmleted")

async def task2():
    print("task2 is started")
    await asyncio.sleep(2)
    print("task2 copmleted")


async def main():
    await asyncio.gather(task1(),task2())

asyncio.run(main())