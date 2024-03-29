"""
anext()
When awaited, return the next item from the given asynchronous iterator,
or default if the given interator is exhausted
This calls the __anext__() method of async_iterator, returning an awaitable.
"""

import asyncio

class AsyncIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __aiter__(self):
        self.cur = self.start
        return self

    async def __anext__(self):
        await asyncio.sleep(1)
        if self.cur >= self.stop:
            raise StopAsyncIteration

        self.cur += 1
        return self.cur - 1


async def exapmle():
    custom_obj = AsyncIterator(1, 10)
    obj_iter = aiter(custom_obj)
    print(await anext(obj_iter))
    print(await anext(obj_iter))
    print(await anext(obj_iter))

asyncio.run(exapmle())
