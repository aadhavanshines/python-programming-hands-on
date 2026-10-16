import asyncio
import time


async def fetch(name, seconds):
    """Pretend to fetch a web page, waiting without blocking other tasks."""
    await asyncio.sleep(seconds)
    return f"{name} ({seconds} s)"


async def main():
    start = time.perf_counter()
    pages = await asyncio.gather(
        fetch("news", 0.3), fetch("weather", 0.1), fetch("sport", 0.2)
    )
    elapsed = time.perf_counter() - start
    print("In the order asked:", pages)
    # One after another, the three would take 0.6 s
    print("Faster than one after another:", elapsed < 0.6)

    tasks = [fetch("news", 0.3), fetch("weather", 0.1), fetch("sport", 0.2)]
    for finished in asyncio.as_completed(tasks):
        print("Finished:", await finished)

    try:
        await asyncio.wait_for(fetch("slow server", 2), timeout=0.2)
    except TimeoutError:
        print("Gave up on the slow server after 0.2 s")


asyncio.run(main())
