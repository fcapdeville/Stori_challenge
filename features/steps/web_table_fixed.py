from behave import when, then
from pages.pages_web_table_fixed import PagesWebTableFixed


@when('Collect names of all the {jobs}')
def collect_names(context, jobs):
    print('\033[92m' + f"\nCollect names of all the {jobs}" + '\033[0m')

    pages_web_table_fixed = PagesWebTableFixed(context)
    pages_web_table_fixed.collect_names(jobs)


@then('Print names of all the {jobs}')
def print_names(context, jobs):
    print('\033[92m' + f"\nPrint names of all the {jobs}" + '\033[0m')

    pages_web_table_fixed = PagesWebTableFixed(context)
    pages_web_table_fixed.print_names(jobs)
