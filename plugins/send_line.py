#!/usr/bin/env python3
"""
Line Notify経由でlineにメッセージを送信する
"""
import argparse
import urllib.request


default_msg = "hello"
url_lineNotify = "https://notify-api.line.me/api/notify"


def send_line(msg, token):
    """
    msgをlineに送信する
    送信結果を文字列で返す
    """
    data_dict = {"message" : msg}
    data = urllib.parse.urlencode(data_dict).encode("utf-8")
    headers = {"Authorization" : f"Bearer {token}"}
    req = urllib.request.Request(url_lineNotify, data, headers)
    with urllib.request.urlopen(req) as res:
        body = res.read()
    return body.decode("utf-8")

def main():
    parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("msg", help="message", default=default_msg, nargs="?")

    args = parser.parse_args()
    send_line(args.msg)

if __name__ == "__main__":
    main()

