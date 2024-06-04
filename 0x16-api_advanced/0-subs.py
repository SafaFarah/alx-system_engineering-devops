#!/usr/bin/python3
""" a module queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """a function queries  Reddit API and returns the number of subscribers """
    url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'my-integration/1.2.3'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        response = response.json()
        return response.get('data').get('subscribers')
    return 0
