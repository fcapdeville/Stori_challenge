from behave import when, then
from pages.pages_web_table import PagesWebTable


@when('Collect number of courses that cost ${cost} and their names')
def collect_courses_and_price(context, cost):
    print('\033[92m' + f"\nCollect number of courses that cost ${cost} and their names" + '\033[0m')

    pages_web_table = PagesWebTable(context)
    pages_web_table.collect_courses_and_price(cost)


@then('Print number of courses and their names')
def print_courses_and_names(context):
    print('\033[92m' + "\nPrint number of courses and their names" + '\033[0m')

    pages_web_table = PagesWebTable(context)
    pages_web_table.print_courses_and_names()
