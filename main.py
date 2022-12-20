from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import sys


def main():
    # product url
    url = "https://www.amazon.com/gp/goldbox?ref_=nav_cs_gb"

    # Create webdriver and go to the top url
    driver = webdriver.Chrome()
    driver.get(url)

    # Get current page from webdriver
    content = driver.page_source.encode('utf-8').strip()

    # Create BeautifulSoup class with that page
    soup = BeautifulSoup(content, "html.parser")

    # Get all discounted item name and price in the page
    item_names = soup.find_all('div', attrs={'data-id': 'TileTitle'})
    item_prices = soup.find_all('div', attrs={'data-id': 'DealPrice'})

    date = datetime.today().strftime("%Y_%m_%d")

    # Field names for the csv file
    field_names = ["name", "price"]

    # Open a new csv file
    with open(f"Amazon_deals_{date}.csv", "w", encoding="UTF8") as csv_file:
        # Add csv file and field names to the dict writer
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        # Write header to the csv file
        writer.writeheader()

        # loop through 2 list at once using zip
        for name, price in zip(item_names, item_prices):
            # Create a dict row with key and value using item name and item price
            row = {"name": name.text, "price": price.text}

            # Write to the csv file
            writer.writerow(row)

    # Show complete message and exit with exitcode 0
    print(f"Data written to Amazon_deals_{date}.csv")
    sys.exit(0)


main()
