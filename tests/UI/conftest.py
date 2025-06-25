
import pytest


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene.support.shared import browser
from okko_python_automation_pet_project.utils import attach

DEFAULT_BROWSER_VERSION = '127.0'

def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default="127.0"
    )


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):

    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )


    browser.config.driver = driver
    browser.config.base_url = "https://okko.tv"

    yield browser

    if request.node.rep_call.failed:
        attach.add_screenshot(browser)
        attach.add_html(browser)
        if browser.driver.capabilities['browserName'] == 'chrome':
            attach.add_logs(browser)
        attach.add_video(browser)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

















# import time
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selene import Browser, Config, browser
#
#
# @pytest.fixture(scope='function', autouse=True)
# def browser_config():
#     browser.config.driver_name = 'chrome'
#     browser.config.window_width = '1800'
#     browser.config.window_height = '1000'
#     browser.config.base_url = 'https://okko.tv'
#     yield
#
#     time.sleep(3)
#     browser.quit()