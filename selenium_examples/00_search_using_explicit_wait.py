"""
Example 5: Search product using explicit wait

This is a better Selenium practice than using time.sleep().
Explicit wait waits until the element is visible or clickable.

This script:
1. Opens Amazon India
2. Waits for search box to be visible
3. Searches for Python books
4. Waits for search button to be clickable
5. Clicks the search button
6. Closes the browser
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open Amazon India
driver.get("https://www.amazon.in")

# Create wait object with maximum wait time of 10 seconds
wait = WebDriverWait(driver, 10)

# Wait until search box is visible
search_box = wait.until(
    EC.visibility_of_element_located((By.ID, "twotabsearchtextbox"))
)

# Enter product name
search_box.send_keys("python books")

# Wait until search button is clickable
search_button = wait.until(
    EC.element_to_be_clickable((By.ID, "nav-search-submit-button"))
)

# Click search button
search_button.click()

print("Search completed successfully")

time.sleep(5)

# Close browser
driver.quit()
