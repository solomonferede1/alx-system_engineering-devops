#!/usr/bin/python3
"""
Module to query Reddit API for subscriber count of a subreddit.
If an invalid subreddit is given, the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API.
    - If not a valid subreddit, return 0.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'custom'}

    # Make the GET request to the Reddit API
    req = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the status code is OK (200)
    if req.status_code == 200:
        # Directly return the number of subscribers
        return req.json()['data']['subscribers']
    
    # Return 0 for invalid subreddit
    return 0

