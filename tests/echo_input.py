"""Run a listing with input() echoing what was typed, as a terminal shows it.
Usage: python echo_input.py listing.py [args...]"""
import builtins
import runpy
import traceback
import sys


def echo_input(prompt=""):
    sys.stdout.write(str(prompt))
    line = sys.stdin.readline()
    if not line:
        raise EOFError("EOF when reading a line")
    line = line.rstrip("\n")
    print(line)
    return line


builtins.input = echo_input
sys.argv = sys.argv[1:]
sys.path.insert(0, ".")
script = sys.argv[0]
try:
    runpy.run_path(script, run_name="__main__")
except SystemExit:
    raise
except BaseException as error:
    # Show the traceback from the listing's own frames, as a terminal would
    tb = error.__traceback__
    while tb is not None and not tb.tb_frame.f_code.co_filename.endswith(script):
        tb = tb.tb_next
    traceback.print_exception(type(error), error, tb)
    sys.exit(1)
