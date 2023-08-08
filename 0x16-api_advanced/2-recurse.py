#!/usr/bin/python3
'''implements queries to the reddit API.'''

import requests


def recurse(subreddit, hot_list=[]):
    '''prints the titles of the first 10 hot posts listed for a given
       subreddit.
    '''
    base_url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0"}
    params = {"limit": 10, "after": after, "count": count}
    r = requests.get(base_url, headers=headers, params=params,
                     allow_redirects=False)
    if r.status_code == 404:
        return None
    result = r.json().get("data")
    after = result.get("after")
    count += result.get("dist")
    for c in result.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list=[])
    return hot_list
