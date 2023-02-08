#!/usr/bin/python3
"""Gather data from a API"""

import requests
import sys


def main():
    url = 'https://jsonplaceholder.typicode.com/'
    userId = sys.argv[1]

    with requests.get(url + "users/{}".format(userId)) as response:
        user = response.json()

    with requests.get(url + "todos", params={"userId": userId}) as response:
        toDos = response.json()
        total = len(toDos)
        toDosDone = [toDo.get("title") for toDo in toDos
                     if toDo.get("completed") is True]
        done = len(toDosDone)

        tstr = "\n\t ".join(toDosDone)
        out = "Employee {} is done with tasks({}/{}):\n\t {}".\
              format(user.get("name"), done, total, tstr)
        print(out)


if __name__ == "__main__":
    main()
