# Chapter 23: Project: Pocket Library with SQLite

The SQLite version of Pocket Library is the `pocket` package in this folder:

```
cd code/ch23
python -m pocket add "Dune" "Frank Herbert" --year 1965
python -m pocket list
python -m pytest -q tests
```

`demo.py` runs a whole series of commands and prints what each shows.

Each `name.py` has its expected output in `name.out`. A `name.in` file holds what was typed when the program asked for input, `name.args` its command-line arguments, and `name.cmd` the command used instead of `python name.py` (for pytest or mypy).

## Programs

- `demo.py`
- `run_tests.py`

## Exercise solutions

Try the exercises yourself before you look.

- `solution_store.py`
