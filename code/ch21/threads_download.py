import time
from concurrent.futures import ThreadPoolExecutor


def download(name):
    """Pretend to download a file: most of the time is spent waiting."""
    time.sleep(0.5)
    return f"{name}: {len(name) * 1000} bytes"


files = [
    "report.pdf",
    "photo.jpg",
    "data.csv",
    "song.mp3",
    "notes.txt",
    "map.png",
]

start = time.perf_counter()
results = [download(f) for f in files]
sequential = time.perf_counter() - start

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=6) as pool:
    # map gives the results in the original order
    threaded_results = list(pool.map(download, files))
threaded = time.perf_counter() - start

print("\n".join(threaded_results))
print("Same results:", results == threaded_results)
print("Threads at least 4 times faster:", sequential / threaded >= 4)
