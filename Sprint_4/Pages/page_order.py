from locators.order_page_locators import TestLocatorsOrder
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class PageOrder:

    # конструктор класса
    def __init__(self, driver):
        self.driver = driver

    #метод заполняет поле Имя
    def fill_name(self, name):
        self.driver.find_element(*TestLocatorsOrder.name).send_keys(name)

    # метод заполняет поле Фамилия
    def fill_surname(self, surname):
        self.driver.find_element(*TestLocatorsOrder.surname).send_keys(surname)

    # метод заполняет поле Адрес
    def fill_address(self, address):
        self.driver.find_element(*TestLocatorsOrder.address).send_keys(address)

    # метод выбирает станцию
    def fill_station(self, station):
        self.driver.find_element(*TestLocatorsOrder.station_field).click()

        element = self.driver.find_element(*station)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        self.driver.find_element(*station).click()

    # метод заполняет поле Телефон
    def fill_phone(self, phone):
        self.driver.find_element(*TestLocatorsOrder.phone).send_keys(phone)

    # метод кликает по кнопке Далее
    def click_next(self):
        self.driver.find_element(*TestLocatorsOrder.button_next).click()

    # метод заполняет поле "Когда привезти самокат"
    def fill_date(self, date):
        self.driver.find_element(*TestLocatorsOrder.date).send_keys(date)

    # метод кликает на поле "Срок аренды" и выбирает нужный срок
    def click_how_long(self, days):
        self.driver.find_element(*TestLocatorsOrder.how_long).click()
        self.driver.find_element(*days).click()

    # метод выбирает цвет самоката
    def choose_color(self, color):
        self.driver.find_element(*color).click()

    # метод заполняет поле "Комментарий"
    def fill_comment(self, comment):
        self.driver.find_element(*TestLocatorsOrder.comment).send_keys(comment)

    # метод нажимает "Заказать" под формой
    def click_order_under_the_form(self):
        self.driver.find_element(*TestLocatorsOrder.button_order_under_the_form).click()

    # метод подтверждает заказ
    def click_yes(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(TestLocatorsOrder.button_yes))
        self.driver.find_element(*TestLocatorsOrder.button_yes).click()

    # метод проверяет отображается ли окно подтверждения
    def confirm_is_displayed(self):
        return self.driver.find_element(*TestLocatorsOrder.confirm_window).is_displayed()

    # метод переходит со страницы заказа на главную
    def click_logo_scooter(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(TestLocatorsOrder.logo_scooter))
        self.driver.find_element(*TestLocatorsOrder.logo_scooter).click()

    # метод заполняет первую страницу заказа
    def complete_first_page(self, name, surname, address, station, phone):
        # заполнили поле Имя
        self.fill_name(name)

        # заполнили поле Фамилия
        self.fill_surname(surname)

        # заполнили поле Адрес
        self.fill_address(address)

        # указали станцию метро
        self.fill_station(station)

        # заполнили поле Телефон
        self.fill_phone(phone)

        # нажали "Далее"
        self.click_next()

    # метод заполняет вторую страницу заказа
    def complete_second_page(self, date_of_delivery, days, color, comment):
        # ввели дату доставки
        self.fill_date(date_of_delivery)

        # ввели срок аренды
        self.click_how_long(days)

        # указали цвет
        self.choose_color(color)

        # оставили комментарий
        self.fill_comment(comment)

        # нажали Заказать под формой заказа
        self.click_order_under_the_form()
