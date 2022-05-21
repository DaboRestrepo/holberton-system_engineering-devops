#!/usr/bin/python3
"""Query in Reddit API and return the total of subscribers to a sudreddit"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """Function that query for the subreddit subscribers:
    subreddit: command line variable."""
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    r = requests.get(url).json()
    try:
        return r['data']['subscribers']
    except Exception:
        return 0
