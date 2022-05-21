#!/usr/bin/python3
"""This module soport the top_ten function"""
import requests


def top_ten(subreddit):
    """This function prints the first 10 titles of a given subreddit.
    subreddit: command line value."""
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    r = requests.get(url, headers={'User-Agent': 'Dabo'}).json()
    try:
        count = 0
        for post in r['data']['children']:
            if count < 10:
                print(post['data']['title'])
                count += 1
    except Exception:
        print(None)
