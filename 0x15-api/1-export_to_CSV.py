#!/usr/bin/python3
""" Use task 0, extend your Python script to export data in the CSV format."""


import csv
import requests
import sys


if __name__ == '__main__':
    ID = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/users/"
    api_url = api_url + ID
    response = requests.get(api_url)
    json = response.json()
    USER_NAME = json['username']
    api_url = "https://jsonplaceholder.typicode.com/todos/"
    response = requests.get(api_url, params={"userId": ID})
    json = response.json()
    FILE_NAME = ID + "." + "csv"
    with open(FILE_NAME, 'w', newline='') as csvfile:
        w = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for TASK in json:
            input_value = [[ID, USER_NAME, TASK['completed'], TASK['title']]]
            w.writerows(input_value)
