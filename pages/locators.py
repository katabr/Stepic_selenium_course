from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators ():
    LOGIN_MAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")

    REG_MAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_REP = (By.CSS_SELECTOR, "#id_registration-password2")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

    EXPECTED_PRISE = (By.CSS_SELECTOR, "p.price_color")
    PRISE = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong") #p.price_color")

    EXPECTED_NAME_BOOK = (By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")
    NAME_BOOK = (By.CSS_SELECTOR, "#messages>div.alert>div.alertinner>strong")