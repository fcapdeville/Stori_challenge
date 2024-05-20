from selenium.webdriver.common.by import By


class LocatorsDropdown:
    # Login page objects
    dropdown_locator = (By.XPATH, "/html/body/div[1]/div[3]/fieldset/select")
    option2_locator = (By.XPATH, "/html/body/div[1]/div[3]/fieldset/select/option[3]")
    option3_locator = (By.XPATH, "/html/body/div[1]/div[3]/fieldset/select/option[4]")
