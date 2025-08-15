import json
import os
from pathlib import Path
from typing import Dict, List, Any

class TestDataManager:  # noqa: N801
    """Manager for test data operations"""
    
    def __init__(self, data_file="test_data/test_data.json"):
        self.data_file = Path(data_file)
        self.test_data = self._load_test_data()
    
    def _load_test_data(self) -> Dict[str, Any]:
        """Load test data from JSON file"""
        if self.data_file.exists():
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            raise FileNotFoundError(f"Test data file not found: {self.data_file}")
    
    def get_search_queries(self, category: str = "valid_searches") -> List[str]:
        """Get search queries by category"""
        return self.test_data.get("search_queries", {}).get(category, [])
    
    def get_url(self, key: str) -> str:
        """Get URL by key"""
        return self.test_data.get("urls", {}).get(key, "")
    
    def get_expected_result(self, key: str) -> str:
        """Get expected result by key"""
        return self.test_data.get("expected_results", {}).get(key, "")
    
    def get_test_user(self, user_type: str = "valid_user") -> Dict[str, str]:
        """Get test user credentials"""
        return self.test_data.get("test_users", {}).get(user_type, {})
    
    def get_browser_config(self, browser: str) -> Dict[str, Any]:
        """Get browser configuration"""
        return self.test_data.get("browser_configs", {}).get(browser, {})
    
    def get_timeout(self, timeout_type: str = "medium") -> int:
        """Get timeout value by type"""
        return self.test_data.get("timeouts", {}).get(timeout_type, 10)
    
    def get_test_categories(self) -> Dict[str, List[str]]:
        """Get test categories and their test methods"""
        return self.test_data.get("test_categories", {})
    
    def get_tests_by_category(self, category: str) -> List[str]:
        """Get test methods by category"""
        return self.test_data.get("test_categories", {}).get(category, [])
    
    def get_random_search_query(self, category: str = "valid_searches") -> str:
        """Get a random search query from specified category"""
        import random
        queries = self.get_search_queries(category)
        return random.choice(queries) if queries else ""
    
    def get_all_search_queries(self) -> List[str]:
        """Get all search queries from all categories"""
        all_queries = []
        search_queries = self.test_data.get("search_queries", {})
        
        for category in search_queries.values():
            if isinstance(category, list):
                all_queries.extend(category)
        
        return all_queries
    
    def add_test_data(self, key: str, value: Any):
        """Add new test data"""
        if key not in self.test_data:
            self.test_data[key] = value
            self._save_test_data()
    
    def update_test_data(self, key: str, value: Any):
        """Update existing test data"""
        self.test_data[key] = value
        self._save_test_data()
    
    def _save_test_data(self):
        """Save test data to JSON file"""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.test_data, f, indent=4, ensure_ascii=False)
    
    def get_data_for_parametrized_test(self, test_type: str) -> List[Dict[str, Any]]:
        """Get data for parametrized tests"""
        if test_type == "search":
            return [
                {"query": query, "expected": "search"} 
                for query in self.get_search_queries("valid_searches")
            ]
        elif test_type == "special_chars":
            return [
                {"query": query, "expected": "search"} 
                for query in self.get_search_queries("special_characters")
            ]
        else:
            return []
    
    def validate_test_data(self) -> bool:
        """Validate test data structure"""
        required_keys = ["search_queries", "urls", "expected_results"]
        
        for key in required_keys:
            if key not in self.test_data:
                print(f"Missing required key: {key}")
                return False
        
        return True
