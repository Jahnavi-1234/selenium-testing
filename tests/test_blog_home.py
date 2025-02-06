import sys
import os
import pytest
from configparser import ConfigParser
from base.base_class import BaseClass
from pages.blog_home_page import BlogHomePage
from pages.contact_us_page import ContactUsPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

@pytest.fixture
def driver():
    base = BaseClass()
    yield base.driver  
    base.close_browser()

def test_blog_home_page(driver):
    config = ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '..', 'config', 'config.ini'))
    
    blog_url = config.get('URLS', 'blog_url')
    contact_url = config.get('URLS', 'contact_us_url')  # Ensure correct contact page URL

    # Navigate to Blog Home Page
    driver.get(blog_url)
    blog_home_page = BlogHomePage(driver)
    contact_us_page = ContactUsPage(driver)

    # Interact with Blog Home Page
    blog_home_page.click_agree_button()
    blog_home_page.click_get_in_touch(contact_url)

    # Ensure we are on the correct Contact Us page
    assert "griddynamics.com/contact" in driver.current_url, f"❌ Contact Us page did not open! Got: {driver.current_url}"
    contact_us_page.fill_contact_form("Anna", "Smith", "annasmith@griddynamics.com")
    contact_us_page.select_media_inquiry()
    contact_us_page.accept_terms()
    contact_us_page.submit_form()
