"""
End-to-End Selenium Example 1
Website: https://www.saucedemo.com/

Flow:
1. Open SauceDemo
2. Login
3. Add product to cart
4. Checkout
5. Enter customer details
6. Finish order
7. Validate success message
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#options = Options()
#options.add_argument("--start-maximized")

#driver = webdriver.Chrome(options=options)


try:
    options = Options()
    
    # Disable Chrome password manager and breach warning popup
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "safebrowsing.enabled": False,
        "safebrowsing.password_protection_enabled": False,
    }
    
    options.add_experimental_option("prefs", prefs)
    
    # Optional Chrome cleanup options
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    
    driver = webdriver.Chrome(options=options)

    wait = WebDriverWait(driver, 15)
    
    driver.get("https://www.saucedemo.com/")

    # Login with standard demo credentials
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Wait for inventory page
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))

    # Add first product to cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Open cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Checkout
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # Enter checkout information
    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Giri")
    driver.find_element(By.ID, "last-name").send_keys("Trainer")
    driver.find_element(By.ID, "postal-code").send_keys("500001")

    driver.find_element(By.ID, "continue").click()

    # Finish order
    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

    # Validate order completion
    success_message = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    ).text

    print("Success Message:", success_message)

    if "Thank you for your order" in success_message:
        print("E2E checkout flow passed.")
    else:
        print("E2E checkout flow failed.")

finally:
    driver.quit()
