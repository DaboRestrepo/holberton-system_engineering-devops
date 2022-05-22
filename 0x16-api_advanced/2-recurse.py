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
    if after is None:
        return hot_list
    r = requests.get(url, headers=headers, params=params)
    if r.status_code != 200:
        return None
    r = r.json()
    posts = r['data']['children']
    hot_list.append(post['data']['title'] for post in posts)
    after = r['data']['after']
    return recurse(subreddit, hot_list, after)
