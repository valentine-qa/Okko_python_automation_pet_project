from time import sleep

import allure
from selene import browser, have, by, be


class LoginPage:

    def __init__(self):
        self.login_button = browser.element('[test-id="nav_sign"]')
        self.login_input_field = browser.element('[test-id="sign_input"]')
        self.confirm_button = browser.element('[test-id="continue_btn"]')
        self.login_window = browser.element('.GFGFQQMn')

    @allure.step("Open a login form")
    def open_login_form(self):
        with allure.step('Open a website'):
            browser.open('/')
        with allure.step('Click by login button'):
            self.login_button.click()

    @allure.step("Input email")
    def input_mail(self, test_email):
        # browser.element(by.text('Войдите или зарегистрируйтесь')).should(be.visible)
        self.login_input_field.type(test_email)
        self.confirm_button.click()

    @allure.step("Checking for an invalid email error")
    def check_registration_fail(self):
        self.login_input_field.element('..').should(have.text('Неверный формат'))

    @allure.step("Checking for login success")
    def check_registration_success(self, test_email):
        self.login_window.should(have.text('Введите код из письма')).should(have.text(f'Мы отправили письмо на {test_email}'))


login_page = LoginPage()

