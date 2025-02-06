from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
class CareerPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_jobs_field = (By.ID, "search-input")  
        self.job_results = (By.CLASS_NAME, "filter-label")  
        self.i_agree_button = (By.ID, "onetrust-accept-btn-handler")
    def click_i_agree_button(self):
        try:
            i_agree_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.i_agree_button)
            )
            i_agree_button.click()
            print("Clicked on 'I agree' button.")
        except Exception as e:
            print(f"Error while clicking 'I agree' button: {str(e)}")
          #  time.sleep(3)
    def search_qa_engineer(self):
        try:
            search_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.search_jobs_field)
            )
            search_field.clear()
            print("Typing 'QA Engineer' into the search field...")
            search_field.send_keys("QA Engineer")
            search_field.send_keys(Keys.RETURN)
            time.sleep(3)
            print("Search for 'QA Engineer' submitted.")
        except Exception as e:
            print(f"Error in searching for QA Engineer: {str(e)}")
    def scroll_and_check_jobs(self):
        try:
            self.driver.execute_script("window.scrollTo(0, 400);")
            print("Scrolled down 400 pixels.")
            job_listings = self.driver.find_elements(By.CLASS_NAME, "filter-label")
            return job_listings
        except Exception as e:
            print(f"Error while scrolling and checking jobs: {str(e)}")
            return []
        
    def click_quality_engineer(self):
        try:
            quality_engineer = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@data-category='Quality Engineering']/button/img[@alt='expand']"))
            )
            quality_engineer.click()
            print("Clicked on 'QUALITY ENGINEER (1)'.")
        except Exception as e:
            print(f"Error clicking on 'QUALITY ENGINEER (1)': {str(e)}")
def count_quality_engineer_jobs(self):
    try:
        job_opportunities = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "job-listing"))
        )
        return len(job_opportunities)
    except Exception as e:
        print(f"Error while counting job opportunities: {str(e)}")
        return 0
def verify_job_opportunities(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.job_results)
        )
        return self.driver.find_elements(*self.job_results)