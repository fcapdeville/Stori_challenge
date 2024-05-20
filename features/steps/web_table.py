from behave import when, then

from locators.locators_web_table import LocatorsWebTable


@when('Collect number of courses that cost ${cost} and their names')
def collect_courses_and_price(context, cost):
    print('\033[92m' + f"\nCollect number of courses that cost ${cost} and their names" + '\033[0m')

    # region Collect table data
    table = context.driver.find_element(*LocatorsWebTable.table_locator)
    rows = table.find_elements(*LocatorsWebTable.rows_locator)
    # endregion

    # region collect price and name
    for row in rows[1:]:    # Avoid first row
        price = row.find_element(*LocatorsWebTable.price_locator).text
        if price == cost:
            course_name = row.find_element(*LocatorsWebTable.course_name_locator).text
            context.web_table_names.append(course_name)
    # endregion


@then('Print number of courses and their names')
def print_courses_and_names(context):
    print('\033[92m' + "\nPrint number of courses and their names" + '\033[0m')

    print('\033[92m' + f"Number of courses: {len(context.web_table_names)}" + '\033[0m')

    for element in context.web_table_names:
        print('\033[92m' + f"Course associated: {element}" + '\033[0m')

    context.web_table_names = []
