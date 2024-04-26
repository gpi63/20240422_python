import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

resp = requests.get("https://finance.yahoo.com/quote/MSFT", headers=headers)

# print(resp.text)

soup = BeautifulSoup(resp.text, "html.parser")

# print(soup.title.string)

# print(soup.prettify())

for element in soup.find_all("button"):
    print(element)
