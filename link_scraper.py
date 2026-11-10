import requests
from selectolax.lexbor import LexborHTMLParser

response = requests.get( # Just one request per run, should be safe
    "http://localhost:8000"
)

tree = LexborHTMLParser(response.text)

for node in tree.css("a"): # a means link's element
    href = node.attributes.get("href") # href is the URL

    print("Link found:", href)