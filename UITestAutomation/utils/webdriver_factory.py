from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from config.config import Config
import os

class WebDriverFactory:
    """Factory class for creating WebDriver instances"""
    
    def __init__(self, config: Config):
        self.config = config
        self.driver = None
    
    def create_driver(self, browser_name=None):
        """Create and return a WebDriver instance"""
        if browser_name is None:
            browser_name = self.config.browser_name
        
        browser_name = browser_name.lower()
        
        if browser_name == "chrome":
            return self._create_chrome_driver()
        elif browser_name == "firefox":
            return self._create_firefox_driver()
        elif browser_name == "edge":
            return self._create_edge_driver()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
    
    def _create_chrome_driver(self):
        """Create Chrome WebDriver"""
        options = self.config.get_browser_options()
        
        # Use webdriver-manager for automatic driver management
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        
        self._configure_driver(driver)
        return driver
    
    def _create_firefox_driver(self):
        """Create Firefox WebDriver"""
        options = self.config.get_browser_options()
        
        # Use webdriver-manager for automatic driver management
        service = FirefoxService(GeckoDriverManager().install())
        
        driver = webdriver.Firefox(service=service, options=options)
        self._configure_driver(driver)
        
        return driver
    
    def _create_edge_driver(self):
        """Create Edge WebDriver"""
        options = self.config.get_browser_options()
        
        # Use webdriver-manager for automatic driver management
        service = EdgeService(EdgeChromiumDriverManager().install())
        
        driver = webdriver.Edge(service=service, options=options)
        self._configure_driver(driver)
        
        return driver
    
    def _configure_driver(self, driver):
        """Configure driver with common settings"""
        # Set timeouts
        driver.implicitly_wait(self.config.browser_implicit_wait)
        driver.set_page_load_timeout(self.config.browser_page_load_timeout)
        
        # Maximize window if not headless
        if not self.config.browser_headless:
            driver.maximize_window()
        
        # Set window size if specified
        if self.config.browser_window_size:
            width, height = self.config.browser_window_size.split(',')
            driver.set_window_size(int(width), int(height))
    
    def create_driver_with_capabilities(self, capabilities):
        """Create driver with custom capabilities"""
        browser_name = self.config.browser_name.lower()
        
        if browser_name == "chrome":
            options = self.config.get_browser_options()
            for key, value in capabilities.items():
                options.set_capability(key, value)
            
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
        
        elif browser_name == "firefox":
            options = self.config.get_browser_options()
            for key, value in capabilities.items():
                options.set_capability(key, value)
            
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)
        
        else:
            raise ValueError(f"Custom capabilities not supported for {browser_name}")
        
        self._configure_driver(driver)
        return driver
    
    def create_mobile_driver(self, device_name="iPhone 12"):
        """Create mobile WebDriver (Chrome only)"""
        if self.config.browser_name.lower() != "chrome":
            raise ValueError("Mobile testing is only supported with Chrome")
        
        mobile_emulation = {
            "deviceMetrics": {
                "width": 375,
                "height": 812,
                "pixelRatio": 3.0
            },
            "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
        }
        
        options = self.config.get_browser_options()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        
        return driver
