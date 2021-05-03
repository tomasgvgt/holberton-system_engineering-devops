#!/usr/bin/python3
"""
 Python script that, using this REST API, for all employees
 returns information todo list progress.
Requirements:
    The script must export data in JSON format
"""
import csv
import json
import requests
import sys

if __name__ == "__main__":
    r_users = requests.get('https://jsonplaceholder.typicode.com/users')
    r_todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    task_status = ""
    dictionary = {}
    filename = "todo_all_employees.json"
    for employee in r_users.json():
        employee_id = employee["id"]
        employee_username = employee["username"]
        data = []
        for task in r_todos.json():
            if task["userId"] == employee_id:
                task_status = task["completed"]
                task_name = task["title"]
                row = {
                    "username": employee_username,
                    "task": task_name, "completed": task_status}
                data.append(row)
        dictionary[str(employee_id)] = data
    with open(filename, 'w') as json_file:
        json.dump(dictionary, json_file)
