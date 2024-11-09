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


if __name__ == "__main__":
    start_time = time.perf_counter()
    # main()
    asyncio.run(main2())
    end_time = time.perf_counter() - start_time
    print(f"{__file__} executed in {end_time:0.2f}")
