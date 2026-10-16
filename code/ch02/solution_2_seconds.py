total_seconds = 10_000
hours = total_seconds // 3600
minutes = total_seconds % 3600 // 60
seconds = total_seconds % 60
print(f"{total_seconds} seconds is {hours} h {minutes} min {seconds} s")
