import smtplib, ssl, os
from dotenv import load_dotenv

load_dotenv(".env")

port = os.getenv("SMTP_PORT")
smtp_server = os.getenv("SMTP_SERVER")
sender_email = os.getenv("SENDER_EMAIL")
password = os.getenv("SMTP_PASSWORD")


receiver_email = "your@gmail.com"
message = """\
Subject: Hi there

This message is sent from Python."""

print(port)
print(smtp_server)
print(password)
print(sender_email)