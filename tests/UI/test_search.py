from selene import browser



def test_search():
    browser.open('https://okko.tv/')
    browser.element('[test-id="nav_search"]').press_enter()
    browser.element('[data-testid="nav_search_input"]').type('Перевозчик').press_enter()
    browser.all('[test-id="card_rail_item"]').first().c