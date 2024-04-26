#!/usr/bin/python3
""" Use task 0,extend your Python script to export data in the JSON format"""


import json
import requests
import sys


if __name__ == '__main__':
    ID = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/users/"
    api_url = api_url + ID
    response = requests.get(api_url)
    json_data = response.json()
    USER_NAME = json_data.get('username')
    api_url = "https://jsonplaceholder.typicode.com/todos/"
    response = requests.get(api_url, params={"userId": ID})
    json_data = response.json()
    FILE_NAME = '{}.json'.format(ID)
    list_task = []
    for TASK in json_data:
        title = TASK.get('title')
        completed = TASK.get('completed')
        list_task.append({"task": title, "completed": completed,
                         "username": USER_NAME})
    _dict = {ID: list_task}
    with open(FILE_NAME, "w") as outfile:
        json.dump(_dict, outfile)
