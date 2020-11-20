import pytest
from selenium import webdriver
from .base_page import BasePage


class MainPage(BasePage):
     def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

