"""
End-to-End Selenium Example 8
Website: https://the-internet.herokuapp.com/upload

Flow:
1. Create a sample file
2. Open upload page
3. Upload file
4. Submit
5. Validate uploaded filename
"""

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


sample_file = Path("sample_selenium_upload.txt").resolve()
sample_file.write_text("This file was created and uploaded by Selenium.", encoding="utf-8")

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

try:
    driver.get("https://the-internet.herokuapp.com/upload")

    wait.until(EC.presence_of_element_located((By.ID, "file-upload"))).send_keys(str(sample_file))
    driver.find_element(By.ID, "file-submit").click()

    heading = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3"))).text
    uploaded_file = driver.find_element(By.ID, "uploaded-files").text

    print("Heading:", heading)
    print("Uploaded File:", uploaded_file)

    if uploaded_file == sample_file.name:
        print("File upload E2E passed.")
    else:
        print("File upload E2E failed.")

finally:
    driver.quit()
