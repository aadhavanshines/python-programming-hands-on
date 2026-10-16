import argparse

parser = argparse.ArgumentParser(
    description="Greet someone, politely or loudly."
)
parser.add_argument("name", help="who to greet")
parser.add_argument(
    "--times", type=int, default=1, help="how many greetings"
)
parser.add_argument(
    "--shout", action="store_true", help="greet in capitals"
)
args = parser.parse_args()

for _ in range(args.times):
    message = f"Hello, {args.name}!"
    print(message.upper() if args.shout else message)
