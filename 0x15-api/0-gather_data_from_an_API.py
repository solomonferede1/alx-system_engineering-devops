#!/usr/bin/python3
'''Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.'''

import sys
import requests


def todo_list_completed(employee_id):
    url_user = "https://jsonplaceholder.typicode.com/users/"
    url_todo = "https://jsonplaceholder.typicode.com/todos/"

    parms = {'id': employee_id}
    user_data = requests.get(url_user, params=parms).json()
    EMPLOYEE_NAME = user_data['name']

    parms = {'userId': employee_id}
    response = requests.get(url_todo, params=parms)
    todos = response.json()

    completed = [task['title'] for task in todos if task['completed']]

    NUMBER_OF_DONE_TASKS = len(completed)
    NUMBER_OF_DONE_TASKS = len(todos)

    print(f"Employee {EMPLOYEE_NAME} is done with tasks(
                        {NUMBER_OF_DONE_TASKS}/{NUMBER_OF_DONE_TASKS}): ")
    for task in completed:
        print(f"\t {task['title']}")


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    todo_list_completed(employee_id)
