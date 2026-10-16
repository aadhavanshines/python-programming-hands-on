# Call the Pocket Library API as a client would: first with urllib from the
# standard library, then with httpx. To keep the example self-contained, the
# server runs in a background thread of this same program.
import json
import socket
import threading
import time
import urllib.error
import urllib.request

import httpx
import uvicorn

import books_api


def start_server():
    with socket.socket() as s:  # ask the system for a free port
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]
    server = uvicorn.Server(
        uvicorn.Config(books_api.app, port=port, log_level="warning")
    )
    threading.Thread(target=server.run, daemon=True).start()
    while not server.started:  # wait until it accepts requests
        time.sleep(0.05)
    return f"http://127.0.0.1:{port}"


base = start_server()

# 1. urllib: GET and POST with the standard library
with urllib.request.urlopen(f"{base}/books") as response:
    print("GET /books ->", response.status, json.loads(response.read()))

request = urllib.request.Request(
    f"{base}/books",
    data=json.dumps(
        {"title": "Dune", "author": "Frank Herbert", "year": 1965}
    ).encode(),
    headers={"Content-Type": "application/json"},
    method="POST",
)
with urllib.request.urlopen(request) as response:
    print("POST /books ->", response.status)
    print("  ", json.loads(response.read()))

try:
    urllib.request.urlopen(f"{base}/books/42")
except urllib.error.HTTPError as error:
    print("GET /books/42 ->", error.code, json.loads(error.read()))

# 2. httpx: the same work, with less code
with httpx.Client(base_url=base, timeout=5) as client:
    r = client.post(
        "/books",
        json={"title": "Emma", "author": "Jane Austen", "year": 1815},
    )
    print("POST /books ->", r.status_code)
    print("  ", r.json())

    r = client.get("/books", params={"author": "austen"})
    titles = [book["title"] for book in r.json()]
    print("GET /books?author=austen ->", r.status_code, titles)

    r = client.post("/books", json={"title": "Untitled"})
    print(
        "POST without author ->",
        r.status_code,
        r.json()["detail"][0]["msg"],
    )

    r = client.get("/books/42")
    try:
        r.raise_for_status()
    except httpx.HTTPStatusError as error:
        print(
            "raise_for_status:",
            error.response.status_code,
            error.response.json()["detail"],
        )
