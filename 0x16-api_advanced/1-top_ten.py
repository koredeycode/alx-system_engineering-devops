#!/usr/bin/python3
"""
print hot posts of a subreddit
"""
import requests


def top_ten(subreddit):
    """Print titlee of 10 hottest posts of a subreddit"""
    url = "https://reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent":
               "linux:0x16.api.advanced:v1.0.0 (by /u/koredeycode)"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=True)
    """ response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)"""
    if response.status_code == 404:
        return None
    data = response.json().get("data")
    [print(child.get("data").get("title")) for child in data.get("children")]
