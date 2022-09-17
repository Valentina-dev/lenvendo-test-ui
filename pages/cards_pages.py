from constants.locators.card_value import CardsValue
from pages.base_page import BasePage


class CardsPage(BasePage):

    def cards_values_is_clickable(self):
        elements = self.browser.find_elements(*CardsValue.values)
        amount_input = self.browser.find_element(*CardsValue.input_value)
        for element in elements:
            element.click()
            gift_value = element.text
            assert element.is_displayed()
            assert amount_input.get_attribute('value') == gift_value
