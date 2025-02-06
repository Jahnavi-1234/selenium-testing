from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BaseClass:
    def __init__(self):
        """Initialize WebDriver."""
        self.driver = self.init_driver()

    def init_driver(self):
        """Initialize and return the WebDriver instance."""
        driver = webdriver.Chrome()  # Change to preferred WebDriver
        driver.maximize_window()
        return driver

    def wait(self, timeout=10):
        """Return WebDriverWait instance."""
        return WebDriverWait(self.driver, timeout)

    def wait_for_element(self, by, value, timeout=10):
        """Wait for an element to be present."""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def wait_for_clickable(self, by, value, timeout=10):
        """Wait for an element to be clickable."""
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, value)))

    def close_browser(self):
        """Close the WebDriver instance."""
        if self.driver:
            self.driver.quit()

