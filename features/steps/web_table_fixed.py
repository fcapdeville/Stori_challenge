from behave import when, then

from locators.locators_web_table_fixed import LocatorsWebTableFixed


@when('Collect names of all the {jobs}')
def collect_names(context, jobs):
    print('\033[92m' + f"\nCollect names of all the {jobs}" + '\033[0m')

    # region Collect table data
    table = context.driver.find_element(*LocatorsWebTableFixed.table_locator)
    rows = table.find_elements(*LocatorsWebTableFixed.row_locator)
    # endregion

    # region collect names
    for row in rows:    # Avoid first row
        position = row.find_element(*LocatorsWebTableFixed.position_locator)

        if position.text == jobs:
            name = row.find_element(*LocatorsWebTableFixed.name_locator)
            context.web_table_fixed_names.append(name.text)
    # endregion


@then('Print names of all the {jobs}')
def print_names(context, jobs):
    print('\033[92m' + f"\nPrint names of all the {jobs}" + '\033[0m')

    for element in context.web_table_fixed_names:
        print('\033[92m' + f"Name of {jobs}: {element}" + '\033[0m')

    context.web_table_fixed_names = []
