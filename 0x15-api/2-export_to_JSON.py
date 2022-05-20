#!/usr/bin/python3
"""This csv exports a request response."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    userId = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId))
    todo = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    name = user.json().get('username')
    do_dict = {}
    list = []

    for elem in todo:
        if elem.get('userId') == int(userId):
            info_task = {"task": elem.get('title'),
                         "completed": elem.get('completed'),
                         "username": name}
            list.append(info_task)
    do_dict[userId] = list
    file = userId + '.json'
    with open(file, mode='w') as f:
        json.dump(do_dict, f)
