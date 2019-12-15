# coding: utf-8
from slackbot.bot import respond_to
from slackbot.bot import default_reply


@default_reply()
def default_func(message):
    text = message.body["text"]
    res = '"' + text + '" とは？'
    message.reply(res)

@respond_to("asdf")
def reply_test(message):
    message.reply("起動中")

# LAUNCH SV
launch_sv_msg = """+hε 9α+ε vv;11 0pεη! ♪u$+ α rn0rnηε+...
d0 rn￥ vε$+ & d0 ￥0uγ vε4+ == [ vv;η ]"""

@respond_to("^LAUNCH SV$")
def reply_echip_start(message):
    message.reply(launch_sv_msg)

