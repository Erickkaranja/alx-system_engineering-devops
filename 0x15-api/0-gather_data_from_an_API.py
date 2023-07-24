#!/usr/bin/python3
"""script that uses a restful api to give employee id and the employee progress
   status
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with ({}/{}):".format(
          user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
