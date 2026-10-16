def handle(command):
    match command.split():
        case ["quit" | "exit"]:
            return "Goodbye."
        case ["add", title]:
            return f"Adding {title!r}."
        case ["add", title, year] if year.isdigit():
            return f"Adding {title!r} from {year}."
        case ["remove", *titles] if titles:
            return f"Removing {len(titles)} book(s): {', '.join(titles)}."
        case ["help" | "?"]:
            return "Commands: add, remove, quit."
        case []:
            return "Please type a command."
        case _:
            return f"I don't understand {command!r}."


for text in [
    "add Dune",
    "add Emma 1815",
    "remove Dune Emma",
    "?",
    "",
    "fly",
    "exit",
]:
    print(f"{text!r:20} -> {handle(text)}")
