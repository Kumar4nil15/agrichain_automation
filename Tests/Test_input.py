from utils.driver_setup import start_browser
from pages.home_page import HomePage
from pages.result_page import ResultPage
import time


def test_valid_input():
    driver = start_browser()

    try:
        home = HomePage(driver)
        result = ResultPage(driver)

        home.open()
        home.enter_text("abcabcbb")
        home.click_submit()

        time.sleep(1)

        output = result.get_result()

        assert output == "3"

    finally:
        driver.quit()


