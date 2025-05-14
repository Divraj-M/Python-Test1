from selenium.webdriver.common.by import By
import pytest
from page.HomePage import HomePage
from page.SearchPage import SearchPage
from Utilities import console

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_valid_product(self):
        log=console.get_logger()
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box("HP")
        log.info("Entering product name into search box")
        home_page.click_search_button()
        log.info("Clicking search button")
        search_page = SearchPage(self.driver)
        search_page.display_status_of_valid_product()
        log.info("Validating product display status")
        