from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import csv

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = Chrome()
        cls.driver.get('https://practicetestautomation.com/practice-test-login/')
    
    def test_valid_login(self):
        with open('login_data.csv', newline = '') as f:
            reader = csv.DictReader(f)
            for row in reader:
                user_name = row['username']
                password = row['password']
                expected = row['expected']
                WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located((By.ID, 'username'))).send_keys(user_name)
                WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys(password)
                WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.ID, 'submit'))).click()
                if expected == 'success':
                    self.assertIn('Logged In Successfully', self.driver.title)
                    self.driver.back()
                else:
                    error_msg = self.driver.find_element(By.ID, 'error').text
                    self.assertTrue('Your username is invalid!' in error_msg)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

