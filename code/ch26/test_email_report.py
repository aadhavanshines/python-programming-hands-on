# Test the --send branch of email_report.py without a real mail server:
# monkeypatch swaps smtplib.SMTP for a fake that records what it's asked.
import runpy
import smtplib
import sys


class FakeSMTP:
    instances = []

    def __init__(self, host, port, timeout):
        self.calls = [("connect", host, port)]
        FakeSMTP.instances.append(self)

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def starttls(self):
        self.calls.append(("starttls",))

    def login(self, user, password):
        self.calls.append(("login", user))

    def send_message(self, message):
        self.calls.append(("send", message["To"]))


def test_send(monkeypatch, capsys):
    monkeypatch.setattr(smtplib, "SMTP", FakeSMTP)
    monkeypatch.setattr(sys, "argv", ["email_report.py", "--send"])
    monkeypatch.setenv("SMTP_HOST", "smtp.example")
    monkeypatch.setenv("SMTP_USER", "reports")
    monkeypatch.setenv("SMTP_PASSWORD", "not-a-real-password")
    runpy.run_path("email_report.py")
    assert FakeSMTP.instances[-1].calls == [
        ("connect", "smtp.example", 587),
        ("starttls",),  # encrypted before the password is sent
        ("login", "reports"),
        ("send", "reader@pocket-library.example"),
    ]
    assert capsys.readouterr().out == "Sent.\n"
