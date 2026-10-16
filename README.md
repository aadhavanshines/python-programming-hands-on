# Python Programming Hands-On: Code

[![Check every listing](https://github.com/aadhavanshines/python-programming-hands-on/actions/workflows/check.yml/badge.svg)](https://github.com/aadhavanshines/python-programming-hands-on/actions/workflows/check.yml)

All the programs, data files, exercise solutions and tests from the book ***Python Programming Hands-On: Learn Python from Basic to Advanced by Writing Real Programs, with Exercises, Solutions and Every Example Tested*** by Aadhavan Muthurengan, arranged by chapter.

Every program here was run on Python 3.12, 3.13, 3.14 and 3.15, and its output compared with the output printed in the book. The expected output of each program is stored next to it, so you can check your own runs. The same check runs on GitHub after every change, on all four versions, and its results are public on the [Actions tab](https://github.com/aadhavanshines/python-programming-hands-on/actions).

## Getting started

1. Install Python 3.12 or newer from [python.org](https://www.python.org/downloads/).
2. Download this repository: the green **Code** button, then **Download ZIP**, or `git clone` it.
3. Parts I and II (Chapters 1 to 11) need nothing else. For Parts III to V, create a virtual environment in the repository folder and install the packages the book uses:

```
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
```

4. Go to a chapter's folder and run a program, for example `cd code/ch05` and `python guessing_game.py`. On macOS, type `python3` instead of `python` until you activate a virtual environment.

Type the short programs yourself first if you can: you'll learn more, and the files here are there to check against.

## Chapters

| Chapter | Topic | Programs | Exercise solutions |
| --- | --- | --- | --- |
| 1 | [Welcome to Python](code/ch01/) | 3 | 1 |
| 2 | [Variables, Numbers and Strings](code/ch02/) | 5 | 3 |
| 3 | [Input, Output and Conversions](code/ch03/) | 6 | 3 |
| 4 | [Making Decisions](code/ch04/) | 5 | 3 |
| 5 | [Loops](code/ch05/) | 6 | 3 |
| 6 | [Lists and Tuples](code/ch06/) | 4 | 3 |
| 7 | [Dictionaries and Sets](code/ch07/) | 4 | 3 |
| 8 | [Functions](code/ch08/) | 6 | 1 |
| 9 | [Working with Text](code/ch09/) | 4 | 1 |
| 10 | [Files and Exceptions](code/ch10/) | 8 | 1 |
| 11 | [Modules and the Standard Library](code/ch11/) | 6 | 1 |
| 12 | [Classes and Objects](code/ch12/) | 3 | 1 |
| 13 | [Inheritance, Dataclasses and Special Methods](code/ch13/) | 5 | 1 |
| 14 | [Comprehensions, Iterators and Generators](code/ch14/) | 4 | 1 |
| 15 | [Testing with pytest](code/ch15/) | 5 | 2 |
| 16 | [Debugging, Logging and Reading Tracebacks](code/ch16/) | 6 | 1 |
| 17 | [Virtual Environments, Packages and Project Layout](code/ch17/) | 0 | 1 |
| 18 | [Decorators and Context Managers](code/ch18/) | 4 | 1 |
| 19 | [Type Hints and Static Checking](code/ch19/) | 4 | 1 |
| 20 | [Functional Tools and Pattern Matching](code/ch20/) | 5 | 1 |
| 21 | [Concurrency: Threads, Processes and asyncio](code/ch21/) | 4 | 1 |
| 22 | [Performance: Measuring, Profiling and Choosing Data Structures](code/ch22/) | 4 | 1 |
| 23 | [Project: Pocket Library with SQLite](code/ch23/) | 2 | 1 |
| 24 | [Project: Data Analysis with CSV, pandas and Charts](code/ch24/) | 4 | 1 |
| 25 | [Project: Web APIs: Calling Them and Building One](code/ch25/) | 4 | 1 |
| 26 | [Project: Automating Everyday Tasks](code/ch26/) | 8 | 1 |
| B, C | [Cheat sheet and common errors](code/appendix/) | shell sessions | |

## What the files are

| File | Contents |
| --- | --- |
| `name.py` | A program from the book |
| `name.out` | Its output, exactly as printed in the book |
| `name.in` | What was typed when the program asked for input |
| `name.args` | Its command-line arguments, one per line |
| `name.cmd` | The command used instead of `python name.py`, such as running pytest or mypy |
| `name.txt` | A Python shell session: type the lines after `>>>` |
| `solution_*.py` | Worked solutions to the chapter's exercises |
| `name.versions` | The program's output is checked only on these Python versions (the debugger session, whose prompts differ slightly between versions) |
| `name.runonly` | The program prints timings, which differ on every computer, so only a clean run is checked |

## Check every program yourself

`tests/run_listings.py` runs every program and shell session and compares the output with the stored `.out` files:

```
python tests/run_listings.py               # everything
python tests/run_listings.py --only ch05   # one chapter
```

Run it in a fresh virtual environment with the exact versions from `requirements.txt` (step 3 above). It uses the Python you run it with, and it tells you at the start if any installed package differs from the versions the book used. Output that depends on your computer, such as timings, is never compared, and pytest plugins you may have installed elsewhere are switched off so that they can't add lines to the output. The whole check takes a few minutes; `--only` runs one chapter at a time.

If a comparison fails, the harness shows the difference. A different Python or package version can occasionally word a message differently; the ideas stay the same. Don't re-record the `.out` files to make a failure go away: they are the book's printed output. If you find a real difference with the pinned versions, please open an issue.

To share the code, use GitHub's **Download ZIP** or `git archive`: they contain only the files in the repository, without the `__pycache__` and `.pytest_cache` folders that running the programs creates on your computer.

## License

The code is released under the MIT License (see `LICENSE`): use it and adapt it freely in your own work. All people, books, shops and figures in the examples are fictional, and email addresses use the reserved `.example` domain.

Python is a trademark of the Python Software Foundation. This repository and the book are independent and not affiliated with the Python Software Foundation.
