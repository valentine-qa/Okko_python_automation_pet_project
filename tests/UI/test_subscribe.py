import allure
import pytest
from allure_commons.types import Severity
from selene import browser, be, have
from okko_python_automation_pet_project.pages.web.main_page import main_page
from okko_python_automation_pet_project.pages.web.subcribe_page import subscribe_page
@pytest.mark.positive
@allure.tag('UI')
@allure.feature('UI')
@allure.story('Subscribe')
@allure.title('Subscribe')
@allure.severity(Severity.CRITICAL)
@allure.link('https://okko.tv/', name='Онлайн-кинотеатр OKKO')
def test_see_film_with_subscribe():
    main_page.open()

    subscribe_page.choose_film_from_films_tab()

    subscribe_page.subscribe()

    subscribe_page.check_login_form_open()




@pytest.mark.positive
@allure.tag('UI')
@allure.feature('UI')
@allure.story('Prices')
@allure.title('Prices is visible')
@allure.severity(Severity.CRITICAL)
@allure.link('https://okko.tv/', name='Онлайн-кинотеатр OKKO')
def test_film_price_is_visible():

    # browser.open('https://okko.tv/store')
    # cards = browser.all('[test-id="search_collection_element"]')
    # for card in cards:
    #     card.element('.__26ii8ap5').should(have.text('ОТ')).should(have.text('руб'))

    main_page.open()

    cards = subscribe_page.get_film_cards()

    subscribe_page.check_prices_windows(cards)