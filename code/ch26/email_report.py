# Build an email with an attachment, and send it only when asked to.
# The SMTP server and password come from environment variables,
# never from the code.
import argparse
import os
import smtplib
from email.message import EmailMessage
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument(
    "--send", action="store_true", help="really send (default: only show)"
)
args = parser.parse_args()

message = EmailMessage()
message["From"] = "reports@pocket-library.example"
message["To"] = "reader@pocket-library.example"
message["Subject"] = "Your reading log"
message.set_content(
    "Hello,\n\nYour reading log is attached.\n\nPocket Library\n"
)
message.add_attachment(
    Path("reading_log.csv").read_bytes(),
    maintype="text",
    subtype="csv",
    filename="reading_log.csv",
)

if args.send:
    host = os.environ["SMTP_HOST"]  # for example smtp.your-provider.example
    user = os.environ["SMTP_USER"]
    password = os.environ["SMTP_PASSWORD"]
    with smtplib.SMTP(host, 587, timeout=30) as server:
        server.starttls()  # encrypt before logging in
        server.login(user, password)
        server.send_message(message)
    print("Sent.")
else:
    print("Not sent (add --send). The message would be:")
    for header in ("From", "To", "Subject"):
        print(f"  {header}: {message[header]}")
    for part in message.iter_parts():
        kind = "attachment" if part.is_attachment() else "body"
        size = len(part.get_content())
        print(
            f"  part: {part.get_content_type()}, {size} characters, {kind}"
        )
    print(
        "  attachment name:",
        next(message.iter_attachments()).get_filename(),
    )
