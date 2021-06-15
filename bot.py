import smtplib
import imaplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import decode_header
import ssl
import json
from datetime import datetime
import time

config_file = open("config.json")
config = json.load(config_file)

waiting = True
timeout = 5

while waiting:
    # Get the timestamp
    now = datetime.now()
    timestamp = datetime.timestamp(now)

    #Compose the email
    html_code = "<h1>Es hora de fichar</h1>"
    context = ssl.create_default_context()
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Es hora de fichar " + str(timestamp)
    msg['From'] = config["sender"]
    msg['To'] = config["receiver"]
    msg.attach(MIMEText(html_code, 'html'))

    # Send the email
    with smtplib.SMTP(config["smtp_server"], config["smtp_port"]) as server:
        server.starttls(context=context)
        server.login(config["sender"], config["password"])
        server.sendmail(config["sender"], config["receiver"], msg.as_string())

    # Check the inbox for responses
    for check in range(1, int(config["resend_timeout"]/10)):
        # Login
        imap = imaplib.IMAP4_SSL(config["imap_server"])
        imap.login(config["sender"], config["password"])

        # Get the count of messages
        status, total_messages = imap.select("INBOX")
        total_messages = int(total_messages[0])

        # Verify the latest emails
        for message_id in range(total_messages, total_messages-5, -1):
            res, message = imap.fetch(str(message_id), "(RFC822)")
            for response in message:
                if isinstance(response, tuple):
                    message = email.message_from_bytes(response[1])
                    subject, encoding = decode_header(message["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding)
                    if str(timestamp) in subject:
                        waiting = False
        time.sleep(10)
    timeout -= 1
    if timeout == 0:
        waiting = False

# Logout
imap.close()
imap.logout()