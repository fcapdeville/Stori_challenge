from behave import when, then
from pages.pages_switch_tab import PagesSwitchTab


@when('Click "Open Tab" button')
def click_open_window(context):
    print('\033[92m' + "\nClick 'Open Tab' button" + '\033[0m')

    pages_switch_tab = PagesSwitchTab(context)
    pages_switch_tab.click_open_window()


@when('See new opened tab and scrolls until specific button is visible')
def see_new_window(context):
    print('\033[92m' + "\nSee new opened tab and scrolls until specific button is visible" + '\033[0m')

    pages_switch_tab = PagesSwitchTab(context)
    pages_switch_tab.see_new_window()


@then('Take a screenshot that includes the button and saves it with the test case name')
def see_text(context):
    print('\033[92m' + "\nTake a screenshot that includes the button and saves it with the test case name" + '\033[0m')

    pages_switch_tab = PagesSwitchTab(context)
    pages_switch_tab.see_text()


@then('Return to first window without closing the new tab')
def closed_window(context):
    print('\033[92m' + "\nReturn to first window without closing the new tab" + '\033[0m')

    pages_switch_tab = PagesSwitchTab(context)
    pages_switch_tab.closed_window()
