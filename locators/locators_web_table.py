from selenium.webdriver.common.by import By


class LocatorsWebTable:
    # Login page objects
    table_locator = (By.CSS_SELECTOR, "table.table-display#product[name='courses']")
    rows_locator = (By.CSS_SELECTOR, 'tbody tr')
    price_locator = (By.CSS_SELECTOR, 'td:nth-child(3)')
    course_name_locator = (By.CSS_SELECTOR, 'td:nth-child(2)')
