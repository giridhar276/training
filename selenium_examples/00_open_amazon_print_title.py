"""
Example 2: Open Amazon and print page title

This script:
1. Opens Amazon India
2. Prints the title of the page
3. Closes the browser
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Amazon India
driver.get("https://www.amazon.in")
driver.maximize_window()

# Print the current web page title
print("Page Title:", driver.title)

# Wait for 5 seconds
time.sleep(5)

# Close browser
driver.quit()
