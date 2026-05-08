# Selenium 10 End-to-End Examples - Different Websites

This package contains 10 independent Selenium scripts.

Each script:
- uses a different website/application
- performs an end-to-end flow
- includes comments for classroom explanation
- can be run separately

## Install

```bash
pip install -r requirements.txt
```

## Browser Requirement

Install Google Chrome.

Selenium 4 includes Selenium Manager, which can automatically manage ChromeDriver in most environments.

## Run Scripts

```bash
python 1_saucedemo_e2e_checkout.py
python 2_practicetestautomation_e2e_login_logout.py
python 3_demoqa_e2e_student_registration_form.py
python 4_demoblaze_e2e_add_to_cart_purchase.py
python 5_expandtesting_e2e_login_secure_logout.py
python 6_automationexercise_e2e_search_add_cart.py
python 7_orangehrm_e2e_login_dashboard_logout.py
python 8_herokuapp_e2e_file_upload.py
python 9_jqueryui_e2e_drag_and_drop.py
python 10_books_toscrape_e2e_search_category_extract.py
```

## Websites Used

1. https://www.saucedemo.com/
2. https://practicetestautomation.com/practice-test-login/
3. https://demoqa.com/automation-practice-form
4. https://www.demoblaze.com/
5. https://practice.expandtesting.com/login
6. https://automationexercise.com/products
7. https://opensource-demo.orangehrmlive.com/
8. https://the-internet.herokuapp.com/upload
9. https://jqueryui.com/droppable/
10. https://books.toscrape.com/

## Notes

These are public demo/practice websites, but public sites can change.
If any locator fails later, inspect the page and update the locator.
