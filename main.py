from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import csv


def main():
    # product url
    url = "https://www.amazon.com/gp/goldbox?ref_=nav_cs_gb&deals-widget=%257B%2522version%2522%253A1%252C%2522viewIndex%2522%253A0%252C%2522presetId%2522%253A%252264049D9C1CDF5B41F83FDB7974F9054B%2522%252C%2522departments%2522%253A%255B%2522172282%2522%255D%252C%2522sorting%2522%253A%2522BY_CUSTOM_CRITERION%2522%257D"

    # Create webdriver and go to the top url
    driver = webdriver.Chrome()
    driver.minimize_window()
    driver.get(url)

    # Get current page from webdriver
    content = driver.page_source.encode('utf-8').strip()

    # Create beautifulsoup class with that page
    soup = BeautifulSoup(content, "html.parser")

    # Get all discounted in the page
    items = soup.find_all("h4", class_="a-offscreen")

    # Current date
    date = datetime.today().strftime("%Y_%m_%d")

    # Field names for the csv file
    field_names = ["name", "price"]

    # Open a new csv file
    with open(f"Amazon_deals_{date}.csv", "w", encoding="UTF8") as csv_file:
        # Add csv file and field names to the dict writer
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        # Write header to the csv file
        writer.writeheader()

        for item in items:
            # Divide text inside h4 to name and price
            item_name_tag, price_tag = item.get_text().split(";")

            # Split from 'Deal' to get name and remove whitespace
            item_name = item_name_tag.split(":")[-1].strip()

            # Split from 'Deal price' to get name and remove whitespace
            price = price_tag.split(":")[-1].strip()

            # Create a dict row with key and value and add to the csv file
            row = {"name": item_name, "price": price}

            writer.writerow(row)

    print(f"Amazon_deals_{date}.csv file saved successfully")


main()
