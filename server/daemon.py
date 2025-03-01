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
MESSAGE_GRACE_TIME = ""

TZ_INFO = None


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
            messages.append({
        "id": mssg.uid,
                "timestamp": mssg.date,
                "message": mssg.subject,
            })

    return messages


def remove_old(messages, grace_period: int) -> [Dict[str, str | datetime.datetime]]:
    """
    remove old messages based on given grace period (in s)
    """
    timely_messages = []

    now = datetime.datetime.now(TZ_INFO)

    # iterate over messages
    for mssg in messages:
        # get time diff between now and message time
        messagetime = mssg['timestamp']

        if not isinstance(messagetime, datetime.datetime):
            messagetime = datetime.datetime.fromisoformat(messagetime)
            mssg['timestamp'] = messagetime
        
        print(messagetime)
        deltatime = now - messagetime
        deltatime = deltatime.seconds

        # only pass on messages that have a lower dt than the grace_period
        if deltatime < grace_period:
            timely_messages.append(mssg)
        else:
            print("I: removing message %s" % mssg['id'])

    return timely_messages


def write_data(messages):
    """
    write message data to JSON file
    """
    for mssg in messages:
        mssg['timestamp'] = mssg['timestamp'].isoformat()

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(messages, f)


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
    global MESSAGE_GRACE_TIME

    DOMAIN = os.getenv('DOMAIN')
    EMAIL_ADRESS = os.getenv('EMAIL_ADRESS')
    PASSWD = os.getenv('PASSWD')
    MESSAGE_GRACE_TIME = int(os.getenv('MESSAGE_GRACE_TIME'))

    print("MESSAGE_GRACE_TIME: %d" % MESSAGE_GRACE_TIME)

    # get timezone info
    global TZ_INFO
    now = datetime.datetime.now()  # current datetime
    TZ_INFO = now.astimezone().tzinfo

    messages = []

    print("I: starting event loop...")

    # event loop
    while True:
        messages += get_new_messages()  # append new messages
        messages = remove_old(messages, MESSAGE_GRACE_TIME)  # remove old messages

        print(messages)

        write_data(messages)  # write data to JSON

        time.sleep(5)


if __name__ == "__main__":
    main()
