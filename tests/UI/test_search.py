from time import sleep

import allure
import pytest
from allure_commons.types import Severity
from selene import browser, be, have
from okko_python_automation_pet_project.pages.web.main_page import main_page

@allure.tag('UI')
@allure.feature('UI')
@allure.story('Film search')
@allure.title('Search film by title')
@allure.severity(Severity.CRITICAL)
@allure.link('https://okko.tv/', name='Онлайн-кинотеатр OKKO')
def test_search_film_by_title():
    film_title = 'Перевозчик'

    main_page.open()

    main_page.search_film_by_title(film_title)

    main_page.chek_result_by_film(film_title)

    # browser.all('[test-id="card_rail_item"]').first.should(be.visible).should(have.text('Перевозчик'))

@pytest.mark.skip
@pytest.mark.positive
@allure.tag('UI')
@allure.feature('UI')
@allure.story('Film search')
@allure.title('Search film by actor')
@allure.severity(Severity.CRITICAL)
@allure.link('https://okko.tv/', name='Онлайн-кинотеатр OKKO')
def test_search_film_by_actor():
    actor_name = 'Джейсон Стэйтем'

    main_page.open()

    main_page.search_film_by_actor(actor_name)

    main_page.chek_result_by_actor(actor_name)

@pytest.mark.skip
@pytest.mark.positive
@allure.tag('UI')
@allure.feature('UI')
@allure.story('Film search')
@allure.title('Search film by director')
@allure.severity(Severity.CRITICAL)
@allure.link('https://okko.tv/', name='Онлайн-кинотеатр OKKO')
def test_search_by_director():
    director_name = 'Гай Ричи'
    main_page.open()

    main_page.search_film_by_director(director_name)

    main_page.chek_result_by_director(director_name)

