# coding: utf-8
import os

from slackbot.bot import listen_to
import plugins.send_line


LINE_NOTIFY_TOKEN = os.environ["PUA_TOKEN_LINE_NOTIFY"]


def get_username(message):
    return message.channel._client.users[message.body["user"]]["real_name"]

@listen_to("^line\n")
def reply_test(message):
    text = message.body["text"]
    username = get_username(message)
    line_msg = f" from {username}\n{text}"
    status = plugins.send_line.send_line(line_msg, LINE_NOTIFY_TOKEN)
    message.send(f"status: {status}")

