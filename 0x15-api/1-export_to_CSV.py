#!/usr/bin/python3
"""Gather data from a API"""

import csv
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

    with open("{}.csv".format(userId), "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for userTodo in userToDos:
            completed = userTodo.get("completed")
            title = userTodo.get("title")
            writer.writerow([userId, employee, completed, title])


if __name__ == "__main__":
    main()
