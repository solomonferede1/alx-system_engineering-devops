#!/usr/bin/python3

""" Python script to export data in the JSON format."""

import json
import requests
import sys


def todo_to_json(employee_id):
    '''List completed tasks'''
    url_user = "https://jsonplaceholder.typicode.com/users/"
    url_todo = "https://jsonplaceholder.typicode.com/todos/"

    parms = {'id': employee_id}
    response = requests.get(url_user, params=parms).json()
    for i in response:
        if i['id'] == employee_id:
            USERNAME = i['username']

    parms = {'userId': employee_id}
    response = requests.get(url_todo, params=parms).json()

    todo_list = []
    for todos in response:
        todo_list.append({
            "task": todos["title"],
            "completed": todos["completed"],
            "username": USERNAME
            })
    data = {str(employee_id): todo_list}

    file_name = f'{employee_id}.json'
    with open(file_name, 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    '''Call if main'''
    employee_id = int(sys.argv[1])
    todo_to_json(employee_id)
