#!/usr/bin/python3
"""Gather data from a API"""

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
        tasks = len(userToDos)
        userToDosDone = [userToDo.get("title") for userToDo in userToDos
                         if userToDo.get("completed") is True]
        tasksDone = len(userToDosDone)

        tstr = "\n\t ".join(userToDosDone)
        out = "Employee {} is done with tasks({}/{}):\n\t {}".format(employee,
                                                                     tasksDone,
                                                                     tasks,
                                                                     tstr)
        print(out)


if __name__ == "__main__":
    main()
