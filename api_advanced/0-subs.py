#!/usr/bin/python3
"""
Module contains function number_of_subscribers
that queries the Reddit API and returns the
number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns number of subscribers for a subreddit
    or 0 if invalid.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "ALU-Student-API-Advanced-Task0/1.0"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            timeout=5
        )
    except Exception:
        return 0

    if response.status_code != 200:
        return 0

    data = response.json().get("data", {})
    return data.get("subscribers", 0)

