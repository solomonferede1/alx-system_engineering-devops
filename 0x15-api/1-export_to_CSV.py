#!/usr/bin/python3
'''Python script that, for a given employee ID,
export to  CSV file'''

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
            USERNAME = i['username']

    parms = {'userId': employee_id}
    response = requests.get(url_todo, params=parms).json()

    lines = []
    file_name = f'{employee_id}.csv'
    for todos in response:
        lines.append(f'"{employee_id}", "{USERNAME}", \
"{todos["completed"]}", "{todos["title"]}"\n')
    with open(file_name, 'w') as file:
        for line in lines:
            file.write(line)


if __name__ == '__main__':
    '''Call if main'''
    employee_id = int(sys.argv[1])
    todo_list_completed(employee_id)
