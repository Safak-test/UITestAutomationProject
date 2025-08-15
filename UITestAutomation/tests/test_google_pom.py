import pytest
import allure
import datetime
from pages.google_page import GooglePage
from utils.webdriver_factory import WebDriverFactory
from utils.test_data_manager import TestDataManager
from config.config import Config

@allure.epic("Google Search Tests")
@allure.feature("Search Functionality")
class TestGoogleSearchPOM:
    
    @pytest.fixture(scope="function")
    def driver(self):
        """WebDriver fixture using factory pattern"""
        config = Config()
        factory = WebDriverFactory(config)
        driver = factory.create_driver()
        yield driver
        driver.quit()
    
    @pytest.fixture(scope="function")
    def google_page(self, driver):
        """Google page object fixture"""
        return GooglePage(driver)
    
    @pytest.fixture(scope="function")
    def test_data(self):
        """Test data manager fixture"""
        return TestDataManager()
    
    @allure.story("Basic Google Search with POM")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_google_search_pom(self, google_page, test_data):
        """Test basic Google search functionality using Page Object Model"""
        test_start_time = datetime.datetime.now()
        allure.dynamic.description(f"Test started at: {test_start_time}")
        
        # Get test data
        search_query = test_data.get_random_search_query("valid_searches")
        expected_title = test_data.get_expected_result("google_title")
        
        with allure.step("Navigate to Google"):
            google_page.navigate_to()
            assert expected_title in google_page.get_page_title()
        
        with allure.step("Perform search"):
            google_page.search_and_submit(search_query)
            assert google_page.is_search_results_page()
        
        # Add test completion metadata
        test_end_time = datetime.datetime.now()
        test_duration = test_end_time - test_start_time
        allure.attach(
            f"Test Duration: {test_duration}\nStart Time: {test_start_time}\nEnd Time: {test_end_time}",
            name="test_metadata",
            attachment_type=allure.attachment_type.TEXT
        )
    
    @allure.story("Empty Search with POM")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_empty_search_pom(self, google_page, test_data):
        """Test Google search with empty query using POM"""
        test_start_time = datetime.datetime.now()
        
        expected_title = test_data.get_expected_result("google_title")
        
        with allure.step("Navigate to Google"):
            google_page.navigate_to()
        
        with allure.step("Submit empty search"):
            google_page.submit_search()
            assert expected_title in google_page.get_page_title()
            assert google_page.is_google_homepage()
        
        test_end_time = datetime.datetime.now()
        test_duration = test_end_time - test_start_time
        allure.attach(
            f"Test Duration: {test_duration}\nStart Time: {test_start_time}\nEnd Time: {test_end_time}",
            name="test_metadata",
            attachment_type=allure.attachment_type.TEXT
        )
    
    @allure.story("Special Characters Search with POM")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_special_characters_search_pom(self, google_page, test_data):
        """Test Google search with special characters using POM"""
        test_start_time = datetime.datetime.now()
        
        search_query = test_data.get_random_search_query("special_characters")
        
        with allure.step("Navigate to Google"):
            google_page.navigate_to()
        
        with allure.step("Search with special characters"):
            google_page.search_and_submit(search_query)
            assert google_page.is_search_results_page()
        
        test_end_time = datetime.datetime.now()
        test_duration = test_end_time - test_start_time
        allure.attach(
            f"Test Duration: {test_duration}\nStart Time: {test_start_time}\nEnd Time: {test_end_time}",
            name="test_metadata",
            attachment_type=allure.attachment_type.TEXT
        )
    
    @pytest.mark.parametrize("search_query", [
        "Selenium Python",
        "Test Automation",
        "WebDriver",
        "Python Testing"
    ])
    @allure.story("Parametrized Search Tests")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_parametrized_search(self, google_page, search_query):
        """Parametrized test for multiple search queries"""
        test_start_time = datetime.datetime.now()
        
        with allure.step(f"Navigate to Google and search for: {search_query}"):
            google_page.navigate_to()
            google_page.search_and_submit(search_query)
            assert google_page.is_search_results_page()
        
        test_end_time = datetime.datetime.now()
        test_duration = test_end_time - test_start_time
        allure.attach(
            f"Query: {search_query}\nDuration: {test_duration}",
            name="parametrized_test_metadata",
            attachment_type=allure.attachment_type.TEXT
        )
    
    @allure.story("Search Results Validation")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_search_results_validation(self, google_page, test_data):
        """Test search results validation"""
        test_start_time = datetime.datetime.now()
        
        search_query = test_data.get_random_search_query("valid_searches")
        min_results = test_data.get_expected_result("min_results_count")
        
        with allure.step("Perform search and validate results"):
            google_page.navigate_to()
            google_page.search_and_submit(search_query)
            
            results_count = google_page.get_search_results_count()
            assert results_count >= int(min_results), f"Expected at least {min_results} results, got {results_count}"
        
        test_end_time = datetime.datetime.now()
        test_duration = test_end_time - test_start_time
        allure.attach(
            f"Results Count: {results_count}\nDuration: {test_duration}",
            name="results_validation_metadata",
            attachment_type=allure.attachment_type.TEXT
        )
    
    @allure.story("Clear Search Box")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_clear_search_box(self, google_page):
        """Test clearing search box functionality"""
        test_start_time = datetime.datetime.now()
        
        with allure.step("Navigate to Google and enter text"):
            google_page.navigate_to()
            google_page.search("Test query")
            assert google_page.get_search_box_value() == "Test query"
        
        with allure.step("Clear search box"):
            google_page.clear_search_box()
            assert google_page.get_search_box_value() == ""
        
        test_end_time = datetime.datetime.now()
        test_duration = test_end_time - test_start_time
        allure.attach(
            f"Test Duration: {test_duration}",
            name="clear_search_metadata",
            attachment_type=allure.attachment_type.TEXT
        )
