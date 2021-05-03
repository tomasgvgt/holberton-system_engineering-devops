#!/usr/bin/python3
"""
 Python script that, using this REST API, for a given employee ID
 returns information about his/her todo list progress.
Requirements:
    The script must accept an integer as a parameter, which is the employee ID
    The script must display on the standard output the employee todo list
"""
import json
import requests
import sys

if __name__ == "__main__":
    if sys.argv[1].isdigit() and len(sys.argv) == 2:
        r_users = requests.get(
            'https://jsonplaceholder.typicode.com/users')
        r_todos = requests.get(
            "https://jsonplaceholder.typicode.com/todos")
        total_tasks = 0
        completed_tasks = 0
        employee_id = int(sys.argv[1])
        completed_list = []
        for employee in r_users.json():
            if employee["id"] == employee_id:
                employee_name = employee["name"]
        for task in r_todos.json():
            if task["userId"] == employee_id:
                total_tasks += 1
                if task["completed"] is True:
                    completed_tasks += 1
                    completed_list.append(task["title"])
        print("Employee {} is done with tasks({}/{}):".format(
                employee_name, completed_tasks, total_tasks))
        for t in completed_list:
            print("\t {}".format(t))
