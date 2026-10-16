import threading

counter = 0
lock = threading.Lock()


def add_many(times):
    global counter
    for _ in range(times):
        with lock:  # only one thread at a time may change counter
            counter += 1


threads = [
    threading.Thread(target=add_many, args=(100_000,)) for _ in range(4)
]
for t in threads:
    t.start()
for t in threads:
    t.join()  # wait for every thread to finish
print("Counter:", counter)
