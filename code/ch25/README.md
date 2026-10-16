# Chapter 25: Project: Web APIs: Calling Them and Building One

Start the web API, then open http://127.0.0.1:8000/docs in your browser:

```
cd code/ch25
python -m uvicorn books_api:app --reload
```

`client_demo.py` starts the server itself and calls it with urllib and httpx; `python -m pytest -q test_books_api.py` runs the tests.

Each `name.py` has its expected output in `name.out`. A `name.in` file holds what was typed when the program asked for input, `name.args` its command-line arguments, and `name.cmd` the command used instead of `python name.py` (for pytest or mypy).

## Programs

- `books_api.py`
- `client_demo.py`
- `json_responses.py`
- `test_books_api.py`

## Exercise solutions

Try the exercises yourself before you look.

- `solution_api.py`
