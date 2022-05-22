#!/usr/bin/python3
"""This module soport the recurse function."""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Return a list with the title of all the hot articles:
    Subreddit: Topis.
    hot_list: list to be returned."""
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    params = {'after': after}
    headers = {'User-Agent': 'Dabo'}
    r = requests.get(url, headers=headers, allow_redirects=False,
                     params=params)
    if r.status_code == 404:
        return None
    try:
        r = r.json()
        posts = r['data']['children']
        hot_list.append(post['data']['title'] for post in posts)
        after = r['data']['after']
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    except Exception:
        print(None)
