#!/usr/bin/python3
"""
print hot posts of a subreddit
"""
import requests

def recurse(subreddit, hot_list=[]):
    """return a list containing the titles of all hot articles"""
    url = "https://reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent" : "linux:0x16.api.advanced:v1.0.0 (by /u/koredeycode)"}
    params = {"limit": 100}
    response = requests.get(url, headers=headers, params=params, allow_redirects=True)
    #response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    data = response.json().get("data")
    [print(child.get("data").get("title")) for child in data.get("children")]
