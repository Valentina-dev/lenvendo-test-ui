from pages.cards_pages import CardsPage
from config import DOMAIN


def test_click_in_cards_values(browser):
    link = f"{DOMAIN}"
    card_page = CardsPage(browser, link)
    card_page.open()
    card_page.cards_values_is_clickable()
