# coding: utf-8
import re

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import plugins.search_github


@default_reply()
def default_func(message):
    text = message.body["text"]
    res = '"' + text + '" とは？'
    message.reply(res)

@respond_to("asdf")
def reply_test(message):
    message.reply("起動中")


RE_REPO = re.compile(r'\$([^ /]+/[^ ]+) ')
RE_WORD = re.compile(r'%([^"]+) ')

@respond_to("[^?]+\?\?$")
def reply_question(message):
    text = message.body["text"]
    m_repo = re.search(RE_REPO, text)
    m_word = re.search(RE_WORD, text)
    if m_repo is not None:
        repo = m_repo.group(1)
        if m_word is None:
            word = "TODO"
        else:
            word = m_word.group(1)
        msg = plugins.search_github.get_msg(repo, word)
        message.reply(msg)
    else:
        message.reply("??")

