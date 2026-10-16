# What a web API sends back: text in JSON format, which json.loads
# turns into ordinary dictionaries and lists.
import json

response_text = """
{
  "count": 2,
  "books": [
    {"id": 1, "title": "Dune", "author": "Frank Herbert", "year": 1965},
    {"id": 2, "title": "Emma", "author": "Jane Austen", "year": 1815}
  ]
}
"""

data = json.loads(response_text)
print(type(data))
print("Books returned:", data["count"])
for book in data["books"]:
    print(
        f"  #{book['id']} {book['title']} by {book['author']}"
        f" ({book['year']})"
    )

# Sending data works the other way round: a dictionary becomes JSON text
new_book = {"title": "Educated", "author": "Tara Westover", "year": 2018}
body = json.dumps(new_book)
print(body)
print(type(body))
