
import os
from datetime import date
import requests
from bs4 import BeautifulSoup
import draw
import write_lists
import load_lists

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
    # Get the price
    price = price.text.split(" ")[1].replace(",", ".")
    
    # Get the query date
    date = date.today().strftime("%d.%m.%Y")
    
    # Get the title for the diagram
    title = soup.find("title")
    title = title.text
    
    # Check for first entry
    if os.path.exists("PriceHistory.txt"):
        # Load lists from file
        prices, data = load_lists.load_lists()
        # Add price and date to the lists
        prices.append(price)
        data.append(date)
        # Write lists to file
        write_lists.write_lists(prices, data)
    else:
        # Add price and date to the lists
        prices.append(price)
        data.append(date)
        # Write lists to file
        write_lists.write_lists(prices, data)
else:
    print("Price not found")
    exit()

draw.draw_diagram(list(map(float,prices)), data, title)
