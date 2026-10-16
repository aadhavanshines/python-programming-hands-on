import re

text = """Contact Meera at meera.k@example.com or 020 7946 0018.
Orders: orders@example.org, phone 020 7946 0991. Office hours 9-17."""

emails = re.findall(r"[\w.]+@[\w.]+\.\w+", text)
print("Emails:", emails)

phones = re.findall(r"\d{3} \d{4} \d{4}", text)
print("Phones:", phones)

masked = re.sub(r"(\d{3} \d{4}) \d{4}", r"\1 ****", text)
print(masked)

match = re.search(r"hours (\d+)-(\d+)", text)
if match:
    print("Opens at", match.group(1), "and closes at", match.group(2))
