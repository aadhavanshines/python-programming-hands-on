import asyncio
from concurrent.futures import ThreadPoolExecutor


def word_counts(texts):
    """Count words in many texts with a pool of threads, in order."""
    with ThreadPoolExecutor(max_workers=4) as pool:
        return list(pool.map(lambda text: len(text.split()), texts))


async def fetch_all(names, limit):
    """Fetch every name, but never more than `limit` at the same time."""
    semaphore = asyncio.Semaphore(limit)
    running = 0
    most = 0

    async def fetch(name):
        nonlocal running, most
        async with semaphore:
            running += 1
            most = max(most, running)
            await asyncio.sleep(0.05)
            running -= 1
            return name.upper()

    results = await asyncio.gather(*(fetch(n) for n in names))
    return results, most


if __name__ == "__main__":
    print(word_counts(["one two", "three", "", "four five six"]))
    results, most = asyncio.run(
        fetch_all(["a", "b", "c", "d", "e"], limit=2)
    )
    print(results, "at most", most, "at once")
