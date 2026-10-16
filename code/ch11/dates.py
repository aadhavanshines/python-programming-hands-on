from datetime import date, datetime, timedelta

today = date(2026, 10, 15)  # a fixed date, so the output matches the book
deadline = date(2026, 12, 24)
print("Days to go:", (deadline - today).days)
print("In two weeks:", today + timedelta(weeks=2))
print(today.strftime("%A %d %B %Y"))

meeting = datetime(2026, 10, 15, 14, 30)
print(meeting.isoformat(), "->", meeting.strftime("%H:%M on %d/%m"))
parsed = datetime.strptime("2026-11-02 09:15", "%Y-%m-%d %H:%M")
print("Parsed:", parsed, "| weekday:", parsed.strftime("%a"))

# For the real date and time, use date.today() and datetime.now().
