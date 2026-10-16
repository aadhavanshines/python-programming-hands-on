# Turn a CSV file into an HTML page you can open in any browser.
import csv
import html
from pathlib import Path

with open("reading_log.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))


def cell(text, tag="td"):
    return f"<{tag}>{html.escape(text)}</{tag}>"  # & < > become safe HTML


header = "".join(cell(name.title(), "th") for name in rows[0])
body = "\n".join(
    "<tr>" + "".join(cell(v) for v in row.values()) + "</tr>"
    for row in rows
)
pages = sum(int(row["pages"]) for row in rows)

page = f"""<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>Reading log</title>
<style>
  body {{ font-family: sans-serif; }}
  td, th {{ padding: 4px 12px; }}
</style></head>
<body>
<h1>Reading log</h1>
<p>{len(rows)} books, {pages:,} pages.</p>
<table>
<tr>{header}</tr>
{body}
</table>
</body>
</html>
"""
Path("reading_log.html").write_text(page, encoding="utf-8")
print(f"Wrote reading_log.html ({len(rows)} rows)")
print(cell("Pride & Prejudice"))  # & becomes &amp;
