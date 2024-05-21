from behave import when, then
from pages.pages_iFrame import PagesIFrame


@when('Get the text highlighted in blue in the iframe')
def get_text_in_blue(context):
    print('\033[92m' + "\nGet the text highlighted in blue in the iframe" + '\033[0m')

    pages_iframe = PagesIFrame(context)
    pages_iframe.get_text_in_blue()


@then('Validate printed text')
def print_text(context):
    print('\033[92m' + "\nValidate printed text" + '\033[0m')

    pages_iframe = PagesIFrame(context)
    pages_iframe.print_text()
