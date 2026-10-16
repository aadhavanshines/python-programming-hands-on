"""Run every listing in code/ and check its output, on every Python version.

Conventions for a listing code/chNN/name.py:
  name.in    text typed by the user, one line per input() call (optional)
  name.args  command-line arguments, one per line (optional)
  name.out   the expected output, as printed in the book
  name.cmd   run "python <this text>" instead of "python name.py" (for example
             "-m mypy name.py" or "-m pytest -q")
  name.versions  only check on these versions (one per line), when the output
             legitimately differs between versions (the file says why)
  name.runonly   check only that it runs without error; the output (timings)
             differs on every run, so the .out file is a recorded example
  name.skip  listing is not run (for example, it waits forever); the file says why
Interactive sessions code/chNN/name.txt are checked with doctest.

The listing runs in a fresh temporary copy of its chapter folder, so files it
writes never change the repository. input() is replaced with a version that
echoes what was typed, so the output looks exactly as it does in a terminal.

Install the packages first:  python -m pip install -r requirements.txt

Usage:
  python tests/run_listings.py                 check against the stored .out files
  python tests/run_listings.py --record        (re)write .out files with the main Python
  python tests/run_listings.py --only ch05     limit to one chapter
"""
import argparse
import difflib
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CODE = ROOT / "code"
# By default, check with the Python running this script. If you have made
# one virtual environment per version in .venvs/py3.12 ... .venvs/py3.15
# (as the author did), every one of them is used instead.
_VENVS = {v: ROOT / ".venvs" / f"py{v}" / "bin" / "python"
          for v in ("3.15", "3.14", "3.13", "3.12")}
PYTHONS = {v: str(p) for v, p in _VENVS.items() if p.exists()}
if not PYTHONS:
    PYTHONS = {f"{sys.version_info[0]}.{sys.version_info[1]}": sys.executable}
MAIN = next(iter(PYTHONS))
RUNNER = Path(__file__).resolve().parent / "echo_input.py"
TIMEOUT = 60


def env_for():
    # Run as in an ordinary terminal. CI services such as GitHub Actions set
    # CI, which makes pytest print longer failure summaries than you see at
    # home, so it is removed along with any PYTHON* settings.
    env = {k: v for k, v in os.environ.items()
           if not k.startswith("PYTHON") and k not in ("CI", "BUILD_NUMBER")}
    env.update(PYTHONDONTWRITEBYTECODE="1", NO_COLOR="1", PYTHON_COLORS="0",
               PYTHONHASHSEED="0", PYTHONUNBUFFERED="1", TERM="dumb", COLUMNS="76", LANG="C.UTF-8",
               PYTHONIOENCODING="utf-8",
               # Third-party pytest plugins installed on your computer can
               # add lines to pytest's output; the book's tests need none
               PYTEST_DISABLE_PLUGIN_AUTOLOAD="1")
    return env


def version_warnings(python):
    """Packages whose installed version differs from requirements.txt."""
    wanted = {}
    for line in (ROOT / "requirements.txt").read_text().splitlines():
        if "==" in line and not line.startswith("#"):
            name, version = line.split("==")
            wanted[name.strip()] = version.strip()
    code = ("import importlib.metadata as m, json, sys\n"
            "out = {}\n"
            "for n in sys.argv[1:]:\n"
            "    try: out[n] = m.version(n)\n"
            "    except m.PackageNotFoundError: out[n] = None\n"
            "print(json.dumps(out))")
    import json
    p = subprocess.run([python, "-c", code, *wanted], capture_output=True, text=True)
    found = json.loads(p.stdout or "{}")
    return [f"{n} {found.get(n) or 'not installed'} (the book used {v})"
            for n, v in wanted.items() if found.get(n) != v]


def run(python, listing):
    """Run one listing in a temporary copy of its folder; return its output."""
    chapter = listing.parent
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp) / chapter.name
        shutil.copytree(chapter, work)
        args_file = listing.with_suffix(".args")
        args = args_file.read_text().split("\n") if args_file.exists() else []
        args = [a for a in args if a]
        stdin_file = listing.with_suffix(".in")
        stdin = stdin_file.read_text() if stdin_file.exists() else ""
        # Only programs that read input need the echoing runner; the others
        # run directly, so their tracebacks look exactly as in a terminal.
        cmd_file = listing.with_suffix(".cmd")
        if cmd_file.exists():
            cmd = [python, *shlex.split(cmd_file.read_text().strip())]
        elif stdin_file.exists():
            cmd = [python, str(RUNNER), listing.name, *args]
        else:
            cmd = [python, listing.name, *args]
        # One stream, unbuffered: output and error messages appear in the
        # same order as in a terminal
        p = subprocess.run(cmd, cwd=work, input=stdin, stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT, text=True, env=env_for(), timeout=TIMEOUT)
        out = p.stdout
        # Show file names as "typo.py", not the temporary folder's full path
        out = out.replace(str(work) + os.sep, "")
        # Standard-library frames: show ".../lib/python3.15/..." instead of
        # this computer's install folder (yours will differ too)
        out = re.sub(r'File "[^"]*?/lib/(python3\.\d+)/', r'File ".../lib/\1/', out)
        # pytest prints how long the tests took; that differs on every run
        out = re.sub(r" in \d+\.\d+s", " in 0.01s", out)
        return out, p.returncode


def comparable(text):
    """Error reports differ between versions in the frames and markers they
    show. If the output ends with an error, compare everything before the
    error report, and the final error line."""
    lines = text.rstrip("\n").split("\n")
    if not lines or not re.match(r"^[A-Za-z_.]*(Error|Exception|Interrupt|Exit)\b", lines[-1]):
        return text
    start = next((i for i, ln in enumerate(lines)
                  if ln.startswith("Traceback (most recent call last)") or ln.startswith('  File "')),
                 len(lines) - 1)
    return "\n".join(lines[:start]) + "\n...\n" + lines[-1]


def check_doctests(python, txt):
    p = subprocess.run([python, "-m", "doctest", "-o", "ELLIPSIS", "-o", "NORMALIZE_WHITESPACE",
                        txt.name], cwd=txt.parent, capture_output=True, text=True,
                       env=env_for(), timeout=TIMEOUT)
    return p.returncode == 0, p.stdout + p.stderr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--record", action="store_true")
    ap.add_argument("--only")
    ap.add_argument("--python", nargs="*", default=list(PYTHONS))
    a = ap.parse_args()
    listings = sorted(p for p in CODE.glob("ch*/*.py")
                      if not p.name.startswith("_") and not (a.only and a.only not in str(p)))
    sessions = sorted(p for p in [*CODE.glob("ch*/*.txt"), *CODE.glob("appendix/*.txt")]
                      if not (a.only and a.only not in str(p)))
    for ver in a.python:
        diffs = version_warnings(PYTHONS[ver])
        if diffs and not a.record:
            print(f"Note for Python {ver}: some packages differ from requirements.txt,")
            print("so a few outputs may differ: " + "; ".join(diffs))
    failures, checked = [], 0
    for listing in listings:
        if listing.with_suffix(".skip").exists():
            continue
        expected_file = listing.with_suffix(".out")
        if a.record:
            out, _ = run(PYTHONS[MAIN], listing)
            expected_file.write_text(out)
            print(f"recorded {listing.relative_to(ROOT)}")
            continue
        if not expected_file.exists():
            failures.append(f"{listing.relative_to(ROOT)}: no .out file")
            continue
        expected = expected_file.read_text()
        versions_file = listing.with_suffix(".versions")
        versions = versions_file.read_text().split() if versions_file.exists() else a.python
        for ver in [v for v in a.python if v in versions]:
            out, code = run(PYTHONS[ver], listing)
            checked += 1
            if listing.with_suffix(".runonly").exists():
                if code != 0:
                    failures.append(f"{listing.relative_to(ROOT)} on {ver}: exit code {code}\n{out}")
                continue
            if comparable(out) != comparable(expected):
                diff = "".join(difflib.unified_diff(comparable(expected).splitlines(True),
                                                    comparable(out).splitlines(True),
                                                    "expected", f"python {ver}"))
                failures.append(f"{listing.relative_to(ROOT)} on {ver}:\n{diff}")
    if not a.record:
        for txt in sessions:
            for ver in a.python:
                ok, msg = check_doctests(PYTHONS[ver], txt)
                checked += 1
                if not ok:
                    failures.append(f"{txt.relative_to(ROOT)} on {ver}:\n{msg}")
    for f in failures:
        print("FAIL", f)
    if not a.record:
        versions = ", ".join(a.python)
        print(f"{checked} checks ({len(listings)} listings, {len(sessions)} sessions, "
              f"Python {versions}); {len(failures)} failures")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
