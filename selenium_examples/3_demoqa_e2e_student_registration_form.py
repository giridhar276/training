"""
End-to-End Selenium Example 3
Website: https://demoqa.com/automation-practice-form

Flow:
1. Open student registration form
2. Fill personal details
3. Select gender and hobbies
4. Upload sample file
5. Select state and city
6. Submit form
7. Validate confirmation modal
"""

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Create sample file for upload
sample_file = Path("demoqa_upload.txt").resolve()
sample_file.write_text("Sample upload file for Selenium DemoQA form.", encoding="utf-8")

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)

try:
    driver.get("https://demoqa.com/automation-practice-form")

    # Fill basic fields
    wait.until(EC.visibility_of_element_located((By.ID, "firstName"))).send_keys("Giri")
    driver.find_element(By.ID, "lastName").send_keys("Trainer")
    driver.find_element(By.ID, "userEmail").send_keys("giri.trainer@example.com")

    # Select gender using JavaScript click because normal click may be blocked by overlays
    male_radio_label = driver.find_element(By.XPATH, "//label[text()='Male']")
    driver.execute_script("arguments[0].click();", male_radio_label)

    driver.find_element(By.ID, "userNumber").send_keys("9876543210")

    # Enter subject
    subject_input = driver.find_element(By.ID, "subjectsInput")
    subject_input.send_keys("Computer Science")
    subject_input.send_keys(Keys.ENTER)

    # Select hobby
    reading_checkbox = driver.find_element(By.XPATH, "//label[text()='Reading']")
    driver.execute_script("arguments[0].click();", reading_checkbox)

    # Upload file
    driver.find_element(By.ID, "uploadPicture").send_keys(str(sample_file))

    # Address
    driver.find_element(By.ID, "currentAddress").send_keys("Hyderabad, India")

    # Select State
    state_input = driver.find_element(By.ID, "react-select-3-input")
    state_input.send_keys("NCR")
    state_input.send_keys(Keys.ENTER)

    # Select City
    city_input = driver.find_element(By.ID, "react-select-4-input")
    city_input.send_keys("Delhi")
    city_input.send_keys(Keys.ENTER)

    # Submit form
    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    driver.execute_script("arguments[0].click();", submit_button)

    # Validate modal
    modal_title = wait.until(
        EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
    ).text

    print("Modal Title:", modal_title)

    if "Thanks for submitting the form" in modal_title:
        print("Student registration form E2E passed.")
    else:
        print("Student registration form E2E failed.")

finally:
    driver.quit()
