#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list containing the titles of all hot articles
    for a given subreddit
    """

    # check argument
    if not subreddit or not isinstance(subreddit, str):
        return 0

    endpoint = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # reddit API requires a User-Agent header
    headers = {"User-Agent": "Mozilla/5.0"}

    # parameters to the request
    params = {"after": after}

    try:
        # call API and get data
        response = requests.get(
            endpoint, headers=headers, params=params, allow_redirects=False
        )
        # add post titles to list
        posts = response.json().get("data").get("children")
        if posts:
            for post in posts:
                hot_list.append(post.get("data").get("title"))

        # check if there are any other posts after
        after = response.json().get("data").get("after")
        if after:
            # call recursive function again to continue fetching next posts
            return recurse(subreddit, hot_list, after)
        else:  # end reached
            return hot_list
    except Exception:
        return None
