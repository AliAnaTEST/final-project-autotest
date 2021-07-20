from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SET), \
           "Products are in basket, but should not be"

    def should_be_message_if_empty_basket(self):
        message = self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY).text
        print(message)
        assert message == "Your basket is empty. Continue shopping", "Error message when basket is empty"
