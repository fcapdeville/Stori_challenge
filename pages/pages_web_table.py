from locators.locators_web_table import LocatorsWebTable


class PagesWebTable:
    def __init__(self, context):
        self.context = context

    def collect_courses_and_price(self, cost):
        """
        Scenario: Web Table - Collect number of courses that cost ${cost} and their names
        :param cost: str - '25' or '15'
        :return: none
        """
        # region Collect table data
        table = self.context.driver.find_element(*LocatorsWebTable.table_locator)
        rows = table.find_elements(*LocatorsWebTable.rows_locator)
        # endregion

        # region collect price and name
        for row in rows[1:]:  # Avoid first row
            price = row.find_element(*LocatorsWebTable.price_locator).text
            if price == cost:
                course_name = row.find_element(*LocatorsWebTable.course_name_locator).text
                self.context.web_table_names.append(course_name)
        # endregion

    def print_courses_and_names(self):
        """
        Scenario: Web Table - Print number of courses and their names
        :return: none
        """
        print(f"Number of courses: {len(self.context.web_table_names)}")

        for element in self.context.web_table_names:
            print(f"Course associated: {element}")

        self.context.web_table_names = []
