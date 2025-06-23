from time import sleep

import allure
from selene import browser, be, have
from okko_python_automation_pet_project.pages.web.login_page import login_page


class Subscribe:

    def __init__(self):
        self.first_film = browser.all('[test-id="search_collection_element"]').first
        self.subscribe_button = browser.element('[test-id="action_purchase"]')
        self.login_tab_header = browser.element('.RdGM53zT')
        self.store_button = browser.element('[test-id="web_main"]')
        self.cards = browser.all('[test-id="search_collection_element"]')
        self.films_tab = browser.element('[test-id="search_collection_element"]')

    @allure.step('Come to film collection and choose a film')
    def choose_film_from_films_tab(self):
        with allure.step('Click on store menu'):
            self.store_button.click()
        with allure.step('Click on first collection'):
            self.films_tab.click()
        sleep(1)
        with allure.step('Click on first film in rail'):
            self.films_tab.click()

    @allure.step('Click subscribe button')
    def subscribe(self):
        self.subscribe_button.click()

    @allure.step('Check that login form is open')
    def check_login_form_open(self):
        self.login_tab_header.should(be.visible).should(have.text('ВХОД ИЛИ РЕГИСТРАЦИЯ'))
        login_page.login_input_field.should(be.visible)

    @allure.step('Get list with all films')
    def get_film_cards(self):
        browser.open('/store')
        cards = browser.all('[test-id="search_collection_element"]')
        return cards

    @allure.step('Check that card_windows has prices')
    def check_prices_windows(self, cards):
        for card in cards:
            card.element('.__26ii8ap5').should(have.text('ОТ')).should(have.text('руб'))






subscribe_page = Subscribe()
