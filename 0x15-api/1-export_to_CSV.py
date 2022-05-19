#!/usr/bin/python3
"""This csv exports a request response."""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    userId = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId))
    todo = requests.get('https://jsonplaceholder.typicode.com/todos')

    employee = user.json().get('username')

    file = userId + '.csv'
    with open(file, mode='w') as fd:
        csv_file = csv.writer(fd, quoting=csv.QUOTE_ALL)
        for elem in todo.json():
            if elem.get('userId') == int(userId):
                csv_file.writerow([userId, employee,
                                  elem.get('completed'), elem.get('title')])
