"""
End-to-End Selenium Example 7
Website: https://opensource-demo.orangehrmlive.com/

Flow:
1. Open OrangeHRM demo login page
2. Login with demo admin credentials
3. Validate dashboard
4. Open user menu
5. Logout
6. Validate login page
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 25)

try:
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Login
    wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Validate dashboard heading
    dashboard_heading = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
    ).text

    print("Page Heading:", dashboard_heading)

    # Open user dropdown
    wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-name"))
    ).click()

    # Logout
    wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
    ).click()

    # Validate login button visible
    login_button = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']"))
    )

    print("Logout successful. Login button visible:", login_button.is_displayed())

finally:
    driver.quit()
