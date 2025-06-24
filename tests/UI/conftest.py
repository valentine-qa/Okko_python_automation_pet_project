import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config, browser


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

@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    options = Options()
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.set_capability("browserName", capabilities["browserName"])
    options.set_capability("browserVersion", capabilities["browserVersion"])
    options.set_capability("selenoid:options", capabilities["selenoid:options"])

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    # Подменяем глобальный браузер
    browser.config.driver = driver
    browser.config.base_url = "https://okko.tv"
    browser.config.timeout = 10

    yield

    browser.quit()

    # attach.add_screenshot(browser)
    # attach.add_logs(browser)
    # attach.add_html(browser)
    # attach.add_video(browser)

    browser.quit()