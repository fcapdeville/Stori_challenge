from locators.locators_iFrame import LocatorsIFrame
from features.testdata import iframe_validation


class PagesIFrame:
    def __init__(self, context):
        self.context = context

    def get_text_in_blue(self):
        """
        Scenario: iFrame - Get the text highlighted in blue in the iframe
        :return: none
        """
        # region Collect paragraphs from frame
        self.context.driver.switch_to.frame(LocatorsIFrame.iframe_locator)
        paragraph_locator = self.context.driver.find_elements(*LocatorsIFrame.paragraph_locator)
        # endregion

        # region check if text is in paragraphs
        for element in paragraph_locator:
            if element.text == iframe_validation:
                self.context.iframe_validation = True
        # endregion

    def print_text(self):
        """
        Scenario: iFrame - Validate printed text
        :return: none
        """
        if self.context.iframe_validation:
            print(iframe_validation)
        else:
            raise AssertionError("Text was not present in the iFrame selected")
