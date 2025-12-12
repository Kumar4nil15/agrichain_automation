from locators.result_locators import ResultLocators

class ResultPage:

    def __init__(self, driver):
        self.driver = driver

    def get_result(self):
        return self.driver.find_element(*ResultLocators.RESULT_TEXT).text
