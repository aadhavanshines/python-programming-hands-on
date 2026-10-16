# Chapter 17: Virtual Environments, Packages and Project Layout

The Pocket Library package is in `pocket-library/`. Install it in a virtual environment, then use the `pocket` command and run its tests:

```
cd code/ch17/pocket-library
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install -e ".[test]"
pocket add "Dune" "Frank Herbert" 1965
pocket list
python -m pytest -q
```

`install_transcript.out` shows a complete run of these steps, as tested on every Python version.

Each `name.py` has its expected output in `name.out`. A `name.in` file holds what was typed when the program asked for input, `name.args` its command-line arguments, and `name.cmd` the command used instead of `python name.py` (for pytest or mypy).

## Exercise solutions

Try the exercises yourself before you look.

- `solution_stats.py`
