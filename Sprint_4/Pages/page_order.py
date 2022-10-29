from locators.order_page_locators import TestLocatorsOrder
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
        self.driver.find_element(*TestLocatorsOrder.button_yes).click()

    # метод проверяет отображается ли окно подтверждения
    def confirm_is_displayed(self):
        return self.driver.find_element(*TestLocatorsOrder.confirm_window).is_displayed()

    # метод переходит со страницы заказа на главную
    def click_logo_scooter(self):
        self.driver.find_element(*TestLocatorsOrder.logo_scooter).click()
