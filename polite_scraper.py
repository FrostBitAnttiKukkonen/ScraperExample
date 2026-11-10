import requests
import time
from selectolax.lexbor import LexborHTMLParser

URL = "http://localhost:8000"

headers = {
    "User-Agent": "LUASNetworkingCourse/1.0"
}

response = requests.get(
    URL,
    headers=headers
)

tree = LexborHTMLParser(response.text) # Whole structure

title = tree.css_first("title") # Using website's sections

if title:
    print("Title:", title.text())

print("Waiting 2 seconds...")
time.sleep(2)