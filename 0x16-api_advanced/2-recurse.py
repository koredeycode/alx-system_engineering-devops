#!/usr/bin/python3
"""
print hot posts of a subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """return a list containing the titles of all hot articles"""
    url = "https://reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent":
               "linux:0x16.api.advanced:v1.0.0 (by /u/koredeycode)"}
    params = {"limit": 100, "after": after, "count": count}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=True)
    if response.status_code == 404:
        return None
    data = response.json().get("data")
    after += data.get("after")
    count += data.get("dist")
    for child in data.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
