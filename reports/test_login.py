from selenium.webdriver import Chrome
import unittest
from login import Login
from selenium.webdriver.common.by import By
import logging
import HtmlTestRunner
import sys
import os

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Chrome()
        cls.login = Login(cls.driver)
        cls.login.open()
        logging.basicConfig(
                            level = logging.INFO,
                            format = '%(asctime)s - %(levelname)s - %(message)s',
                            stream=sys.stdout)
    
    def test1_valid_login(self):
        logging.info('Valid test case started')
        logged_in_text = self.login.valid_login()
        self.assertIn('Logged In Successfully', logged_in_text)
        self.login.logout()
        assert 'Test Login' in self.driver.title

    def test2_soft_assert(self):
        try:
            self.login.logout()
        except Exception as e:
            #print('Assertion error is ', e)
            logging.error(f'test case failed {self._testMethodName}')
    
    def test3_invalid_login(self):
        actual_msg = self.login.invalid_login()
        try:
            self.assertEqual('Your username is invalid!', actual_msg), f'exected: Your username is invalid! but got {actual_msg}'
        except AssertionError as e:
            print('assertion error is: ', e)

    def test4_assertisnone(self):
        optional_text = None
        try:
            optional_text = self.driver.find_element(By.ID, 'q')
        except:
            pass
        self.assertIsNone(optional_text)
    
    def tearDown(self):
        if self._outcome.result.errors:
            os.makedirs("screenshots", exist_ok=True)
            ss_name = f'screenshots/{self._testMethodName}_failure.png'
            self.driver.save_screenshot(ss_name)
            print(f'test failed: {ss_name}')
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        logging.info('testing complete')

if __name__ == '__main__':
    unittest.main(
        testRunner= HtmlTestRunner.HTMLTestRunner(
            output='reports',
            report_name='LoginTestReport',
            verbosity=2
        )
    )

