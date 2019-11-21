# coding: utf-8
"""
githubのコード検索結果取得
"""
import urllib.request
import html
import re

GITHUB_URL = "https://github.com/"

RESULT_MARK = "bg-yellow-light"
RE_TAG = re.compile(r"<[^>]*?>")
RE_FILENAME = re.compile(r'title="([^"]+)"')
RE_LINENUM = re.compile(r'#L([0-9]+)')


def _valid_repo(repo):
    tokens = repo.split("/")
    user = urllib.parse.quote(tokens[0])
    if len(user) == 0:
        return False
    reponame = urllib.parse.quote(tokens[1])
    if len(reponame) == 0:
        return False
    return f"{user}/{reponame}" == repo

def _get_res(repo, word):
    if not _valid_repo(repo):
        # bad repository name
        return None
    params = urllib.parse.urlencode({"q":word})
    # https://github.com/ユーザ名/リポジトリ名/search?q=検索する単語
    url = f"{GITHUB_URL}{repo}/search?{params}"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        body = res.read()
    return body.decode("utf-8")

def _get_filename(line):
    m = RE_FILENAME.search(line)
    if m is None:
        return None
    fname = m.group(1)
    return html.unescape(fname)

def _get_linenum(line):
    m = RE_LINENUM.search(line)
    if m is None:
        return None
    num = m.group(1)
    return html.unescape(num)

def _is_result_line(line):
    return RESULT_MARK in line

def _get_plain(str):
    notag = RE_TAG.sub("", str)
    return html.unescape(notag)

def _get_results(res_body):
    results = []
    last_filename = ""
    last_linenum = ""
    lines = res_body.split("\n")
    for line in lines:
        line = line.strip()
        fname = _get_filename(line)
        if fname is not None:
            last_filename = fname
            continue
        num = _get_linenum(line)
        if num is not None:
            last_linenum = num
            continue
        if not _is_result_line(line):
            continue
        pos = f"{last_filename} +{last_linenum}"
        results.append([pos, _get_plain(line)])
    return results

def _search_github(repo, word):
    res = _get_res(repo, word)
    if res is None:
        return []
    return _get_results(res)

def get_msg(repo, word):
    results = _search_github(repo, word)
    msg = f'{repo} の"{word}"は'
    results_num = len(results)
    if results_num == 0:
        msg += "検索失敗しました"
    else:
        msg += f"{results_num}件見つかりました\n\n"
        for ret in results:
            pos = ret[0]
            line = ret[1]
            msg += f"{pos}\n`{line}`\n\n"
    return msg

