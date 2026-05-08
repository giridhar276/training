"""
End-to-End Selenium Example 10
Website: https://books.toscrape.com/

Flow:
1. Open Books to Scrape
2. Open Travel category
3. Read book names and prices
4. Open first book
5. Validate product information page
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

try:
    driver.get("https://books.toscrape.com/")

    # Open Travel category
    travel_link = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Travel"))
    )
    travel_link.click()

    # Read book cards
    books = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.product_pod"))
    )

    print("Books in Travel Category:")
    for book in books:
        title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
        price = book.find_element(By.CLASS_NAME, "price_color").text
        print(title, "-", price)

    # Open first book details page
    first_book_link = books[0].find_element(By.CSS_SELECTOR, "h3 a")
    first_book_title = first_book_link.get_attribute("title")
    first_book_link.click()

    product_title = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".product_main h1"))
    ).text

    print("\nOpened Book:", product_title)

    if first_book_title == product_title:
        print("Book category extraction E2E passed.")
    else:
        print("Book category extraction E2E failed.")

finally:
    driver.quit()
