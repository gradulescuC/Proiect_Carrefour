from pages.base_page import Base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Careers_page(Base_page):

    CITY_BOX = (By.ID, 'city')
    STORE_BOX = (By.ID, 'store')
    SEARCH_JOB_BUTTON = (By.XPATH, '//button[@type="submit"]')
    JOB_SEARCH_RESULTS = (By.XPATH, '//div[@class="location"]')


    def choose_city_from_city_box(self, alege_oras):
        WebDriverWait(self.chrome, 50).until(EC.presence_of_element_located(self.CITY_BOX))
        city_dropdown = Select(self.chrome.find_element(*self.CITY_BOX))
        city_dropdown.select_by_visible_text(alege_oras)

    def choose_store_from_city_box(self, alege_magazin):
        WebDriverWait(self.chrome, 50).until(EC.presence_of_element_located(self.STORE_BOX))
        store_dropdown = Select(self.chrome.find_element(*self.STORE_BOX))
        store_dropdown.select_by_visible_text(alege_magazin)

    def click_search_job_button(self):
        self.chrome.find_element(*self.SEARCH_JOB_BUTTON).click()

    def check_job_search_results(self, results_number):
        results = self.chrome.find_elements(*self.JOB_SEARCH_RESULTS)
        assert len(results)>=int(results_number), "Error: the number of job results is incorrect"
