from time import sleep

import allure
import pytest
from allure_commons.types import Severity
from selene import browser, be, have


@allure.tag('UI')
@allure.feature('UI')
@allure.story('Registration options')
@allure.title('Check registration options')
@allure.severity(Severity.CRITICAL)
@allure.link('https://okko.tv/', name='Онлайн-кинотеатр OKKO')
def test_search_by_film_name():
    browser.open('https://okko.tv/')
    browser.element('[test-id="nav_search"]').press_enter()
    browser.element('[data-testid="nav_search_input"]').type('Перевозчик').press_enter()
    browser.all('[test-id="card_rail_item"]').first.should(be.visible).should(have.text('Перевозчик'))
    browser.all('[test-id="card_rail_item"]').second.should(be.visible).should(have.text('Перевозчик'))


def test_search_by_actor():
    browser.open('https://okko.tv/')
    browser.element('[test-id="nav_search"]').press_enter()
    browser.element('[data-testid="nav_search_input"]').type('Джейсон Стейтэм').press_enter()
    sleep(1)
    browser.all('[test-id="card_rail_item"]').first.click()
    browser.element('[test-id="meta_actors"]').should(have.text('Джейсон Стэйтем'))

def test_search_by_director():
    browser.open('https://okko.tv/')
    browser.element('[test-id="nav_search"]').press_enter()
    browser.element('[data-testid="nav_search_input"]').type('Гай ричи').press_enter()
    sleep(1)
    browser.all('[test-id="card_rail_item"]').first.click()
    browser.element('test-id="meta_director"').should(have.text('Гай ричи'))
