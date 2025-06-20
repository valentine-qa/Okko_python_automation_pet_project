import os
import time

import pytest
from selene import browser, have, by, be




@pytest.fixture(scope="function")
def browser_params():
    # Браузер остается открытым
    browser.config.hold_browser_open = True
    # Ширина/высота окна браузера
    browser.config.window_width = 1280
    browser.config.window_height = 800
    #На каком браузере открываем тест
    browser.config.driver_name = 'chrome'

    #yield что мы будем делать после теста
    yield

    time.sleep(4) #ждем 4 секунды
    browser.quit() #выходим из браузера, НЕ писать close()!!!!

def test_demoqa(browser_params): #в скобках указываем фикстуру

    browser.open('https://demoqa.com/automation-practice-form') #Открытие страницы

    browser.element('#firstName').type('valentine') #Ввод текста в поле по id
    # ______________________________________________________________________________
    # Поиск родительского элемента по id и внутри него поиск по тексту
    browser.element('#genterWrapper').element(by.text("Male")).click()
    # ______________________________________________________________________________
    # Поиск всех элементов с name=gender и выбор в них элемента со значением male
    browser.all('[name=gender]').element_by(have.value('Male')).click()
    # ______________________________________________________________________________
    # Поиск элемента по двум аттрибутам в рамках одной строки И name И gender
    # <input name="gender" id="gender-radio-1" value="Male">
    browser.element('[name=gender][value=Male]').click()
    #______________________________________________________________________________
    #Обращение к родителю элемента .element('..')
    browser.element('[name=gender]').element('..').click()
    # ______________________________________________________________________________
    # Выбор даты рождения
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").element("[value='4']").click()
    browser.element(".react-datepicker__year-select").element("[value='2000']").click()
    browser.all(".react-datepicker__day:not(.react-datepicker__day--outside-month)").element_by(have.text('13')).click()
    # ______________________________________________________________________________
    # Поиск родителя, а затем внутри него элемента с тегом Label и аттрибутом for
    # <label title for ="hobbies-checkbox-1" class ="custom-control-label" >
    browser.element("#hobbiesWrapper").element("label[for=hobbies-checkbox-1]").click()
    # ______________________________________________________________________________
    # Поиск родителя, а затем внутри него элемента с тегом Label и аттрибутом for через пробел
    browser.element("#hobbiesWrapper [for=hobbies-checkbox-1]").click()
    # ______________________________________________________________________________
    # Поиск всех элементов, где есть артибут НАЧИНАЮЩИЙСЯ на gender-radio [for^=gender-radio]
    browser.all('[for^=gender-radio]').element_by(have.text('Male')).click()
    # Поиск всех элементов, где есть артибут НАЧИНАЮЩИЙСЯ на gender-radio [for^=gender-radio]
    # И также в атрибуте id ГДЕ-ТО ЕСТЬ option /id=react-select-3-option-1/
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('NCR')).click()
    # ______________________________________________________________________________
    #Отправка фото
    browser.element('input[id=uploadPicture]').send_keys(os.path.abspath('picture.png'))

    #Проверка, что элемент должен быть на странице
    browser.element(".modal-content").should(be.visible)
    #Проверка, что внутри элемента есть текст
    browser.element(".modal-content").should(have.text("Thanks for submitting the form"))

    browser.all(".table-responsive").element_by(have.exact_texts("Student Name", "valentine"))








#Прочие фичи
#Зафризить UI через Devtoolse console- setTimeout('debugger', 3_000) (заморозится через 3 секунды)