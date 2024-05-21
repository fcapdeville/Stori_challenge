import time
from locators.locators_switch_to_alert import LocatorsSwitchToAlert
from features.testdata import (switch_to_alert_validation, switch_to_alert_text,
                               switch_to_alert_popup_alert, switch_to_alert_popup_confirm)


class PagesSwitchToAlert:
    def __init__(self, context):
        self.context = context

    def type_text_and_click(self, name):
        """
        Switch To Alert - Type "Stori Card" and click {name} button
        :param name: str - 'Alert' or 'Confirm'
        :return: none
        """
        # region 'name' validation
        if name not in switch_to_alert_validation:
            print('\033[91m' + f"[ERROR] Input parameter name is not supported: '{name}'" + '\033[0m')
            raise AssertionError(f"[ERROR] Input parameter name is not supported: '{name}'")
        # endregion

        # region Enter string value
        input_field = self.context.driver.find_element(*LocatorsSwitchToAlert.input_locator)
        input_field.send_keys(switch_to_alert_text)
        # endregion

        # region Click element
        if name == "Alert":
            alert_btn = self.context.driver.find_element(*LocatorsSwitchToAlert.accept_locator)
        else:
            alert_btn = self.context.driver.find_element(*LocatorsSwitchToAlert.confirm_locator)
        alert_btn.click()
        # endregion

        # Collecting popup text
        popup = self.context.driver.switch_to.alert
        print(f"\nCollected popup text: {popup.text}")

    def validate_alert_button(self):
        """
        Switch To Alert - Validate printed text in the alert and clicks OK
        :return: none
        """
        # Validating popup
        if self.context.driver.switch_to.alert.text != switch_to_alert_popup_alert:
            raise AssertionError(f"[ERROR] message present is not the same: {self.context.driver.switch_to.alert.text}")
        time.sleep(1)  # just for humans

        # Clicks 'Accept' button
        self.context.driver.switch_to.alert.accept()

    def validate_confirm_button(self):
        """
        Switch To Alert - Validate Confirm button and clicks OK
        :return: none
        """
        # Validating popup
        if self.context.driver.switch_to.alert.text != switch_to_alert_popup_confirm:
            raise AssertionError(f"[ERROR] message present is not the same: {self.context.driver.switch_to.alert.text}")
        time.sleep(1)  # just for humans

        # Click in 'ok' button
        self.context.driver.switch_to.alert.accept()
