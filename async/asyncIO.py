import asyncio
import time


# syncron example
def count():
    print("One")
    time.sleep(1)
    print("Two")


def main():
    for _ in range(3):
        count()


async def count2():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main2():
    await asyncio.gather(count2(), count2(), count2())


# creating a procecs in seperate threath
def blocking_procec():
    print("sleep is not running")
    # time.sleep(5)
    with open("text.txt", "w") as fs:
        for i in range(10000):
            fs.write(f"Item {i}\n")


async def seperate_treath():
    print("procec has running")
    await asyncio.to_thread(blocking_procec)
    print("procec still running")


# using with a low level api
from concurrent.futures import ThreadPoolExecutor

threat = ThreadPoolExecutor()


async def seperate_treath_low():
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(threat, blocking_procec)


if __name__ == "__main__":
    start_time = time.perf_counter()
    # main()
    # asyncio.run(main2())
    asyncio.run(seperate_treath())
    # asyncio.run(seperate_treath_low())

    end_time = time.perf_counter() - start_time
    print(f"{__file__} executed in {end_time:0.2f}")
