#!/usr/bin/python3
"""
Module to fetch and display TODO list progress of an employee from REST API
and export data to CSV file
"""

import requests

import sys

import csv


def get_employee_todo_progress(employee_id):
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Invalid employee ID. Enter the correct integer.")
        return
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found")
        return
    employee_name = user_response.json().get("name")
    todos_url = (
            f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
            )
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Could not retrieve todo list.")
        return
    todos = todos_response.json()
    # Calculate progress
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    number_of_done_tasks = len(done_tasks)
    # display results
    print(
            f"Employee {employee_name} is done with tasks"

            f"({number_of_done_tasks}/{total_tasks}):"
            )
    for task in done_tasks:
        print(f"\t {task.get('title')}")


        CSV_file = f"{employee_id}.csv"
        with open(csv_fil, mode='w', newline='') as file:
          writer = csv.writer(file, quoting= csv.QUOTE_ALL)
          for task in todos:
              writer.writerow([employee_id, employee_name, task.get("completed"), task.get('title')])

              print(f"Data exported to {csv_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script_name.py EMPLOYEE_ID")
    else:
        get_employee_todo_progress(sys.argv[1])

