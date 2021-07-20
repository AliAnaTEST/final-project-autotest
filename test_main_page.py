from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from selenium.webdriver.common.by import By
import time


def go_to_basket_page(browser):
    link = browser.find_element(By.CSS_SELECTOR, ".btn-group > .btn:first-child")
    link.click()
    return BasketPage(browser=browser, url=browser.current_url) 

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    basket_page = go_to_basket_page(browser)
    basket_page.should_not_be_products_in_empty_basket()
    basket_page.should_be_message_if_empty_basket()
