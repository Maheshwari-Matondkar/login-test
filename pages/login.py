from base import BasePage
from locators import Locators
from data import user1, pass1, user2, pass2, url

class Login(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)
    
    def open(self):
        self.open_url(url)

    def login(self, user_name, password):
        self.enter_text(Locators.user_name, user_name)
        self.enter_text(Locators.password, password)
        self.click(Locators.submit_btn)
    
    def valid_login(self):
        self.login(user1, pass1)
        return self.get_text(Locators.login_text)

    def logout(self):
        self.click(Locators.logout_btn)

    def invalid_login(self):
        self.login(user2, pass2)
        return self.get_text(Locators.login_error)
    