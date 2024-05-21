import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from features.testdata import suggestion_class_validation
from locators.locators_suggestion_class import LocatorsSuggestionClass


class PagesSuggestionClass:
    def __init__(self, context):
        self.context = context

    def enter_text_and_select(self, text, country):
        """
        Scenario: Suggestion Class - Enter {text} in the suggestion class and selects {country}
        :param text: str - 'Me' or 'Uni'
        :param country: str - 'Mexico', 'United Arab Emirates' or 'United States (USA)'
        :return: none
        """
        # region 'text' validation
        if text not in suggestion_class_validation:
            print('\033[91m' + f"[ERROR] Input parameter text is not supported: '{text}'" + '\033[0m')
            raise AssertionError(f"[ERROR] Input parameter text is not supported: '{text}'")
        # endregion

        # region Enter search value
        suggestion_field = self.context.driver.find_element(*LocatorsSuggestionClass.suggestion_locator)
        suggestion_field.send_keys(text)
        # endregion

        # region Check visibility of list and element
        if text == "Me" and country == "Mexico":
            suggestion_list = WebDriverWait(self.context.driver, 5).until(
                expected_conditions.visibility_of_element_located(LocatorsSuggestionClass.suggestion_list_me_locator))
        elif text == "Uni" and country == "United Arab Emirates":
            suggestion_list = WebDriverWait(self.context.driver, 5).until(
                expected_conditions.visibility_of_element_located(LocatorsSuggestionClass.suggestion_list_uae_locator))
        elif text == "Uni" and country == "United States (USA)":
            suggestion_list = WebDriverWait(self.context.driver, 5).until(
                expected_conditions.visibility_of_element_located(LocatorsSuggestionClass.suggestion_list_usa_locator))
        else:
            print('\033[91m' + f"[ERROR] Input parameters are not supported: '{text}' and '{country}'" + '\033[0m')
            raise AssertionError(f"[ERROR] Input parameters are not supported: '{text}' and '{country}'")
        # endregion

        # Click suggested element
        suggestion_list.click()

        # Validate text
        self.context.suggestion_class_counter.append(text)
        time.sleep(1)  # Just for humans to see
        suggestion_field.clear()

    def validation_suggestion_class(self):
        """
        Scenario: Suggestion Class - Suggestion Class should be correctly selected
        :return: none
        """
        if self.context.suggestion_class_counter != suggestion_class_validation:
            print('\033[91m' + f"[ERROR] Suggestion Class was not performed successfully in all scenarios: "
                               f"'{self.context.suggestion_class_counter}'" + '\033[0m')
            raise AssertionError(f"[ERROR] Suggestion Class was not performed successfully in all scenarios: "
                                 f"'{self.context.suggestion_class_counter}'")
        else:
            print("\nSuggestion Class was performed successfully")
