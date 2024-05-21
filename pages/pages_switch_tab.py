class PagesSwitchTab:
    def __init__(self, context):
        self.context = context

    def click_open_window(self):
        """
        Scenario: Switch Tab - Click "Open Tab" button
        :return: none
        """
        raise NotImplementedError("Test was not implemented due to failure in manual exploratory tests")

    def see_new_window(self):
        """
        Scenario: Switch Tab - See new opened tab and scrolls until specific button is visible
        :return: none
        """
        raise NotImplementedError("Test was not implemented due to failure in manual exploratory tests")

    def see_text(self):
        """
        Scenario: Switch Tab - Take a screenshot that includes the button and saves it with the test case name
        :return: none
        """
        raise NotImplementedError("Test was not implemented due to failure in manual exploratory tests")

    def closed_window(self):
        """
        Scenario: Switch Tab - Return to first window without closing the new tab
        :return: none
        """
        raise NotImplementedError("Test was not implemented due to failure in manual exploratory tests")
