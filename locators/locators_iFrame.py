from selenium.webdriver.common.by import By


class LocatorsIFrame:
    # Login page objects
    iframe_locator = "courses-iframe"
    paragraph_locator = (By.CSS_SELECTOR, "ul.list-style-two > li")
