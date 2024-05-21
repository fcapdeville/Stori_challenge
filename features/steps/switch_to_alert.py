from behave import when, then
from pages.pages_switch_to_alert import PagesSwitchToAlert


@when('Type "Stori Card" and click {name} button')
def type_text_and_click(context, name):
    print('\033[92m' + f"\nType 'Stori Card' and click {name} button" + '\033[0m')

    pages_switch_to_alert = PagesSwitchToAlert(context)
    pages_switch_to_alert.type_text_and_click(name)


@then('Validate printed text in the alert and clicks OK')
def validate_alert_button(context):
    print('\033[92m' + f"\nValidate printed text in the alert and clicks OK" + '\033[0m')

    pages_switch_to_alert = PagesSwitchToAlert(context)
    pages_switch_to_alert.validate_alert_button()


@then('Validate Confirm button and clicks OK')
def validate_confirm_button(context):
    print('\033[92m' + f"\nValidate Confirm button and clicks OK" + '\033[0m')

    pages_switch_to_alert = PagesSwitchToAlert(context)
    pages_switch_to_alert.validate_confirm_button()
