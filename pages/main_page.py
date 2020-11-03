import pytest
from selenium import webdriver
from .base_page import BasePage
from .basket_page import BasketPage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
     def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)








