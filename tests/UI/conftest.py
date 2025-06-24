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

import pytest


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config

from okko_python_automation_pet_project.utils import attach


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default="127.0"
    )


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):

    browser_version = request.config.getoption('--browser_version')
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

    browser = Browser(Config(driver=lambda: driver))

    yield browser

    attach.add_screenshot(browser)
    attach.add_html(browser)
    attach.add_html(browser)
    attach.add_video(browser)
