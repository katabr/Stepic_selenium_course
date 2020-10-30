import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from pages.product_page import PageObject

from pages.locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException

#1 вариант
# @pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", "7", "8", "9"])
# def test_guest_can_add_product_to_basket(browser, promo_offer):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"


# 2 вариант
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"

    page = PageObject(browser,link)
    page.open()

    expected_name_book = page.expected_name_book()
    expected_prise = page.expected_prise()

    page.add_to_basket()
    page.solve_quiz_and_get_code()# расчет
    time.sleep(1)

    name_book = page.fined_name_book()
    prise = page.fined_prise()



    assert name_book == expected_name_book, "Name book doesn't match the expected "
    assert prise == expected_prise, "Prise doesn't match the expected"



    #name_book = div.col - sm - 6:nth - child(2) > h1.text




    # ПРОВЕРКИ  ТОВАР В КОЗИНЕ сообщение о добавлении strong The shellcoder's handbook has been added to your basket.
    #
    #
    #text Your basket total is now £9.99
    #
    #
    #
    #
# СТОИМОСТЬ СОВПАДАЕТ С ЦЕНОЙ   цена в корзине



    # link = "http://selenium1py.pythonanywhere.com"
    # page = MainPage(browser, link)
    # page.open()
    # login_page = page.go_to_login_page()
    # login_page.should_be_login_page()
    # def test_guest_can_put_to_basket(browser):
    #     link = "http://selenium1py.pythonanywhere.com"
    #     page = MainPage(browser, link)
    #     page.open()
    #     login_page = page.go_to_login_page()
    #     login_page.should_be_login_page()

