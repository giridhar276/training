"""
End-to-End Selenium Example 2
Website: https://practicetestautomation.com/practice-test-login/

Flow:
1. Open login page
2. Login with valid credentials
3. Validate successful login page
4. Click Log out
5. Validate return to login page
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
    driver.get("https://practicetestautomation.com/practice-test-login/")

    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    heading = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1"))).text
    print("After Login Heading:", heading)

    # Click logout button/link
    logout_link = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Log out"))
    )
    logout_link.click()

    # Validate login page is visible again
    login_button = wait.until(
        EC.visibility_of_element_located((By.ID, "submit"))
    )

    print("Logout successful. Login button displayed:", login_button.is_displayed())

finally:
    driver.quit()
