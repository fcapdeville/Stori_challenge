from behave import when, then
from pages.pages_switch_window import PagesSwitchWindow


@when('Click "Open Window" button')
def click_open_window(context):
    print('\033[92m' + "\nClick 'Open Window' button" + '\033[0m')

    pages_switch_window = PagesSwitchWindow(context)
    pages_switch_window.click_open_window()


@when('See new opened window')
def see_new_window(context):
    print('\033[92m' + "\nSee new opened window" + '\033[0m')

    pages_switch_window = PagesSwitchWindow(context)
    pages_switch_window.see_new_window()


@then('See "30 day money back guarantee" text')
def see_text(context):
    print('\033[92m' + "\nSee '30 day money back guarantee' text" + '\033[0m')

    pages_switch_window = PagesSwitchWindow(context)
    pages_switch_window.see_text()


@then('Window should be closed if text is not found')
def closed_window(context):
    print('\033[92m' + "\nWindow should be closed if text is not found" + '\033[0m')

    pages_switch_window = PagesSwitchWindow(context)
    pages_switch_window.closed_window()
