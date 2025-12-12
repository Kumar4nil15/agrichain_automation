from locators.home_locators import HomeLocators

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://agrichain.com")

    def enter_text(self, text):
        self.driver.find_element(*HomeLocators.INPUT).send_keys(text)

    def click_submit(self):
        self.driver.find_element(*HomeLocators.SUBMIT).click()

