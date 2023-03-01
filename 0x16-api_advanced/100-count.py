#!/usr/bin/python3
"""
print hot posts of a subreddit
"""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """return a list containing the titles of all hot articles"""
    url = "https://reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent":
               "linux:0x16.api.advanced:v1.0.0 (by /u/koredeycode)"}
    params = {"limit": 100, "after": after, "count": count}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=True)
    if response.status_code == 404:
        print()
        return None
    data = response.json().get("data")
    after += data.get("after")
    count += data.get("dist")
    for child in data.get("children"):
        title = child.get("data").get("title").lower().split()
        for word in word_list:
            times = title.count(word.lower())
            if times:
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is not None:
        if len(instances) == 0:
            print()
            return None
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
