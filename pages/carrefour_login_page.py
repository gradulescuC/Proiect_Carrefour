from time import sleep
from pages.base_page import Base_page
from selenium.webdriver.common.by import By

class Login_page(Base_page):

    LOGIN_PAGE = "https://www.carrefour.ro/customer/account/login"
    EMAIL_ADDRESS = (By.XPATH, '//input[@name="login[credentials]"]')
    PASSWORD = (By.XPATH,'//input[@name="login[password]"]')
    LOGIN_BUTTON = (By.ID, "send2")

    def navigate_to_loginpage(self):
        self.chrome.get(*self.LOGIN_PAGE)

    def enter_any_username(self,username):
        self.chrome.find_element(*self.EMAIL_ADDRESS).send_keys(username)

    def enter_any_password(self,password):
        self.chrome.find_element(*self.PASSWORD).send_keys(password)

    def click_on_login_button(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()

    def login_succesfuly(self):
        current_url = self.chrome.current_url
        assert "customer/account" in current_url, f"Error: expected url to contain customer/account. Actual url: {current_url}"



