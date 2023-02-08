#!/usr/bin/python3
"""Gather data from a API"""

import json
import requests
import sys


def main():
    url1 = 'https://jsonplaceholder.typicode.com/users'
    url2 = 'https://jsonplaceholder.typicode.com/todos'
    userId = int(sys.argv[1])

    with requests.get(url1) as response:
        users = response.json()
        for user in users:
            if user.get("id") == userId:
                employee = user.get("name")
                break

    with requests.get(url2) as response:
        toDos = response.json()
        userToDos = [toDo for toDo in toDos if toDo.get("userId") == userId]
        userId = str(userId)
        objs = {userId: []}
        for userToDo in userToDos:
            obj = {
                    "task": userToDo.get("title"),
                    "completed": userToDo.get("completed"),
                    "username": employee
                    }
            objs.get(userId).append(obj)

        with open(userId + ".json", "w") as f:
            json.dump(objs, f)


if __name__ == "__main__":
    main()
