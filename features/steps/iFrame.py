from behave import when, then

from locators.locators_iFrame import LocatorsIFrame
from features.testdata import iframe_validation


@when('Get the text highlighted in blue in the iframe')
def get_text_in_blue(context):
    print('\033[92m' + "\nGet the text highlighted in blue in the iframe" + '\033[0m')

    # region Collect paragraphs from frame
    context.driver.switch_to.frame(LocatorsIFrame.iframe_locator)
    paragraph_locator = context.driver.find_elements(*LocatorsIFrame.paragraph_locator)
    # endregion

    # region check if text is in paragraphs
    for element in paragraph_locator:
        if element.text == iframe_validation:
            context.iframe_validation = True
    # endregion


@then('Validate printed text')
def print_text(context):
    print('\033[92m' + "\nValidate printed text" + '\033[0m')

    if context.iframe_validation:
        print(iframe_validation)
    else:
        raise AssertionError("Text was not present in the iFrame selected")
