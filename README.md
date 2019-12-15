# Pua Slackbot
slack用のbot

## 準備
* `pip3 install slackbot`
* `export PUA_TOKEN_SLACKBOT_API=<slackbotのトークン>`
* `export PUA_TOKEN_LINE_NOTIFY=<line notifyのトークン>`

## 機能
* lineへの転送
    * 先頭行が`line`のみのメッセージの場合、lineへ転送する

## 起動
* `python3 run.py`

