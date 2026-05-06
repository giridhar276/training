# 36. OOP with BeautifulSoup using Local HTML
# This is useful for classroom demos when internet is not available.

from bs4 import BeautifulSoup

class LocalHTMLParser:
    def __init__(self, filename):
        self.filename = filename
        self.content = None

    def read_file(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            self.content = file.read()
        print("HTML file loaded")

    def show_products(self):
        soup = BeautifulSoup(self.content, "html.parser")
        products = soup.find_all("div", class_="product")

        for product in products:
            name = product.find("h2").get_text(strip=True)
            price = product.find("span", class_="price").get_text(strip=True)
            print(name, "-", price)

parser = LocalHTMLParser("sample_products.html")
parser.read_file()
parser.show_products()
