
from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
         assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not present"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_MAIL), "Form for login is not present" #and  self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD))


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_MAIL) ,  "Form for registration is not present"  #and self.is_element_present(*LoginPageLocators.REG_PASSWORD) and (*LoginPageLocators.REG_PASSWORD_REP)), "Form for registration is not present"



    def register_new_user(self, email, password):

        login_link = self.browser.find_element(*LoginPageLocators.REG_MAIL)
        login_link.click()
        login_link.send_keys(email)
        login_link = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        login_link.click()
        login_link.send_keys(password)
        login_link = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_REP)
        login_link.click()
        login_link.send_keys(password)
        login_link = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        login_link.click()