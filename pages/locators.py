from selenium.webdriver.common.by import By


class MainPageLocators():
    pass
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_BLOCK = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_BLOCK = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_REPEAT_BLOCK = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > .btn:first-child")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_SET = (By.CSS_SELECTOR, "#basket_formset")
    MESSAGE_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
