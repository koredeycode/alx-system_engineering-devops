#!/usr/bin/python3
"""
Queries the reddit api
"""
import requests

def number_of_subscribers(subreddit):
    """returns number of subscriber for a subreddit"""
    url = "https://reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent" : "linux:0x16.api.advanced:v1.0.0 (by /u/koredeycode)"}
    #response = requests.get(url, headers=headers, allow_redirects=False)
    response = requests.get(url, headers=headers, allow_redirects=True)
    if response.status_code != 200:
        return 0
    data = response.json().get("data")
    return data.get("subscribers") if data.get("subscribers") else 0
