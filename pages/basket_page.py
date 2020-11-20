
from .base_page import BasePage

from .locators import BasketPageLocators

class BasketPage(BasePage):

    def fined_empty_basket(self):
        login_link = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        print(login_link)
        return (login_link)


    def should_not_product_in_the_basket(self):
        assert self.is_disappeared(*BasketPageLocators.PRODUCT_IN_BASKET),"Product is presented, but should not be"

    def should_be_text_about_empty_basket(self):
        EXPECTED_TEXT = "Your basket is empty. Continue shopping"
        self.fined_empty_basket()
        assert self.fined_empty_basket() == EXPECTED_TEXT , "Basket not empty"