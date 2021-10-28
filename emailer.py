import smtplib, ssl, os
from dotenv import load_dotenv

load_dotenv(".env")

port = os.getenv("SMTP_PORT")
smtp_server = os.getenv("SMTP_SERVER")
sender_email = os.getenv("SENDER_EMAIL")
password = os.getenv("SMTP_PASSWORD")


receiver_email = "dbdayta@up.edu.ph"
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)