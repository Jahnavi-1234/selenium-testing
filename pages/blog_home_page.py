from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BlogHomePage:
    """Page Object Model for the Blog Home Page"""

    # Locators
    BTN_I_AGREE = (By.XPATH, "//button[contains(text(),'I agree')]")
    BTN_MENU = (By.CLASS_NAME, "primary-menu__burger")
    BTN_GET_IN_TOUCH = (By.XPATH, "//*[contains(text(),'Get in touch')]")

    def __init__(self, driver, timeout=10):
        """Initialize the BlogHomePage object with a WebDriver instance"""
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_blog_homepage(self, url="https://blog.griddynamics.com"):
        """Opens the blog homepage"""
        self.driver.get(url)

    def click_agree_button(self):
        """Clicks the 'I Agree' button if it appears"""
        try:
            agree_button = self.wait.until(EC.element_to_be_clickable(self.BTN_I_AGREE))
            agree_button.click()
            print("✅ 'I Agree' button clicked successfully.")
        except Exception:
            print("⚠️ No 'I Agree' button found, skipping.")

    def click_get_in_touch(self, expected_url="https://blog.griddynamics.com/contact-us/"):
        """Clicks the 'Get in Touch' button and verifies redirection"""
        try:
            button = self.wait.until(EC.element_to_be_clickable(self.BTN_GET_IN_TOUCH))
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", button)
            button.click()
            print("✅ 'Get in Touch' button clicked successfully.")

            # Wait for redirection to complete
            WebDriverWait(self.driver, 10).until(EC.url_contains("contact"))
            assert expected_url in self.driver.current_url, "❌ Redirection failed!"
            print(f"✅ Successfully redirected to Contact Us page: {self.driver.current_url}")

        except Exception as e:
            print(f"⚠️ Error clicking 'Get in Touch' button: {e}")

    def open_menu(self):
        """Opens the menu if it's available"""
        try:
            menu_button = self.wait.until(EC.visibility_of_element_located(self.BTN_MENU))
            menu_button.click()
            print("✅ Menu button clicked successfully.")
        except Exception:
            print("⚠️ Menu button not found or not clickable.")

    def scroll_and_click(self, locator):
        """Scrolls to an element, waits for visibility, and clicks it"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
            self.wait.until(EC.element_to_be_clickable(locator)).click()
            print("✅ Element clicked successfully.")
        except Exception:
            print("⚠️ Failed to click the element.")

    def wait_for_element(self, locator, condition=EC.element_to_be_clickable):
        """Waits for an element based on a given condition"""
        try:
            return self.wait.until(condition(locator))
        except Exception:
            print(f"⚠️ Element {locator} not found.")
            return None


