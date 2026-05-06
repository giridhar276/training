# 35. OOP with BeautifulSoup Web Scraping
# This example fetches a web page, extracts title and links.
# Install dependencies: pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.html_content = None

    def fetch_page(self):
        try:
            response = requests.get(self.url, timeout=10)
            if response.status_code == 200:
                self.html_content = response.text
                print("Page fetched successfully")
            else:
                print("Failed. Status code:", response.status_code)
        except Exception as e:
            print("Error while fetching page:", e)

    def show_title(self):
        if self.html_content is None:
            print("Please fetch page first")
            return

        soup = BeautifulSoup(self.html_content, "html.parser")
        if soup.title:
            print("Page Title:", soup.title.get_text(strip=True))
        else:
            print("No title found")

    def show_links(self):
        if self.html_content is None:
            print("Please fetch page first")
            return

        soup = BeautifulSoup(self.html_content, "html.parser")
        links = soup.find_all("a", href=True)

        print("Total Links:", len(links))
        for link in links[:10]:
            print(link["href"])

scraper = WebScraper("https://www.python.org")
scraper.fetch_page()
scraper.show_title()
scraper.show_links()
