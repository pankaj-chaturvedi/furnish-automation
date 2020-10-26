import pytest
import xlrd
import os

from base.webdriver_factory import WebDriverFactory
from pages.test001_login_page import LoginPage


@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser, env):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance(env)
    lp = LoginPage(driver)
    username = "pankaj@arcgate.com"
    password = "Arcgate12!"
    lp.login_to_website(username, password)

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")
    parser.addoption("--env", help="Type of environment i.e prod, qa, dev")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")


@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


