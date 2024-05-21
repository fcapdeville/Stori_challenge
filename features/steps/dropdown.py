from behave import when, then
from pages.pages_dropdown import PagesDropdown


@when('Select option {option} in the dropdown')
def select_option_in_dropdown(context, option):
    print('\033[92m' + f"\nSelect option {option} in the dropdown" + '\033[0m')

    pages_dropdown = PagesDropdown(context)
    pages_dropdown.select_option_in_dropdown(option)


@then('Should be able to see the change')
def validate_change_dropdown(context):
    print('\033[92m' + "\nShould be able to see the change" + '\033[0m')

    pages_dropdown = PagesDropdown(context)
    pages_dropdown.validate_change_dropdown()
