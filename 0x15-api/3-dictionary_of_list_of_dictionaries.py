#!/usr/bin/python3

""" Python script to export data in the JSON format."""

import json
import requests
import sys


def fetch_data():
    """Fetch data from the API and format it."""
    url_user = "https://jsonplaceholder.typicode.com/users/"
    url_todo = "https://jsonplaceholder.typicode.com/todos/"

    # Fetch all users
    users = requests.get(url_user).json()

    # Create a dictionary to hold tasks for each user
    all_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']

        # Fetch todos for the current user
        todos = requests.get(url_todo, params={'userId': user_id}).json()

        # Collect tasks
        user_tasks = []
        for todo in todos:
            user_tasks.append({
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            })
        all_tasks[str(user_id)] = user_tasks

    return all_tasks


def save_to_file(data):
    """Save the data to a JSON file."""
    file_name = 'todo_all_employees.json'
    with open(file_name, 'w') as file:
        json.dump(data, file)  # Pretty print the JSON with indent


if __name__ == '__main__':
    """Main function."""
    data = fetch_data()
    save_to_file(data)
