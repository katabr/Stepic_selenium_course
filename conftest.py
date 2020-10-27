import pytest
from selenium import webdriver
import time






@pytest.fixture
def browser(request):

    language_name = request.config.getoption("language")
    lang = str(language_name)
    link = "http://selenium1py.pythonanywhere.com/" + lang + "/catalogue/coders-at-work_207/"
    browser = webdriver.Chrome()
    browser.get(link)
    yield browser
    browser.quit()


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default = None, help="Choose language")

