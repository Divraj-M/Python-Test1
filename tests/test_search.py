from selenium.webdriver.common.by import By
import pytest

from pages.Homepage import HomePage
from pages.Searchpage import SearchPage

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_valid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box("HP")
        home_page.click_search_button()
        search_page = SearchPage(self.driver)
        assert search_page.display_status_of_valid_product() == True