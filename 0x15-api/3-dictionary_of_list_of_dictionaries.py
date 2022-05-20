#!/usr/bin/python3
"""This module export all the employee data in json format"""
import json
import requests


if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users/').json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    total_usr = {}
    for usr in user:
        id_list = []
        for do in todo:
            if do.get('userId') == usr.get('id'):
                task_dict = {"username": usr.get('username'),
                             "task": do.get('title'),
                             "completed": do.get('completed')}
                id_list.append(task_dict)
        total_usr[usr.get('id')] = id_list

    file = 'todo_all_employees.json'
    with open(file, mode='w') as f:
        json.dump(total_usr, f)
