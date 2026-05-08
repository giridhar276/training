"""
End-to-End Selenium Example 4
Website: https://www.demoblaze.com/

Flow:
1. Open Demoblaze
2. Open a product
3. Add product to cart
4. Handle alert
5. Open cart
6. Place order
7. Fill purchase form
8. Validate purchase confirmation
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)

try:
    driver.get("https://www.demoblaze.com/")

    # Open first product
    first_product = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6"))
    )
    first_product.click()

    # Add to cart
    add_to_cart = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Add to cart"))
    )
    add_to_cart.click()

    # Accept alert
    alert = wait.until(EC.alert_is_present())
    print("Alert Text:", alert.text)
    alert.accept()

    # Open cart
    wait.until(EC.element_to_be_clickable((By.ID, "cartur"))).click()

    # Place order
    place_order = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']"))
    )
    place_order.click()

    # Fill purchase details
    wait.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys("Giri")
    driver.find_element(By.ID, "country").send_keys("India")
    driver.find_element(By.ID, "city").send_keys("Hyderabad")
    driver.find_element(By.ID, "card").send_keys("4111111111111111")
    driver.find_element(By.ID, "month").send_keys("05")
    driver.find_element(By.ID, "year").send_keys("2026")

    driver.find_element(By.XPATH, "//button[text()='Purchase']").click()

    confirmation = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "sweet-alert"))
    )

    print("Confirmation Text:")
    print(confirmation.text)

    if "Thank you for your purchase" in confirmation.text:
        print("Demoblaze purchase E2E passed.")
    else:
        print("Demoblaze purchase E2E failed.")

finally:
    driver.quit()
