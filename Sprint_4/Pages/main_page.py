from locators.main_page_locators import TestLocatorsMainPage

class MainPage:

    # конструктор класса
    def __init__(self, driver):
        self.driver = driver

    # метод кликает на Заказ
    def click_order(self, order):
        self.driver.find_element(*order).click()

    # метод скроллит до кнопки заказ
    def scroll_to_order(self):
        element = self.driver.find_element(*TestLocatorsMainPage.order_button_at_the_bottom)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # метод кликает по логотипу Яндекс
    def click_yandex(self):
        self.driver.find_element(*TestLocatorsMainPage.logo_yandex).click()
