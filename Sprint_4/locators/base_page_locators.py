from selenium.webdriver.common.by import By

class TestLocatorsBasePage:
    # куки, кнопка "да все привыкли"
    cookie_button = (By.XPATH, ".//button[contains(@class, 'App_CookieButton')]")