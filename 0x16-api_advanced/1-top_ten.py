#!/usr/bin/python3
'''implements queries to the reddit API.'''

import requests


def top_ten(subreddit):
    '''prints the titles of the first 10 hot posts listed for a given
       subreddit.
    '''
    base_url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0"}
    params = {"limit": 10}
    r = requests.get(base_url, headers=headers, params=params,
                     allow_redirects=False)
    if r.status_code == 404:
        print("None")
        return
    result = r.json().get("data")
    [print(c.get("data").get("title")) for c in result.get("children")]
