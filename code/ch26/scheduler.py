# Run tasks at set intervals with the standard library's sched module.
# The intervals here are tenths of a second so the example finishes quickly;
# for real use, think minutes or hours.
import sched
import time

scheduler = sched.scheduler(time.monotonic, time.sleep)
runs = {"check inbox": 0, "back up notes": 0}


def every(seconds, name, times, start):
    runs[name] += 1
    print(f"run {runs[name]} of {name!r}")
    if runs[name] < times:
        # Book the next run at an exact time, so small delays don't add up
        next_time = start + seconds * (runs[name] + 1)
        scheduler.enterabs(
            next_time, 1, every, (seconds, name, times, start)
        )


start = time.monotonic()
scheduler.enterabs(start + 0.1, 1, every, (0.1, "check inbox", 4, start))
scheduler.enterabs(
    start + 0.25, 1, every, (0.25, "back up notes", 2, start)
)
scheduler.run()  # blocks until no tasks are left
print("All tasks done.")
