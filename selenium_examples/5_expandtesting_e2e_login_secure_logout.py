"""
End-to-End Selenium Example 5
Website: https://practice.expandtesting.com/login

Flow:
1. Open login page
2. Login with valid credentials
3. Validate secure area
4. Logout
5. Validate logout/login page
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
    driver.get("https://practice.expandtesting.com/login")

    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("practice")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    flash_message = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text

    print("Login Flash Message:", flash_message)

    # Logout
    logout_button = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
    )
    logout_button.click()

    logout_flash = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text

    print("Logout Flash Message:", logout_flash)

finally:
    driver.quit()
