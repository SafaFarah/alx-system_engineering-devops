#!/usr/bin/python3
""" a module queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """a function queries  Reddit API and returns the number of subscribers """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'CustomClient/1.0'}
    results = requests.get(url, headers=headers, allow_redirects=False)
    if results.status_code == 200:
        data = results.json()
        return data['data']['subscribers']
    else:
        return 0
