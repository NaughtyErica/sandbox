import asyncio
from datetime import datetime


async def print_num():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(0.1)


async def print_time():
    count = 0
    while True:
        if count % 2 == 0:
            now_time = datetime.now()
            print(f'{count} second passed. Now time = {now_time}')
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(print_num())
    task2 = asyncio.create_task(print_time())
    await asyncio.gather(task1, task2)

if __name__ == '__main__':
    asyncio.run(main())
