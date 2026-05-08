"""
Example 1: Open Amazon website using Selenium Chrome

This script:
1. Opens Chrome browser
2. Opens Amazon India website
3. Maximizes the browser window
4. Waits for a few seconds
5. Closes the browser
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


# Create Chrome browser object using webdriver-manager
# webdriver-manager automatically downloads the correct ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Amazon India website
driver.get("https://www.amazon.in")

# Maximize browser window
driver.maximize_window()

# Wait for 5 seconds so that we can see the opened page
time.sleep(5)

# Close the browser
driver.quit()
