import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators.locators_dropdown import LocatorsDropdown
from features.testdata import dropdown_possible_options, dropdown_validation


class PagesDropdown:
    def __init__(self, context):
        self.context = context

    def select_option_in_dropdown(self, option):
        """
        Scenario: Dropdown - Select option {option} in the dropdown
        :param option: str - '2' or '3'
        :return: none
        """
        # region 'option' validation
        if option not in dropdown_possible_options:
            print('\033[91m' + f"[ERROR] Input parameter option is not supported: '{option}'" + '\033[0m')
            raise AssertionError(f"[ERROR] Input parameter option is not supported: '{option}'")
        # endregion

        # region Click element
        suggestion_field = self.context.driver.find_element(*LocatorsDropdown.dropdown_locator)
        suggestion_field.click()
        # endregion

        # region Check visibility of list and element
        if option == "2":
            selection_list = WebDriverWait(self.context.driver, 5).until(
                expected_conditions.visibility_of_element_located(LocatorsDropdown.option2_locator))
        else:
            selection_list = WebDriverWait(self.context.driver, 5).until(
                expected_conditions.visibility_of_element_located(LocatorsDropdown.option3_locator))
        # endregion

        # Click element and collect value
        selection_list.click()
        self.context.dropdown_collector.append(suggestion_field.get_attribute("value"))

        time.sleep(1)  # just for humans

    def validate_change_dropdown(self):
        """
        Scenario: Dropdown - Should be able to see the change
        :return: none
        """
        if self.context.dropdown_collector != dropdown_validation:
            print('\033[91m' + f"[ERROR] Dropdown was not performed successfully in all scenarios: "
                               f"'{self.context.dropdown_collector}'" + '\033[0m')
            raise AssertionError(f"[ERROR] Dropdown was not performed successfully in all scenarios: "
                                 f"'{self.context.dropdown_collector}'")
        else:
            print("\nSuggestion Class was performed successfully")
