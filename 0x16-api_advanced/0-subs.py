#!/usr/bin/python3
"""
If an invalid subreddit is given, the function should return 0
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    user_agent = "0-subs (Python; Ubuntu 20.04; Contact: ezezsolomonferede@gmail.com)"
    headers = {'User-Agent': user_agent}
    try:
        req = requests.get(url, headers=headers, allow_redirects=False)
        if req.status_code == 200:
            return req.json()['data']['subscribers']
        else:
            return 0
    except requests.RequestsException:
        return 0
