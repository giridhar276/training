"""
Asyncio Example 13: Async Log Monitor Pattern

Real-time Use Case:
Simulate watching log lines without blocking other async tasks.
"""

import asyncio
from pathlib import Path


async def monitor_logs(log_file):
    lines = log_file.read_text(encoding="utf-8").splitlines()

    for line in lines:
        await asyncio.sleep(0.5)

        if "ERROR" in line or "WARNING" in line:
            print("Important log found:", line)


async def heartbeat():
    for count in range(1, 6):
        print("Heartbeat", count)
        await asyncio.sleep(0.5)


async def main():
    log_file = Path(__file__).resolve().parents[1] / "data" / "server.log"

    await asyncio.gather(
        monitor_logs(log_file),
        heartbeat(),
    )


asyncio.run(main())
