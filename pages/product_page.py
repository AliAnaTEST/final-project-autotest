from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
import time


class ProductPage(BasePage):

	def should_add_product_to_basket(self):
		product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
		product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
		self.add_product_to_basket()
		self.solve_quiz_and_get_code()
		self.check_product_name_in_message(product_name)
		self.check_product_price_in_message(product_price)

	def solve_quiz_and_get_code(self):
		try:
			alert = self.browser.switch_to.alert
			x = alert.text.split(" ")[2]
			answer = str(math.log(abs((12 * math.sin(float(x))))))
			alert.send_keys(answer)
			alert.accept()
		except NoAlertPresentException:
			print("No first alert presented")
			try:
				alert = self.browser.switch_to.alert
				alert_text = alert.text
				print(f"Your code: {alert_text}")
				alert.accept()
			except NoAlertPresentException:
				print("No second alert presented")

	def check_product_name_in_message(self, product_name):
	 	product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
	 	assert product_name == product_name_in_message, "Error product name in message"

	def check_product_price_in_message(self, product_price):
		product_price_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE).text
		assert product_price == product_price_in_message, "Error product price in message"

	def add_product_to_basket(self):
		add_product_button = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)
		add_product_button.click()

	def should_not_be_success_message(self):
	    assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
	       "Success message is presented, but should not be"

	def should_be_disappeared_message(self):
	    assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
	       "Message is still presented, but should not be"
