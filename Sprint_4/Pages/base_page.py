from locators.base_page_locators import TestLocatorsBasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:

    # конструктор класса
    def __init__(self, driver):
        self.driver = driver

    #метод нажимает кнопку "да все привыкли"
    def click_cookie_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(TestLocatorsBasePage.cookie_button))
        self.driver.find_element(*TestLocatorsBasePage.cookie_button).click()