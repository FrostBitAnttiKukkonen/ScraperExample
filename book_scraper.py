import requests
from selectolax.lexbor import LexborHTMLParser

response = requests.get(
    "http://localhost:8000/books.html"
)

tree = LexborHTMLParser(response.text)

for book in tree.css(".book"):

    title = book.css_first(".title").text()
    price = book.css_first(".price").text()

    print(title, "-", price)