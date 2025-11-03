from selenium.webdriver.common.by import By


class Locators:
    user_name = (By.NAME, 'username')
    password = (By.NAME, 'password')
    submit_btn = (By.ID, 'submit')
    login_text = (By.CLASS_NAME, 'post-title')
    logout_btn = (By.LINK_TEXT, 'Log out')
    login_error = (By.ID, 'error')