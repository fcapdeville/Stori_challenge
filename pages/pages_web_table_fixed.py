from locators.locators_web_table_fixed import LocatorsWebTableFixed


class PagesWebTableFixed:
    def __init__(self, context):
        self.context = context

    def collect_names(self, jobs):
        """
        Scenario: Web Table Fixed - Collect names of all the {jobs}
        :param jobs: str - 'Engineer' or 'Businessman'
        :return: none
        """
        # region Collect table data
        table = self.context.driver.find_element(*LocatorsWebTableFixed.table_locator)
        rows = table.find_elements(*LocatorsWebTableFixed.row_locator)
        # endregion

        # region collect names
        for row in rows:  # Avoid first row
            position = row.find_element(*LocatorsWebTableFixed.position_locator)

            if position.text == jobs:
                name = row.find_element(*LocatorsWebTableFixed.name_locator)
                self.context.web_table_fixed_names.append(name.text)
        # endregion

    def print_names(self, jobs):
        """
        Scenario: Web Table Fixed - Print names of all the {jobs}
        :param jobs: str - 'Engineer' or 'Businessman'
        :return: none
        """
        for element in self.context.web_table_fixed_names:
            print(f"Name of {jobs}: {element}")

        self.context.web_table_fixed_names = []
