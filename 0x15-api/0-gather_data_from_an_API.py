#!/usr/bin/python3
""" a Python script that, using this REST API, for a given employee ID,\
        returns information about his/her TODO list progress."""


import sys
import requests


if __name__ == '__main__':
    ID = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/users/"
    api_url = api_url + ID
    response = requests.get(api_url)
    json = response.json()
    EMPLOYEE_NAME = json['name']
    api_url = "https://jsonplaceholder.typicode.com/todos/"
    response = requests.get(api_url, params={"userId": ID})
    json = response.json()
    NUMBER_OF_TASKS = len(json)
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = ""
    for TASK in json:
        if (TASK['completed']):
            TASK_TITLE = TASK_TITLE + "\t " + TASK['title'] + "\n"
            NUMBER_OF_DONE_TASKS = NUMBER_OF_DONE_TASKS + 1
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          NUMBER_OF_TASKS))
    print(TASK_TITLE, end="")
