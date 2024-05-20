from selenium.webdriver.common.by import By


class LocatorsWebTableFixed:
    # Login page objects
    table_locator = (By.CSS_SELECTOR, "div.tableFixHead > table#product")
    row_locator = (By.XPATH, ".//tbody/tr")
    name_locator = (By.XPATH, ".//td[1]")
    position_locator = (By.XPATH, ".//td[2]")
