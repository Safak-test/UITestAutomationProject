import os
import json
from pathlib import Path

class Config:
    """Configuration management for the test framework"""
    
    def __init__(self, environment="local"):
        self.environment = environment
        self.config_data = self._load_config()
    
    def _load_config(self):
        """Load configuration from JSON file"""
        config_file = Path(__file__).parent / f"config_{self.environment}.json"
        
        if config_file.exists():
            with open(config_file, 'r') as f:
                return json.load(f)
        else:
            # Default configuration
            return {
                "browser": {
                    "name": "chrome",
                    "headless": False,
                    "implicit_wait": 10,
                    "page_load_timeout": 30,
                    "window_size": "1920,1080"
                },
                "urls": {
                    "base_url": "https://www.google.com",
                    "test_url": "https://www.google.com"
                },
                "timeouts": {
                    "implicit_wait": 10,
                    "explicit_wait": 10,
                    "page_load": 30
                },
                "screenshots": {
                    "on_failure": True,
                    "on_success": False,
                    "screenshot_dir": "screenshots"
                },
                "reports": {
                    "html": True,
                    "allure": True,
                    "json": False,
                    "xml": False
                },
                "parallel": {
                    "enabled": False,
                    "workers": "auto"
                }
            }
    
    @property
    def browser_name(self):
        return self.config_data["browser"]["name"]
    
    @property
    def browser_headless(self):
        return self.config_data["browser"]["headless"]
    
    @property
    def browser_implicit_wait(self):
        return self.config_data["browser"]["implicit_wait"]
    
    @property
    def browser_page_load_timeout(self):
        return self.config_data["browser"]["page_load_timeout"]
    
    @property
    def browser_window_size(self):
        return self.config_data["browser"]["window_size"]
    
    @property
    def base_url(self):
        return self.config_data["urls"]["base_url"]
    
    @property
    def test_url(self):
        return self.config_data["urls"]["test_url"]
    
    @property
    def implicit_wait(self):
        return self.config_data["timeouts"]["implicit_wait"]
    
    @property
    def explicit_wait(self):
        return self.config_data["timeouts"]["explicit_wait"]
    
    @property
    def page_load_timeout(self):
        return self.config_data["timeouts"]["page_load"]
    
    @property
    def screenshot_on_failure(self):
        return self.config_data["screenshots"]["on_failure"]
    
    @property
    def screenshot_on_success(self):
        return self.config_data["screenshots"]["on_success"]
    
    @property
    def screenshot_dir(self):
        return self.config_data["screenshots"]["screenshot_dir"]
    
    @property
    def html_reports_enabled(self):
        return self.config_data["reports"]["html"]
    
    @property
    def allure_reports_enabled(self):
        return self.config_data["reports"]["allure"]
    
    @property
    def parallel_enabled(self):
        return self.config_data["parallel"]["enabled"]
    
    @property
    def parallel_workers(self):
        return self.config_data["parallel"]["workers"]
    
    def get_browser_options(self):
        """Get browser-specific options"""
        if self.browser_name.lower() == "chrome":
            from selenium.webdriver.chrome.options import Options
            options = Options()
            
            if self.browser_headless:
                options.add_argument("--headless")
            
            options.add_argument(f"--window-size={self.browser_window_size}")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-extensions")
            
            return options
        
        elif self.browser_name.lower() == "firefox":
            from selenium.webdriver.firefox.options import Options
            options = Options()
            
            if self.browser_headless:
                options.add_argument("--headless")
            
            return options
        
        else:
            return None
