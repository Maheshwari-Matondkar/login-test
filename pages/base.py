from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def click(self, locator):
        ele = WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located(locator)).send_keys(text)
    
    def get_text(self, locator):
        return WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located(locator)).text

    