import asyncio

async def a():
    await c(0.1)

async def b():
    await c(0.2)

async def c(n):
    await d(n)

async def d(n):
    await asyncio.sleep(n)

async def run():
    await asyncio.gather(a(), b())

if __name__ == "__main__":
    asyncio.run(run())
