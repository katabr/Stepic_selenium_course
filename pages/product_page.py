import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import LoginPageLocators
from .login_page import LoginPage
from pages.locators import ProductPageLocators



class PageObject(BasePage):

    def add_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        login_link.click()

    def fined_name_book(self):
        login_link = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        print(login_link)


    def expected_name_book(self):
        login_link = self.browser.find_element(*ProductPageLocators.EXPECTED_NAME_BOOK).text
        print(login_link)

    def fined_prise(self):
        login_link = self.browser.find_element(*ProductPageLocators.PRISE).text
        print(login_link)


    def expected_prise(self):
        login_link = self.browser.find_element(*ProductPageLocators.EXPECTED_PRISE).text
        print(login_link)
        



    def test_guest_can_put_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        login_page = page.go_to_login_page()
        login_page.should_be_login_page()