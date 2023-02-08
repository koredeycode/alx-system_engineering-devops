#!/usr/bin/python3
"""Gather data from a API"""

import csv
import requests
import sys


def main():
    url = 'https://jsonplaceholder.typicode.com/'
    userId = sys.argv[1]

    with requests.get(url + "users/{}".format(userId)) as response:
        user = response.json()

    with requests.get(url + "todos", params={"userId": userId}) as response:
        toDos = response.json()

        with open("{}.csv".format(userId), "w") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for toDo in toDos:
                completed = toDo.get("completed")
                title = toDo.get("title")
                name = user.get("name")
                writer.writerow([userId, name, completed, title])

if __name__ == "__main__":
    main()
