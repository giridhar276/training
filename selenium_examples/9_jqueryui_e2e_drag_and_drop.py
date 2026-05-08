"""
End-to-End Selenium Example 9
Website: https://jqueryui.com/droppable/

Flow:
1. Open jQuery UI Droppable page
2. Switch into demo iframe
3. Drag source element
4. Drop into target element
5. Validate dropped message
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)

try:
    driver.get("https://jqueryui.com/droppable/")

    # The actual demo is inside an iframe
    iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".demo-frame")))
    driver.switch_to.frame(iframe)

    source = wait.until(EC.visibility_of_element_located((By.ID, "draggable")))
    target = wait.until(EC.visibility_of_element_located((By.ID, "droppable")))

    # Drag and drop
    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()

    # Validate target text after drop
    result_text = target.text
    print("Target Text After Drop:", result_text)

    if "Dropped" in result_text:
        print("Drag and drop E2E passed.")
    else:
        print("Drag and drop E2E failed.")

finally:
    driver.quit()
