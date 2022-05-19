#!/usr/bin/python3
"""This module get data from an API"""
import requests
from sys import argv


if __name__ == "__main__":
    userId = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId))

    employee = user.json().get('name')
    completed = 0
    totalTask = 0

    todo = requests.get('https://jsonplaceholder.typicode.com/todos')

    for do in todo.json():
        if do.get('userId') == int(userId):
            totalTask += 1
            if do.get('completed'):
                completed += 1
    print('Employee {} is done with tasks({}/{}):'.format(employee, completed,
                                                          totalTask))
    for title in todo.json():
        if title.get('userId') == int(userId):
            if title.get('completed'):
                print('\t {}'.format(title.get('title')))
