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
    json = response.json()
    USER_NAME = json.get('username')
    api_url = "https://jsonplaceholder.typicode.com/todos/"
    response = requests.get(api_url, params={"userId": ID})
    json = response.json()
    FILE_NAME = ID + "." + "json"
    dictionary = {ID: []}
    for TASK in json:
        title = TASK.get('title')
        completed = TASK.get('completed')
        dictionary[ID].append({"task": title, "completed": completed,
                              "username": USER_NAME})
    with open("FILE_NAME", "w") as outfile:
        json.dump(dictionary, outfile)
