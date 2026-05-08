"""
End-to-End Selenium Example 6
Website: https://automationexercise.com/

Flow:
1. Open products page
2. Search product
3. Add first matching product to cart
4. Open cart
5. Validate product is present in cart
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
    driver.get("https://automationexercise.com/products")

    # Search for a product
    search_box = wait.until(EC.visibility_of_element_located((By.ID, "search_product")))
    search_box.send_keys("top")
    driver.find_element(By.ID, "submit_search").click()

    # Wait for searched products heading
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Searched Products')]")))

    # Add first product to cart
    first_add_to_cart = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//a[contains(@class,'add-to-cart')])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", first_add_to_cart)
    driver.execute_script("arguments[0].click();", first_add_to_cart)

    # Click View Cart in modal
    view_cart = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//u[text()='View Cart']"))
    )
    view_cart.click()

    # Validate cart table
    cart_table = wait.until(
        EC.visibility_of_element_located((By.ID, "cart_info"))
    )

    print("Cart displayed:", cart_table.is_displayed())

    product_names = driver.find_elements(By.CSS_SELECTOR, ".cart_description h4 a")

    print("Products in Cart:")
    for item in product_names:
        print(item.text)

finally:
    driver.quit()
