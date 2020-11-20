import pytest

import time

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.product_page import PageObject



@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = PageObject(browser, link)
    page.open()
    page.add_to_basket()
    assert page.should_not_be_success_message() == True

@pytest.mark.skip
@pytest.mark.xfail

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = PageObject(browser, link)
    page.open()
    assert page.should_not_be_success_message() == True



@pytest.mark.skip
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = PageObject(browser,link)
    page.open()
    page.add_to_basket()
    assert page.should_not_be_disappeared()== True


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()




@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_basket()
    basket = BasketPage(browser, link)
    basket.should_not_product_in_the_basket()
    basket.should_be_text_about_empty_basket()

@pytest.mark.need_review
#@pytest.mark.skip
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

def test_guest_can_add_product_to_basket(browser,link):
    #link = "http: // selenium1py.pythonanywhere.com / catalogue / coders - at - work_207 /?promo = newYear2019"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = PageObject(browser, link)
    page.open()

    expected_name_book = page.expected_name_book()
    expected_prise = page.expected_prise()

    page.add_to_basket()
    page.solve_quiz_and_get_code()  # расчет
    time.sleep(1)

    name_book = page.fined_name_book()
    prise = page.fined_prise()

    page.should_be_name_book_equivalent_expected_name_book(name_book, expected_name_book)
    page.should_be_prise_equivalent_expected_prise(prise, expected_prise)



@pytest.mark.user
class TestUserAddToBasketFromProductPage(object):
    @pytest.fixture(scope="function",  autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        self.page = PageObject(browser, link)
        self.page.open()

        self.page.go_to_login_page()
        password = str(time.time())
        email = str(time.time()) + "@fakemail.org"
        self.login = LoginPage(browser,link)
        self.login.register_new_user(email,password)
        self.page.should_be_authorized_user()

    #@pytest.mark.skip
    #@pytest.mark.xfail
    #@pytest.mark.skip
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = PageObject(browser, link)
        page.open()
        page.should_not_be_success_message()


    @pytest.mark.need_review
    #@pytest.mark.skip
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = PageObject(browser, link)
        page.open()

        expected_name_book = page.expected_name_book()
        expected_prise = page.expected_prise()

        page.add_to_basket()
        # page.solve_quiz_and_get_code()  # расчет


        name_book = page.fined_name_book()
        prise = page.fined_prise()

        page.should_be_name_book_equivalent_expected_name_book(name_book, expected_name_book)
        page.should_be_prise_equivalent_expected_prise(prise, expected_prise)



