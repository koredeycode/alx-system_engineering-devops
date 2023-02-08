#!/usr/bin/python3
"""Gather data from a API"""

import json
import requests
import sys


def main():
    url = 'https://jsonplaceholder.typicode.com/'
    userId = sys.argv[1]

    with requests.get(url + "users/{}".format(userId)) as response:
        user = response.json()

    with requests.get(url + "todos", params={"userId": userId}) as response:
        toDos = response.json()
        objs = {userId: []}
        name = user.get("name")
        for toDo in toDos:
            obj = {
                    "task": toDo.get("title"),
                    "completed": toDo.get("completed"),
                    "username": name
                    }
            objs.get(userId).append(obj)
        with open(userId + ".json", "w") as f:
            json.dump(objs, f)


if __name__ == "__main__":
    main()
