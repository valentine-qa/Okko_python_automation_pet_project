
from selene import browser, by, be, have


def test_invalid_login():
    browser.open('https://okko.tv/')
    browser.element('[test-id="nav_sign"]').click()
    # browser.element(by.text('Войдите или зарегистрируйтесь')).should(be.visible)
    browser.element('[test-id="sign_input"]').type('@@@').press_enter()
    browser.element('[test-id="sign_input"]').element('..').should(have.text('Неверный формат'))


def test_valid_login():
    browser.open('https://okko.tv/')
    browser.element('[test-id="nav_sign"]').click()
    browser.element('.GFGFQQMn').should(have.text('Войдите или зарегистрируйтесь'))
    browser.element('[test-id="sign_input"]').type('valentien@gmail.com').press_enter()
    browser.element('.GFGFQQMn').should(have.text('Введите код из письма')).should(have.text(f'Мы отправили письмо на valentien@gmail.com'))

