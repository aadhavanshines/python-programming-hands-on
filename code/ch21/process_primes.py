from concurrent.futures import ProcessPoolExecutor


def count_primes(start, stop):
    """Count the primes in range(start, stop): pure calculation."""
    count = 0
    for n in range(max(start, 2), stop):
        if all(n % d for d in range(2, int(n**0.5) + 1)):
            count += 1
    return count


# Required: each worker process imports this file
if __name__ == "__main__":
    ranges = [
        (0, 50_000),
        (50_000, 100_000),
        (100_000, 150_000),
        (150_000, 200_000),
    ]
    with ProcessPoolExecutor() as pool:
        counts = list(pool.map(count_primes, *zip(*ranges)))
    for (start, stop), count in zip(ranges, counts):
        print(f"{start:>7,} to {stop:>7,}: {count:,} primes")
    print(f"Total: {sum(counts):,}")
