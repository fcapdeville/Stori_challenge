from behave import when, then
from pages.pages_suggestion_class import PagesSuggestionClass


@when('Enter {text} in the suggestion class and selects {country}')
def enter_text_and_select(context, text, country):
    print('\033[92m' + f"\nEnter {text} in the suggestion class and selects {country}" + '\033[0m')

    pages_suggestion_class = PagesSuggestionClass(context)
    pages_suggestion_class.enter_text_and_select(text, country)


@then('Suggestion Class should be correctly selected')
def validation_suggestion_class(context):
    print('\033[92m' + "\nSuggestion Class should be correctly selected" + '\033[0m')

    pages_suggestion_class = PagesSuggestionClass(context)
    pages_suggestion_class.validation_suggestion_class()
