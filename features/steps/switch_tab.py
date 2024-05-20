from behave import when, then


@when('Click "Open Tab" button')
def click_open_window(context):
    print('\033[92m' + "\nClick 'Open Tab' button" + '\033[0m')

    raise NotImplementedError("Test was not implemented due to failure in manual exploratory tests")


@when('See new opened tab and scrolls until specific button is visible')
def see_new_window(context):
    print('\033[92m' + "\nSee new opened tab and scrolls until specific button is visible" + '\033[0m')

    raise NotImplementedError("Test was not implemented due to failure in manual exploratory tests")


@then('Take a screenshot that includes the button and saves it with the test case name')
def see_text(context):
    print('\033[92m' + "\nTake a screenshot that includes the button and saves it with the test case name" + '\033[0m')

    raise NotImplementedError("Test was not implemented due to failure in manual exploratory tests")


@then('Return to first window without closing the new tab')
def closed_window(context):
    print('\033[92m' + "\nReturn to first window without closing the new tab" + '\033[0m')

    raise NotImplementedError("Test was not implemented due to failure in manual exploratory tests")
