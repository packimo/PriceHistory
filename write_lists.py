
# Write lists to file   
def write_lists(prices, data):
    prices_str = "prices = " + ", ".join(prices) + "\n"
    data_str = "data = " + ", ".join(data) + "\n"
    
    with open("PriceHistory.txt", "w") as file:
        file.write(prices_str)
        file.write(data_str)
