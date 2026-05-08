"""
Example 4: Search product and print product names

This script:
1. Opens Amazon India
2. Searches for laptop bags
3. Captures product title elements
4. Prints first 10 product names
5. Closes the browser
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Amazon India
driver.get("https://www.amazon.in")
driver.maximize_window()

time.sleep(3)

# Search for product
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("laptop bag")

search_button = driver.find_element(By.ID, "nav-search-submit-button")
search_button.click()

time.sleep(5)

# Find product names from search result page
# Amazon page structure may change sometimes, so this XPath may need adjustment later
products = driver.find_elements(
    By.XPATH,
    "//span[@class='a-size-medium a-color-base a-text-normal']"
)

print("Product Names:")

# Print first 10 product names
for product in products[:10]:
    if product.text.strip():
        print(product.text)

# Close browser
driver.quit()
