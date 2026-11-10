# get_robots.py

import requests

site = "https://www.python.org"

robots_url = site + "/robots.txt"

response = requests.get(robots_url) # fine for single request

print(response.text)
