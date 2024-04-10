#!/usr/bin/python3
"""
queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit
    """

    # check argument
    if not subreddit or not isinstance(subreddit, str):
        return 0

    endpoint = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # reddit API requires a User-Agent header
    headers = {"User-Agent": "Mozilla/5.0"}

    # parameters to the request
    params = {"limit": 10}

    try:
        # call API and get data
        response = requests.get(
            endpoint, headers=headers, params=params, allow_redirects=False
        )
        posts = response.json().get("data").get("children")
        if posts:
            for post in posts:
                print(post.get("data").get("title"))
    except Exception:
        pass
