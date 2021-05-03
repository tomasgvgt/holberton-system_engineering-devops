#!/usr/bin/python3
"""
 Python script that, using this REST API, for a given employee ID
 returns information about his/her todo list progress.
Requirements:
    The script must accept an integer as a parameter, which is the employee ID
    The script must export data in JSON format
"""
import csv
import json
import requests
import sys

if __name__ == "__main__":
    r_users = requests.get('https://jsonplaceholder.typicode.com/users')
    r_todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    employee_id = int(sys.argv[1])
    task_status = ""
    dictionary = {}
    data = []
    filename = sys.argv[1] + ".json"
    for employee in r_users.json():
        if employee["id"] == employee_id:
            employee_username = employee["username"]
    for task in r_todos.json():
        if task["userId"] == employee_id:
            task_status = task["completed"]
            task_name = task["title"]
            row = {
                "task": task_name, "completed": task_status,
                "username": employee_username}
            data.append(row)
    dictionary[str(employee_id)] = data
    with open(filename, 'w') as json_file:
        json.dump(dictionary, json_file)
