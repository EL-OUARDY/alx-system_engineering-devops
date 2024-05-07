#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """get number of subscribers for a given subreddit"""

    # check argument
    if not subreddit or not isinstance(subreddit, str):
        return 0

    endpoint = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Reddit API requires a User-Agent header
    headers = {"User-Agent": "Mozilla/5.0"}

    # call API and get data
    response = requests.get(endpoint, headers=headers, allow_redirects=False)
    subscribers = response.json().get("data").get("subscribers")
    if subscribers:
        return subscribers
    return 0
