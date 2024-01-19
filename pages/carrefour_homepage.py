from time import sleep
from pages.base_page import Base_page
from selenium.webdriver.common.by import By


class Home_page(Base_page):

    HOMEPAGE = "https://www.carrefour.ro/"
    SEARCH_BOX = (By.ID, "search")
    SEARCH_BUTTON = (By.XPATH, '//button[@class="form-submit"]')
    SEARCH_RESULTS = (By.XPATH, '//span[@class="base"]/span')
    LOGIN_BUTTON = (By.XPATH, '//a[@title="login"]')
    MY_BASKET_BUTTON = (By.XPATH, '//a[@role="button" and @title="minicart"]')
    CAREERS_LINK = (By.XPATH, '//a[@href= "/corporate/cariere" and @title="Cariere">Ca]')
    ADD_TO_SHOPPING_CART_BUTTON = (By.XPATH,'//button[@title="Adauga in cos"][1]')

    def navigate_to_homepage(self):
        self.chrome.get(self.HOMEPAGE)

    def insert_search_value(self, product_name):
        self.chrome.find_element(*self.SEARCH_BOX).send_keys(product_name)

    def click_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()

    def check_search_results(self, results_number):
        no_results = self.chrome.find_element(*self.SEARCH_RESULTS).text
        result = no_results[:no_results.index(" ")]
        assert int(result) >= int(results_number), f"ERROR: Results Number is incorrect. EXPECTED: {results_number}, ACTUAL {result}"

    def click_on_login_button(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()

    def click_my_basket_button(self):
        self.chrome.find_element(*self.MY_BASKET_BUTTON).click()

    def click_on_carers_link(self):
        self.chrome.find_element(*self.CAREERS_LINK).click()

    def click_account_button(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()

    def navigate_to_login_page(self):
        current_url = self.chrome.current_url
        assert "login" in current_url, f"Error: expected url to contain login. Actual URL: {current_url}"

    def add_product_to_shopping_cart(self):
        self.chrome.find_element(*self.ADD_TO_SHOPPING_CART_BUTTON).click()






































