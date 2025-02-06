from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import BaseClass
import time

class ContactUsPage(BaseClass):
    TXT_FNAME = (By.XPATH, "//input[@name='first_name']")
    TXT_LNAME = (By.XPATH, "//input[@name='last_name']")
    TXT_EMAIL = (By.XPATH, "//input[@name='email']")

    def __init__(self, driver, timeout=30):
        """Initialize the BlogHomePage object with a WebDriver instance"""
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def fill_contact_form(self, first_name, last_name, email):
        first_name_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.TXT_FNAME)  # Wait until the field is clickable
        )
        first_name_field.clear()
        first_name_field.send_keys(first_name) 
        time.sleep(1)
       #  WebDriverWait(self.driver, 10)

        
        last_name_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.TXT_LNAME)  # Wait until the field is clickable
        )
        last_name_field.clear() 
        last_name_field.send_keys(last_name)
        time.sleep(1)
       #  WebDriverWait(self.driver, 10)

        email_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.TXT_EMAIL)  # Wait until the field is clickable
        )
        email_field.clear() 
        email_field.send_keys(email)
        time.sleep(1)
       #  WebDriverWait(self.driver, 70)

    def select_media_inquiry(self):
        dropdown = self.driver.find_element(By.CLASS_NAME, "get-in-touch-form__dropdown-current")
        dropdown.click()
        time.sleep(1)
        # WebDriverWait(self.driver, 4)
        options = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Media inquiry')]")
        self.driver.execute_script("window.scrollTo(0, 200);")
        options.click()
        time.sleep(1)
        # WebDriverWait(self.driver, 10)

    def accept_terms(self):
        checkbox1 = self.driver.find_element(By.NAME, "terms")
        self.driver.execute_script("arguments[0].click();", checkbox1)
        time.sleep(1)
       #  WebDriverWait(self.driver, 10)

    def submit_form(self):
        submit_button = self.driver.find_element(By.XPATH, "//input[@value='Submit']")
        if submit_button.get_attribute("disabled") == "true":
            print("The submit button is inactive.")
        else:
            print("The submit button is active.")
            time.sleep(1)
       #  WebDriverWait(self.driver, 10)



# dropdown = driver.find_element(By.CLASS_NAME, "get-in-touch-form__dropdown-current")
# dropdown.click()
# options = driver.find_element(By.XPATH, "//div[contains(text(), 'Media inquiry')]")
# driver.execute_script("window.scrollTo(0, 200);")
# options.click()
# time.sleep(1)

# checkbox1 = driver.find_element(By.NAME, "terms")  

# driver.execute_script("arguments[0].click();", checkbox1)
# time.sleep(2)

# submit_button = driver.find_element(By.XPATH, "//input[@value='Submit']")  # Replace with actual class name
# if submit_button.get_attribute("disabled") == "true":
#     print("The submit button is inactive.")
# else:
#     print("The submit button is active.")



