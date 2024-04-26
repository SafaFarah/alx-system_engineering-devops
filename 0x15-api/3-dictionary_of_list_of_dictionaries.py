#!/usr/bin/python3
""" Use task 0,extend your Python script to export data in the JSON format"""


import json
import requests
import sys


if __name__ == '__main__':
    api_url = "https://jsonplaceholder.typicode.com/users/"
    response = requests.get(api_url)
    json_data = response.json()
    users = {}
    for user in json_data:
        ID = user.get('id')
        USER_NAME = user.get('username')
        api_url = "https://jsonplaceholder.typicode.com/todos/"
        response = requests.get(api_url, params={"userId": ID})
        json_data = response.json()
        users[ID] = []
        for TASK in json_data:
            title = TASK.get('title')
            completed = TASK.get('completed')
            users[ID].append({"username": USER_NAME,
                             "task": title, "completed": completed})
    with open('todo_all_employees.json', "w") as outfile:
        json.dump(users, outfile)
