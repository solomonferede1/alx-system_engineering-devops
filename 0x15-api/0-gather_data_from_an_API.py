#!/usr/bin/python3
'''Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.'''

import requests
import sys


def todo_list_completed(employee_id):
    '''List completed tasks'''
    url_user = "https://jsonplaceholder.typicode.com/users/"
    url_todo = "https://jsonplaceholder.typicode.com/todos/"

    parms = {'id': employee_id}
    response = requests.get(url_user, params=parms).json()
    for i in response:
        if i['id'] == employee_id:
            EMPLOYEE_NAME = i['name']

    parms = {'userId': employee_id}
    response = requests.get(url_todo, params=parms).json()

    completed = []
    for todos in response:
        if todos['completed']:
            completed.append(todos['title'])

    NUMBER_OF_DONE_TASKS = len(completed)
    TOTAL_NUMBER_OF_TASKS = len(response)

    print(f"Employee {EMPLOYEE_NAME} is done with tasks(\
{NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}): ")
    for task in completed:
        print(f"\t {task}")


if __name__ == '__main__':
    '''Call if main'''
    employee_id = int(sys.argv[1])
    todo_list_completed(employee_id)
