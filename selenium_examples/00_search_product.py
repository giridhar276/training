"""
Example 3: Search for a product on Amazon

This script:
1. Opens Amazon India
2. Finds the search box
3. Enters a product name
4. Clicks the search button
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

# Locate the search box using ID
search_box = driver.find_element(By.ID, "twotabsearchtextbox")

# Type product name into search box
search_box.send_keys("wireless mouse")

# Locate the search button using ID
search_button = driver.find_element(By.ID, "nav-search-submit-button")

# Click search button
search_button.click()

time.sleep(5)

# Close browser
driver.quit()
