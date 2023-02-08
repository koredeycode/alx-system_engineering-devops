#!/usr/bin/python3
"""Gather data from a API"""

import json
import requests
import sys


def main():
    url1 = 'https://jsonplaceholder.typicode.com/users'
    url2 = 'https://jsonplaceholder.typicode.com/todos'

    with requests.get(url1) as response:
        data = response.json()
        users = {}
        for datum in data:
            users[str(datum.get("id"))] = datum.get("name")
    print(users)

    with requests.get(url2) as response:
        toDos = response.json()
        tasks = {}
        for toDo in toDos:
            userId = str(toDo.get("userId"))
            obj = {
                    "username": users.get(userId),
                    "task": toDo.get("title"),
                    "completed": toDo.get("completed")
                    }
            if tasks.get(userId) is None:
                tasks[userId] = [obj]
            else:
                tasks.get(userId).append(obj)

        with open("todo_all_employees.json", "w") as f:
            json.dump(tasks, f)


if __name__ == "__main__":
    main()
