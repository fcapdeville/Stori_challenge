import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from behave import when, then

from features.testdata import suggestion_class_validation
from locators.locators_suggestion_class import LocatorsSuggestionClass


@when('Enter {text} in the suggestion class and selects {country}')
def enter_text_and_select(context, text, country):
    print('\033[92m' + f"\nEnter {text} in the suggestion class and selects {country}" + '\033[0m')

    # region 'text' validation
    if text not in suggestion_class_validation:
        print('\033[91m' + f"[ERROR] Input parameter text is not supported: '{text}'" + '\033[0m')
        raise AssertionError(f"[ERROR] Input parameter text is not supported: '{text}'")
    # endregion

    # region Enter search value
    suggestion_field = context.driver.find_element(*LocatorsSuggestionClass.suggestion_locator)
    suggestion_field.send_keys(text)
    # endregion

    # region Check visibility of list and element
    if text == "Me" and country == "Mexico":
        suggestion_list = WebDriverWait(context.driver, 5).until(
            expected_conditions.visibility_of_element_located(LocatorsSuggestionClass.suggestion_list_me_locator))
    elif text == "Uni" and country == "United Arab Emirates":
        suggestion_list = WebDriverWait(context.driver, 5).until(
            expected_conditions.visibility_of_element_located(LocatorsSuggestionClass.suggestion_list_uae_locator))
    elif text == "Uni" and country == "United States (USA)":
        suggestion_list = WebDriverWait(context.driver, 5).until(
            expected_conditions.visibility_of_element_located(LocatorsSuggestionClass.suggestion_list_usa_locator))
    else:
        print('\033[91m' + f"[ERROR] Input parameters are not supported: '{text}' and '{country}'" + '\033[0m')
        raise AssertionError(f"[ERROR] Input parameters are not supported: '{text}' and '{country}'")
    # endregion

    # Click suggested element
    suggestion_list.click()

    # Validate text
    context.suggestion_class_counter.append(text)
    time.sleep(1)   # Just for humans to see
    suggestion_field.clear()


@then('Suggestion Class should be correctly selected')
def validation_suggestion_class(context):
    print('\033[92m' + "\nSuggestion Class should be correctly selected" + '\033[0m')

    if context.suggestion_class_counter != suggestion_class_validation:
        print('\033[91m' + f"[ERROR] Suggestion Class was not performed successfully in all scenarios: "
                           f"'{context.suggestion_class_counter}'" + '\033[0m')
        raise AssertionError(f"[ERROR] Suggestion Class was not performed successfully in all scenarios: "
                             f"'{context.suggestion_class_counter}'")
    else:
        print('\033[92m' + "\nSuggestion Class was performed successfully" + '\033[0m')
