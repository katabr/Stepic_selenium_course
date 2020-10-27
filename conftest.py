
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en-gb")

@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language")
    lang = str(language_name)
    link = "http://selenium1py.pythonanywhere.com/" + lang
    options = Options()
    options.add_experimental_option(
    'prefs', {'intl.accept_languages':language_name})


    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        print("Browser {} still is not implemented".format(browser_name))

    browser.get(link)
    yield browser
    print("\nquit browser..")
    browser.quit()




# @pytest.fixture
# def browser(request):
#
#     language_name = request.config.getoption("language")
#     #lang = str(language_name)
#     #link = "http://selenium1py.pythonanywhere.com/" + lang + "/catalogue/coders-at-work_207/"
#     options = Options()
#     options.add_experimental_option(
#         'prefs', {'intl.accept_languages':language_name})
#
#     browser = webdriver.Chrome()
#     browser.get(link)
#     yield browser
#     browser.quit()
#
#
# def pytest_addoption(parser):
#     parser.addoption('--language', action='store', default =en-gb , help="Choose language")

