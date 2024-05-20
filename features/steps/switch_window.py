from behave import when, then


@when('Click "Open Window" button')
def click_open_window(context):
    print('\033[92m' + "\nClick 'Open Window' button" + '\033[0m')

    raise NotImplementedError("Test was not implemented due to failure in manual exploratory tests")


@when('See new opened window')
def see_new_window(context):
    print('\033[92m' + "\nSee new opened window" + '\033[0m')

    raise NotImplementedError("Test was not implemented due to failure in manual exploratory tests")


@then('See "30 day money back guarantee" text')
def see_text(context):
    print('\033[92m' + "\nSee '30 day money back guarantee' text" + '\033[0m')

    raise NotImplementedError("Test was not implemented due to failure in manual exploratory tests")


@then('Window should be closed if text is not found')
def closed_window(context):
    print('\033[92m' + "\nWindow should be closed if text is not found" + '\033[0m')

    raise NotImplementedError("Test was not implemented due to failure in manual exploratory tests")
