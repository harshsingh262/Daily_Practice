import asyncio
async def fun():
    print("This is")
    await asyncio.sleep(1)
    print("asynchronous programming")
    await asyncio.sleep(1)
    print("and not multi-threading")
asyncio.run(fun())