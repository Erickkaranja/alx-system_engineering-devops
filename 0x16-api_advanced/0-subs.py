#!/usr/bin/python3

'''query the reditt api and returns the number of subscribers for a given
   subreddit.
'''
import requests


def number_of_subscribers(subreddit):
    '''queries a subreddit if a valid subreddit, return the number of
       subscribers else None
    '''
    base_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0"}
    r = requests.get(base_url, headers=headers, allow_redirects=False)
    if r.status_code == 404:
        return 0
    result = r.json().get("data")
    return result.get("subscribers")
