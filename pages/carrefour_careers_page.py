from pages.base_page import Base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Careers_page(Base_page):

    CITY_BOX = (By.XPATH, '//select[@name="city" and @id="city"]')
    STORE_BOX = (By.XPATH, '//select[@name="store" and @id="store"]')
    SEARCH_JOB_BUTTON = (By.XPATH, '//button[@type="submit"]')

    def choose_city_from_city_box(self, alege_oras):
       category_dropdown = Select(self.chrome.find_element(*self.CITY_BOX))
       category_dropdown.select_by_visible_text(alege_oras)

    def choose_store_from_city_box(self, alege_magazin):
        category_dropdown = Select(self.chrome.find_element(*self.STORE_BOX))
        category_dropdown.select_by_visible_text(alege_magazin)

    def click_search_job_button(self):
        self.chrome.find_element(*self.SEARCH_JOB_BUTTON).click()
