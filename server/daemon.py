"""
daemon.py
"""
# import imaplib
# import email
from typing import Dict
import time
import datetime
import os
import dotenv
from imap_tools import MailBox, AND
import json

DOMAIN = ""
EMAIL_ADRESS = ""
PASSWD = ""


def get_new_messages() -> [Dict[str, str | datetime.datetime]]:
    """
    parse unread messages to message list
    """
    messages = []
    # Connect to the mailbox
    # MOVE SECTION TO main() TO AVOID CONSTANTLY LOGGING IN
    with MailBox(DOMAIN).login(EMAIL_ADRESS, PASSWD) as mailbox:
        # Fetch emails
        for mssg in mailbox.fetch(AND(seen=False)):
            subject = mssg.subject
            print(mssg.uid)
            print(mssg.date)
            print(subject)

            messages.append({
                "id": mssg.uid,
                "timestamp": mssg.date,
                "message": mssg.subject,
            })

    return messages


def remove_old(messages, grace_period: int):
    """
    remove old messages based on given grace period (in s)
    """
    for mssg in messages:
        ...


def main():
    """
    driver code
    """
    print("I: STARTING DAEMON...")
    dotenv.load_dotenv()  # load env vars

    # get login data
    global DOMAIN
    global EMAIL_ADRESS
    global PASSWD

    # set env vars
    DOMAIN = os.getenv('DOMAIN')
    EMAIL_ADRESS = os.getenv('EMAIL_ADRESS')
    PASSWD = os.getenv('PASSWD')

    messages = []

    print("I: starting event loop...")

    # event loop
    while True:
        # messages += get_new_messages()  # append new messages
        # remove_old(messages, 60*5)  # remove old messages
        messages = [
            {
                "id": "123",
                "timestamp": "2025-02-28...",
                "message": "Hello",
            },
            {
                "id": "124",
                "timestamp": "2025-02-28...",
                "message": "Hello again",
            },
        ]

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(messages, f)

        time.sleep(10)


if __name__ == "__main__":
    main()
