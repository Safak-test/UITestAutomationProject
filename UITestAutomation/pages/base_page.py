from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import allure
import time

class BasePage:
    """Base page class that all page objects inherit from"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator, timeout=10):
        """Find element with explicit wait"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name=f"element_not_found_{locator[1]}",
                attachment_type=allure.attachment_type.PNG
            )
            raise
    
    def find_elements(self, locator, timeout=10):
        """Find elements with explicit wait"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name=f"elements_not_found_{locator[1]}",
                attachment_type=allure.attachment_type.PNG
            )
            raise
    
    def click(self, locator, timeout=10):
        """Click element with explicit wait"""
        element = self.find_element(locator, timeout)
        try:
            element.click()
        except Exception as e:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name=f"click_failed_{locator[1]}",
                attachment_type=allure.attachment_type.PNG
            )
            raise
    
    def send_keys(self, locator, text, timeout=10):
        """Send keys to element with explicit wait"""
        element = self.find_element(locator, timeout)
        try:
            element.clear()
            element.send_keys(text)
        except Exception as e:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name=f"send_keys_failed_{locator[1]}",
                attachment_type=allure.attachment_type.PNG
            )
            raise
    
    def get_text(self, locator, timeout=10):
        """Get text from element with explicit wait"""
        element = self.find_element(locator, timeout)
        return element.text
    
    def is_element_present(self, locator, timeout=10):
        """Check if element is present"""
        try:
            self.find_element(locator, timeout)
            return True
        except TimeoutException:
            return False
    
    def is_element_visible(self, locator, timeout=10):
        """Check if element is visible"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def wait_for_page_load(self, timeout=30):
        """Wait for page to load completely"""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="page_load_timeout",
                attachment_type=allure.attachment_type.PNG
            )
            raise
    
    def take_screenshot(self, name="screenshot"):
        """Take screenshot and attach to Allure report"""
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
    
    def scroll_to_element(self, locator):
        """Scroll to element"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)  # Small delay for smooth scrolling
    
    def get_current_url(self):
        """Get current URL"""
        return self.driver.current_url
    
    def get_page_title(self):
        """Get page title"""
        return self.driver.title
