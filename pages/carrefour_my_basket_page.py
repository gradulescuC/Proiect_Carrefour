from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Base_page
from selenium.webdriver.common.by import By


class My_basket(Base_page):

		SHOPPING_CART_PRODUCT = (By.XPATH,'//div[@class="item-name"]')
		REMOVE_PRODUCT_BUTTON = (By.XPATH,'//div[@class="js-qty-update item-delete"]')
		EMPTY_CART_MESSAGE = (By.XPATH,'//div[@class="alert alert-danger error-message"]/strong')

		def product_should_be_found_in_cart(self):
				is_product_found = False
				try:
						self.chrome.find_element(*self.SHOPPING_CART_PRODUCT)
						is_product_found = True
				except:
						pass

				assert is_product_found == True, "Error, the product was not found into the shopping cart"

		def click_on_remove_button(self):
				remove_product_button = WebDriverWait(self.chrome, 50).until(EC.visibility_of_element_located(self.REMOVE_PRODUCT_BUTTON))
				remove_product_button.click()

		def the_product_is_removed(self):
				is_product_found = True
				try:
						self.chrome.find_element(*self.SHOPPING_CART_PRODUCT)
				except:
						is_product_found = False
				assert is_product_found == False, "Error, the product was not removed from the shopping cart"
				empty_cart_message = self.chrome.find_element(*self.EMPTY_CART_MESSAGE).text
				assert empty_cart_message == 'Nu ai produse adaugate in cos',f"Error: message is not correct. Expected message: Nu ai produse adaugate in cos, actual message: {empty_cart_message}"


