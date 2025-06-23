from time import sleep

import allure
from selene import browser, have, be


class MainPage:

    def __init__(self):
        self.search_button = browser.element('[test-id="nav_search"]')
        self.search_button_input_field = browser.element('[data-testid="nav_search_input"]')
        self.login_button = browser.element('[test-id="nav_sign"]')
        self.first_film = browser.all('[test-id="card_rail_item"]').first
        self.actors_tab = browser.element('[test-id="meta_actors"]')
        self.director_tab = browser.element('[test-id="meta_director"]')

    @allure.step('Open website')
    def open(self):
        browser.open('/')

    @allure.step('Search film by title')
    def search_film_by_title(self, film_title):
        self.search_button.click()
        self.search_button_input_field.type(film_title).press_enter()
        sleep(1)

    @allure.step('Search film by actor')
    def search_film_by_actor(self, actor_name):
        self.search_button.click()
        self.search_button_input_field.type(actor_name).press_enter()
        sleep(1)

    @allure.step('Search film by director')
    def search_film_by_director(self, director_name):
        self.search_button.click()
        self.search_button_input_field.type(director_name).press_enter()
        sleep(1)

    @allure.step("Check actor name in actors tab")
    def chek_result_by_actor(self, actor_name):
        self.first_film.click()
        self.actors_tab.should(have.text(actor_name))

    @allure.step("Check film title in first film")
    def chek_result_by_film(self, film_title):
        self.first_film.should(be.visible).should(have.text(film_title))

    @allure.step("Check director name in directors tab")
    def chek_result_by_director(self, director_name):
        self.first_film.click()
        self.director_tab.should(have.text(director_name))


main_page = MainPage()