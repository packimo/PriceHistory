
# Load lists from file
def load_lists():
    tmp_prices = []
    tmp_data = []
    
    with open("PriceHistory.txt", "r") as file:
        tmp_prices = [price.strip() for price in file.readline().split("=")[1].split(",")]
        tmp_data = [date.strip() for date in file.readline().split("=")[1].split(",")]

    return tmp_prices, tmp_data