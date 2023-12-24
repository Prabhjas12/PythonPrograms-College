import requests
from bs4 import BeautifulSoup
import time

urls = {
    'BestBuy': 'https://www.bestbuy.com/site/searchpage.jsp?st=PlayStation+Portal',
    'Target': 'https://www.target.com/s?searchTerm=PlayStation+Portal',
    'GameStop': 'https://www.gamestop.com/search/?q=PlayStation+Portal',
    'Walmart': 'https://www.walmart.com/search/?query=PlayStation+Portal',
    'Sony': 'https://www.sony.com/search?query=PlayStation+Portal',
    'Amazon': 'https://www.amazon.com/s?k=PlayStation+Portal'
}

def check_availability():
    headers = {'User-Agent': 'Mozilla/5.0'}
    for store, url in urls.items():
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        if soup.find('button', class_='add_to_cart_button_class'):
            print(f"{store}: Available")
        else:
            print(f"{store}: Not Available")

while True:
    check_availability()
    time.sleep(3600)  
