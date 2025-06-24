import time
from ssl import Options

import pytest
from selene import browser, Browser, Config
from selene.support import webdriver


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

@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser = Browser(Config(driver=lambda: driver))
    yield browser

    # attach.add_screenshot(browser)
    # attach.add_logs(browser)
    # attach.add_html(browser)
    # attach.add_video(browser)

    browser.quit()