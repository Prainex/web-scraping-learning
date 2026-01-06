import requests
from bs4 import BeautifulSoup as BS

response = requests.get('https://books.toscrape.com')
soup = BS(response.content, 'html.parser')

# Find the nav list and get the first li (Books category)
nav_list = soup.find('ul', class_='nav-list')
books_li = nav_list.find('li')
categories_ul = books_li.find('ul')

# Extract all category names
for category_li in categories_ul.find_all('li'):
    link = category_li.find('a')
    if link:
        print(link.get_text(strip=True))