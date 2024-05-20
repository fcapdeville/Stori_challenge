import time
from behave import when, then

from features.testdata import (switch_to_alert_validation, switch_to_alert_text,
                               switch_to_alert_popup_alert, switch_to_alert_popup_confirm)
from locators.locators_switch_to_alert import LocatorsSwitchToAlert


@when('Type "Stori Card" and click {name} button')
def type_text_and_click(context, name):
    print('\033[92m' + f"\nType 'Stori Card' and click {name} button" + '\033[0m')

    # region 'name' validation
    if name not in switch_to_alert_validation:
        print('\033[91m' + f"[ERROR] Input parameter name is not supported: '{name}'" + '\033[0m')
        raise AssertionError(f"[ERROR] Input parameter name is not supported: '{name}'")
    # endregion

    # region Enter string value
    input_field = context.driver.find_element(*LocatorsSwitchToAlert.input_locator)
    input_field.send_keys(switch_to_alert_text)
    # endregion

    # region Click element
    if name == "Alert":
        alert_btn = context.driver.find_element(*LocatorsSwitchToAlert.accept_locator)
    else:
        alert_btn = context.driver.find_element(*LocatorsSwitchToAlert.confirm_locator)
    alert_btn.click()
    # endregion

    # Collecting popup text
    popup = context.driver.switch_to.alert
    print('\033[92m' + f"\nCollected popup text: {popup.text}" + '\033[0m')


@then('Validate printed text in the alert and clicks OK')
def validate_alert_button(context):
    print('\033[92m' + f"\nValidate printed text in the alert and clicks OK" + '\033[0m')

    # Validating popup
    if context.driver.switch_to.alert.text != switch_to_alert_popup_alert:
        raise AssertionError(f"[ERROR] message present is not the same: {context.driver.switch_to.alert.text}")
    time.sleep(1)   # just for humans

    # Clicks 'Accept' button
    context.driver.switch_to.alert.accept()


@then('Validate Confirm button and clicks OK')
def validate_confirm_button(context):
    print('\033[92m' + f"\nValidate Confirm button and clicks OK" + '\033[0m')

    # Validating popup
    if context.driver.switch_to.alert.text != switch_to_alert_popup_confirm:
        raise AssertionError(f"[ERROR] message present is not the same: {context.driver.switch_to.alert.text}")
    time.sleep(1)   # just for humans

    # Click in 'ok' button
    context.driver.switch_to.alert.accept()
