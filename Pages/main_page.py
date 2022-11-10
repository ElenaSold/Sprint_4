from locators.main_page_locators import TestLocatorsMainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class MainPage:

    # конструктор класса
    def __init__(self, driver):
        self.driver = driver

    # метод кликает на Заказ
    def click_order(self, order):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(order))
        self.driver.find_element(*order).click()

    # метод скроллит до кнопки заказ
    def scroll_to_order(self):
        WebDriverWait(self.driver, 5).until(
             expected_conditions.presence_of_element_located(TestLocatorsMainPage.order_button_at_the_bottom))
        element = self.driver.find_element(*TestLocatorsMainPage.order_button_at_the_bottom)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # метод кликает по логотипу Яндекс
    def click_yandex(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(TestLocatorsMainPage.logo_yandex))
        self.driver.find_element(*TestLocatorsMainPage.logo_yandex).click()
