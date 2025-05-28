
import requests
from bs4 import BeautifulSoup

# URL to the product from which the price should be extracted
url = "https://www.alternate.de/Intel/Core-Ultra-7-265K-Prozessor/html/product/100077064"

# Make the request appear as if it is coming from a real web browser
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

price = soup.find("span", class_="price")
price = price.text

if price:
    print(f"Price: {price}")
else:
    print("Price not found")
