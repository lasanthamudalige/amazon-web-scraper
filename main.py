from bs4 import BeautifulSoup
import requests


def main():
    # add header files because this is not to browser login
    headers = {'Accepted-Language': 'en-US,en;q=0.9',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

    # product url
    url = "https://www.amazon.com/gp/goldbox?ref_=nav_cs_gb&deals-widget=%257B%2522version%2522%253A1%252C%2522viewIndex%2522%253A0%252C%2522presetId%2522%253A%252264049D9C1CDF5B41F83FDB7974F9054B%2522%252C%2522departments%2522%253A%255B%2522172282%2522%255D%252C%2522sorting%2522%253A%2522BY_CUSTOM_CRITERION%2522%257D"

    # response from the website
    response = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    # print(soup)


main()
