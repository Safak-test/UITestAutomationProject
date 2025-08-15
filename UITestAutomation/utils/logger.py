import logging
import os
from datetime import datetime
from pathlib import Path

class TestLogger:
    """Custom logger for test automation framework"""
    
    def __init__(self, name="UI_Test_Automation", log_level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)
        
        # Prevent duplicate handlers
        if not self.logger.handlers:
            self._setup_handlers()
    
    def _setup_handlers(self):
        """Setup console and file handlers"""
        # Create logs directory
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        # Create timestamp for log file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = log_dir / f"test_execution_{timestamp}.log"
        
        # File handler
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers to logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def info(self, message):
        """Log info message"""
        self.logger.info(message)
    
    def debug(self, message):
        """Log debug message"""
        self.logger.debug(message)
    
    def warning(self, message):
        """Log warning message"""
        self.logger.warning(message)
    
    def error(self, message):
        """Log error message"""
        self.logger.error(message)
    
    def critical(self, message):
        """Log critical message"""
        self.logger.critical(message)
    
    def log_test_start(self, test_name):
        """Log test start"""
        self.info(f"🚀 Starting test: {test_name}")
    
    def log_test_end(self, test_name, status="PASSED"):
        """Log test end"""
        self.info(f"✅ Test {test_name} {status}")
    
    def log_test_failure(self, test_name, error_message):
        """Log test failure"""
        self.error(f"❌ Test {test_name} FAILED: {error_message}")
    
    def log_browser_action(self, action, details=""):
        """Log browser action"""
        self.debug(f"🌐 Browser Action: {action} {details}")
    
    def log_page_load(self, url):
        """Log page load"""
        self.debug(f"📄 Loading page: {url}")
    
    def log_element_action(self, action, element_info):
        """Log element action"""
        self.debug(f"🔍 Element Action: {action} on {element_info}")
    
    def log_screenshot(self, screenshot_path):
        """Log screenshot taken"""
        self.debug(f"📸 Screenshot saved: {screenshot_path}")
    
    def log_configuration(self, config_info):
        """Log configuration information"""
        self.info(f"⚙️ Configuration: {config_info}")
    
    def log_performance(self, operation, duration):
        """Log performance metrics"""
        self.info(f"⏱️ Performance: {operation} took {duration:.2f} seconds")

# Global logger instance
logger = TestLogger()
