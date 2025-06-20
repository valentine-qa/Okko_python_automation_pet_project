from selene import browser, be, have


def test_come_to_main_menu_by_logo_click():
    browser.open('https://okko.tv/catalog')
    browser.element('a[aria-label="Главная страница"]').click()
    browser.element('[test-id="home_page"]').should(be.visible)

def test_free_month():
    browser.open('https://okko.tv/')
    browser.element('[test-id="header"]').should(have.text('Месяц бесплатно'))

def test_film_price_is_visible():
    browser.open('https://okko.tv/store')
    cards = browser.all('[test-id="search_collection_element"]')
    for card in cards:
        card.element('.__26ii8ap5').should(have.text('ОТ')).should(have.text('руб'))
