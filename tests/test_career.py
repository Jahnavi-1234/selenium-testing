import time
import sys
import os
import pytest
from selenium import webdriver
from configparser import ConfigParser
from base.base_class import BaseClass
from pages.career_page import CareerPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
@pytest.fixture
def driver():
    base = BaseClass()
    yield base.driver  
    base.close_browser()
   # time.sleep(3)
def test_career_page(driver):
    config = ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '..', 'config', 'config.ini'))
    career_url = config.get('URLS', 'career_url')
    driver.get(career_url)
    career_page = CareerPage(driver)
    career_page.click_i_agree_button()
    career_page.search_qa_engineer()
    job_listings = career_page.scroll_and_check_jobs()
    career_page.click_quality_engineer()   
    try:
        job_listings = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@data-category='Quality Engineering']/button/img[@alt=expand]"))
        )
        if len(job_listings) == 1:
            print("There is one job opportunity for QA Engineer")
        elif len(job_listings) > 1:
            print(f"There are {len(job_listings)} job opportunities for QA Engineer")
        else:
            print("There are no job opportunities for QA Engineer")
    except Exception as e:
        print(f"Error while checking job opportunities: {str(e)}")





