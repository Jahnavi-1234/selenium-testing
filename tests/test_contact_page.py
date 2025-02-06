import pytest
import os
from configparser import ConfigParser
from base.base_class import BaseClass
from pages.blog_home_page import BlogHomePage
from pages.contact_us_page import ContactUsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    base = BaseClass()
    yield base.driver  
    base.close_browser()

def test_blog_home_page(driver):
    """Test navigating from Blog to Contact Us and filling the form including dropdown selection."""
    
    config = ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '..', 'config', 'config.ini'))
    blog_url = config.get('URLS', 'blog_url')

    driver.get(blog_url)
    blog_home_page = BlogHomePage(driver)
    blog_home_page.click_agree_button()
    blog_home_page.click_get_in_touch()

    contact_us_page = ContactUsPage(driver)
    contact_us_page.fill_contact_form("Anna", "Smith", "annasmith@griddynamics.com")  
    
    # Wait for the dropdown to become clickable
    dropdown_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "get-in-touch-form__dropdown-current"))
    )
    dropdown_element.click()

    # Wait for the 'Media inquiry' option to be clickable
    media_inquiry_option = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Media inquiry')]"))
    )
    media_inquiry_option.click()

    # Optionally, scroll down if needed
    driver.execute_script("window.scrollTo(0, 200);")
    time.sleep(1)

    # Accept the terms and conditions
    contact_us_page.accept_terms()

    # Assert if the submit button is enabled
    assert contact_us_page.is_submit_button_enabled(), "❌ Submit button should be active!"
