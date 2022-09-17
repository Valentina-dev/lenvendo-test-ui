from selenium.webdriver.common.by import By


class CardsValue:
    values = (By.XPATH, "(//button[contains(@class, 'par-options__button')])")
    input_value = (By.XPATH, "(//input[contains(@class, 'js-par-input par-input-block__input')])")