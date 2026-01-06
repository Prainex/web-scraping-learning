# Web Scraping Learning Journey

## Day 1: Getting Started with BeautifulSoup

### What I Learned
- Set up a Python environment for web scraping
- Installed essential libraries: `requests` and `beautifulsoup4`
- Fixed deprecation warnings (replaced `findAll` with `find_all`)
- Understanding HTML structure and navigation

### Project: Scraping Book Categories
Built a simple scraper that extracts all book categories from [Books to Scrape](https://books.toscrape.com)

**Key Concepts:**
- Making HTTP requests with `requests.get()`
- Parsing HTML with BeautifulSoup
- Navigating the DOM tree using `find()` and `find_all()`
- Extracting text content with `get_text(strip=True)`

**Code Highlights:**
```python
# Finding nested elements
nav_list = soup.find('ul', class_='nav-list')
books_li = nav_list.find('li')
categories_ul = books_li.find('ul')

# Iterating through elements
for category_li in categories_ul.find_all('li'):
    link = category_li.find('a')
    if link:
        print(link.get_text(strip=True))
```

### Challenges Faced
1. Initially used empty class selector `class_=''` which returned no results
2. Had to inspect the HTML structure to understand the nested navigation
3. Learned the importance of understanding DOM hierarchy before scraping

### Next Steps
- Learn to scrape multiple pages
- Extract more detailed information (book titles, prices, ratings)
- Handle errors and edge cases
