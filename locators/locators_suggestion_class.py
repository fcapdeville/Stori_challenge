from selenium.webdriver.common.by import By


class LocatorsSuggestionClass:
    # Login page objects
    suggestion_locator = (By.ID, "autocomplete")
    suggestion_list_me_locator = (By.XPATH, "//div[contains(text(),'Mexico')]")
    suggestion_list_usa_locator = (By.XPATH, "//div[contains(text(),'United States (USA)')]")
    all_suggestions_locator = (By.ID, "ui-id-1")
    suggestion_list_uae_locator = (By.XPATH, "//div[contains(text(),'United Arab Emirates')]")
