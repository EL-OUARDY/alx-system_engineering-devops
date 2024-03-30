#!/usr/bin/python3
"""Script save information about employee TODO list progress
in the JSON format"""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    endpoint = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    # get user name
    employee_name = requests.get(endpoint).json().get("name")

    # get employee todos
    endpoint += "/todos"
    todos = requests.get(endpoint).json()

    # prepare our dictionary
    dictionary = {employee_id: []}
    for todo in todos:
        dictionary[employee_id].append(
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": employee_name,
            }
        )

    filename = f"{employee_id}.json"
    with open(filename, "w") as file:
        json.dump(dictionary, filename)
