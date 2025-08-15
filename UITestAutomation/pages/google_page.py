from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import allure
import time

class GooglePage(BasePage):
    """Page Object for Google Search Page"""
    
    # Locators
    SEARCH_BOX = (By.NAME, "q")
    SEARCH_BUTTON = (By.NAME, "btnK")
    FEELING_LUCKY_BUTTON = (By.NAME, "btnI")
    GOOGLE_LOGO = (By.ID, "hplogo")
    SEARCH_RESULTS = (By.ID, "search")
    FIRST_RESULT = (By.CSS_SELECTOR, "#search .g:first-child h3")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.google.com"
    
    def navigate_to(self):
        """Navigate to Google homepage"""
        with allure.step("Navigate to Google homepage"):
            self.driver.get(self.url)
            self.wait_for_page_load()
            self.take_screenshot("google_homepage")
    
    def search(self, query):
        """Perform a search with the given query"""
        with allure.step(f"Search for: {query}"):
            self.send_keys(self.SEARCH_BOX, query)
            self.take_screenshot("search_entered")
    
    def submit_search(self):
        """Submit the search by pressing Enter"""
        with allure.step("Submit search"):
            self.send_keys(self.SEARCH_BOX, Keys.RETURN)
            time.sleep(2)  # Wait for page to load
            self.wait_for_page_load()
            self.take_screenshot("search_results")
    
    def search_and_submit(self, query):
        """Search and submit in one action"""
        self.search(query)
        # Try clicking search button first, then fallback to Enter key
        try:
            self.click_search_button()
        except:
            self.submit_search()
    
    def click_search_button(self):
        """Click the search button"""
        with allure.step("Click search button"):
            self.click(self.SEARCH_BUTTON)
            time.sleep(2)  # Wait for page to load
            self.wait_for_page_load()
            self.take_screenshot("search_results")
    
    def click_feeling_lucky(self):
        """Click the 'I'm Feeling Lucky' button"""
        with allure.step("Click 'I'm Feeling Lucky' button"):
            self.click(self.FEELING_LUCKY_BUTTON)
            self.wait_for_page_load()
            self.take_screenshot("feeling_lucky_result")
    
    def get_search_results_count(self):
        """Get the number of search results"""
        try:
            # Try different selectors for search results
            selectors = [
                "#search .g",
                "#search .rc",
                ".g",
                ".rc",
                "[data-sokoban-container] .g",
                ".MjjYud"
            ]
            
            for selector in selectors:
                try:
                    results = self.find_elements((By.CSS_SELECTOR, selector))
                    if results:
                        return len(results)
                except:
                    continue
            
            return 0
        except:
            return 0
    
    def get_first_result_title(self):
        """Get the title of the first search result"""
        try:
            return self.get_text(self.FIRST_RESULT)
        except:
            return None
    
    def click_first_result(self):
        """Click on the first search result"""
        with allure.step("Click first search result"):
            self.click(self.FIRST_RESULT)
            self.wait_for_page_load()
            self.take_screenshot("first_result_clicked")
    
    def is_search_results_page(self):
        """Check if we're on search results page"""
        current_url = self.get_current_url().lower()
        return "search" in current_url or "q=" in current_url
    
    def is_google_homepage(self):
        """Check if we're on Google homepage"""
        return "google.com" in self.get_current_url() and "search" not in self.get_current_url().lower()
    
    def clear_search_box(self):
        """Clear the search box"""
        with allure.step("Clear search box"):
            self.send_keys(self.SEARCH_BOX, Keys.CONTROL + "a")
            self.send_keys(self.SEARCH_BOX, Keys.DELETE)
    
    def get_search_box_value(self):
        """Get the current value in search box"""
        element = self.find_element(self.SEARCH_BOX)
        return element.get_attribute("value")
