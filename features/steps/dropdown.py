import time
from behave import when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from features.testdata import dropdown_possible_options, dropdown_validation
from locators.locators_dropdown import LocatorsDropdown


@when('Select option {option} in the dropdown')
def select_option_in_dropdown(context, option):
    print('\033[92m' + f"\nSelect option {option} in the dropdown" + '\033[0m')

    # region 'option' validation
    if option not in dropdown_possible_options:
        print('\033[91m' + f"[ERROR] Input parameter option is not supported: '{option}'" + '\033[0m')
        raise AssertionError(f"[ERROR] Input parameter option is not supported: '{option}'")
    # endregion

    # region Click element
    suggestion_field = context.driver.find_element(*LocatorsDropdown.dropdown_locator)
    suggestion_field.click()
    # endregion

    # region Check visibility of list and element
    if option == "2":
        selection_list = WebDriverWait(context.driver, 5).until(
            expected_conditions.visibility_of_element_located(LocatorsDropdown.option2_locator))
    else:
        selection_list = WebDriverWait(context.driver, 5).until(
            expected_conditions.visibility_of_element_located(LocatorsDropdown.option3_locator))
    # endregion

    # Click element and collect value
    selection_list.click()
    context.dropdown_collector.append(suggestion_field.get_attribute("value"))

    time.sleep(1)   # just for humans


@then('Should be able to see the change')
def validate_change_dropdown(context):
    print('\033[92m' + "\nShould be able to see the change" + '\033[0m')

    if context.dropdown_collector != dropdown_validation:
        print('\033[91m' + f"[ERROR] Dropdown was not performed successfully in all scenarios: "
                           f"'{context.dropdown_collector}'" + '\033[0m')
        raise AssertionError(f"[ERROR] Dropdown was not performed successfully in all scenarios: "
                             f"'{context.dropdown_collector}'")
    else:
        print('\033[92m' + "\nSuggestion Class was performed successfully" + '\033[0m')

    print(context.dropdown_collector)
