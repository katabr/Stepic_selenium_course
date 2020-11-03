import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage
from .basket_page import BasketPage
from .locators import ProductPageLocators



class PageObject(BasePage):

    def add_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        login_link.click()

    def fined_name_book(self):
        login_link = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        print(login_link)
        return (login_link)


    def expected_name_book(self):
        login_link = self.browser.find_element(*ProductPageLocators.EXPECTED_NAME_BOOK).text
        print(login_link)
        return (login_link)

    def fined_prise(self):
        login_link = self.browser.find_element(*ProductPageLocators.PRISE).text
        print(login_link)
        return (login_link)


    def expected_prise(self):
        login_link = self.browser.find_element(*ProductPageLocators.EXPECTED_PRISE).text
        print(login_link)
        return (login_link)


    # метод-проверка, что элемент отсутствует
    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is presented"

    # метод-проверка, для элемента, который не появляется некоторое время
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is presented, but should not be"

    # метод-проверка, для элемента, который был, но исчезает
    def should_not_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
