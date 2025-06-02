
from datetime import date
import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
import numpy as np

# This list holds the price from the query
prices = []
# This list holds the date from the query
data = []

# Title for the diagram
title = ""

# URL to the product from which the price should be extracted
url = "https://www.alternate.de/Intel/Core-Ultra-7-265K-Prozessor/html/product/100077064"

# Make the request appear as if it is coming from a real web browser
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find the element where the price is stored
price = soup.find("span", class_="price")

# Check if we found the price
if price is not None:
    price = price.text
    price = float(price[2:].replace(",", "."))
    print(f"Price: {price:.2f}")
    
    # Get the query date
    date = date.today().strftime("%d.%m.%Y")
    print(f"Query date: {date}")
    
    # Get the title for the diagram
    title = soup.find("title")
    title = title.text
    print(f"Title for diagram: {title}")
    
    # Add price and date to the lists
    prices.append(price)
    data.append(date)
else:
    print("Price not found")
    exit()

# Plot diagram here
plt.xlabel("Date of query")
plt.ylabel("Price in €")
plt.title(title)
plt.ylim(min(prices) - 5, max(prices) + 5)
plt.yticks(np.arange(min(prices) - 5, max(prices) + 5, 5))
plt.plot(data, prices, "bo-")
plt.show()
