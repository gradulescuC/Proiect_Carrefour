from time import sleep
from pages.base_page import Base_page
from selenium.webdriver.common.by import By


class My_basket(Base_page):

		SHOPPING_CART_PRODUCT = (By.XPATH,'//div[@class="item-name"]')

		def product_should_be_found_in_cart(self):
				is_product_found = False
				try:
						self.chrome.find_element(*self.SHOPPING_CART_PRODUCT)
						is_product_found = True
				except:
						pass

				assert is_product_found == True, "Error, the product was not found into the shopping cart"
