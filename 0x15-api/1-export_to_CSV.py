#!/usr/bin/env python3
"""
 Python script that, using this REST API, for a given employee ID
 returns information about his/her todo list progress.
Requirements:
    The script must accept an integer as a parameter, which is the employee ID
    The script to export data in the CSV format
"""
import sys
import requests
import json
import csv

if __name__ == "__main__":
    r_users = requests.get('https://jsonplaceholder.typicode.com/users')
    r_todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    employee_id = int(sys.argv[1])
    task_status = ""
    data = []
    filename = sys.argv[1] + ".csv"
    for employee in r_users.json():
        if employee["id"] == employee_id:
            employee_username = employee["username"]
    for task in r_todos.json():
        if task["userId"] == employee_id:
            if task["completed"] is True:
                task_status = "True"
            else:
                task_status = "False"
            task_name = task["title"]
            row = [employee_id, employee_username, task_status, task_name]
            data.append(row)
    with open(filename, 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        writer.writerows(data)
