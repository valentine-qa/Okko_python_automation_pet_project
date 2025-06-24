import allure
import pytest
from allure_commons.types import Severity
from selene import browser, by, be, have
from okko_python_automation_pet_project.pages.web.login_page import login_page



# allure serve tests/UI/allure-results


@pytest.mark.negative
@allure.tag('UI')
@allure.feature('UI')
@allure.story('User Login')
@allure.title('Login with invalid email')
@allure.severity(Severity.CRITICAL)
@allure.link('https://okko.tv/', name='Онлайн-кинотеатр OKKO')
def test_invalid_login():
    invalid_email = '@@@!@312'

    login_page.open_login_form()

    login_page.input_mail(invalid_email)

    login_page.chek_registration_fail()

@pytest.mark.skip
@pytest.mark.positive
@allure.tag('UI')
@allure.feature('UI')
@allure.story('User Login')
@allure.title('Login with valid email')
@allure.severity(Severity.CRITICAL)
@allure.link('https://okko.tv/', name='Онлайн-кинотеатр OKKO')
def test_valid_login():
    valid_email = 'valentineQA@gmail.com'

    login_page.open_login_form()

    login_page.input_mail(valid_email)

    login_page.check_registration_success(valid_email)

    # browser.open('https://okko.tv/')
    # browser.element('[test-id="nav_sign"]').click()
    # browser.element('.GFGFQQMn').should(have.text('Войдите или зарегистрируйтесь'))
    # browser.element('[test-id="sign_input"]').type('valentine@gmail.com').press_enter()
    # browser.element('.GFGFQQMn').should(have.text('Введите код из письма')).should(have.text(f'Мы отправили письмо на valentien@gmail.com'))

