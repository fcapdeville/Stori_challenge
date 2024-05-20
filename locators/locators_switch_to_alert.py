from selenium.webdriver.common.by import By


class LocatorsSwitchToAlert:
    # Login page objects
    input_locator = (By.XPATH, '//*[@id="name"]')
    accept_locator = (By.XPATH, '//*[@id="alertbtn"]')
    confirm_locator = (By.XPATH, '//*[@id="confirmbtn"]')
    popup_locator = (By.XPATH, )
