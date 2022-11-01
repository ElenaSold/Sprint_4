from locators.base_page_locators import TestLocatorsBasePage

class BasePage:

    # конструктор класса
    def __init__(self, driver):
        self.driver = driver

    #метод нажимает кнопку "да все привыкли"
    def click_cookie_button(self):
        self.driver.find_element(*TestLocatorsBasePage.cookie_button).click()