from selenium import webdriver
from Pages.page_order import PageOrder
from locators.order_page_locators import TestLocatorsOrder
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from datetime import date

class TestOrderPage:

    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()

    def test_make_an_order_for_first_day_of_next_month_1day_black_aeroport_phone_with_7_with_comment(self):
        # перешли на страницу заказа
        self.driver.get('https://qa-scooter.praktikum-services.ru/order')

        # создали объект класса страницы заказа
        page_order = PageOrder(self.driver)

        # заполнили поле Имя
        page_order.fill_name('Елена')

        # заполнили поле Фамилия
        page_order.fill_surname('Солдатенкова')

        # заполнили поле Адрес
        page_order.fill_address('Жукова,3')

        # указали станцию метро
        page_order.fill_station(TestLocatorsOrder.station_aeroport)

        # заполнили поле Телефон
        page_order.fill_phone('+79099999999')

        # нажали "Далее"
        page_order.click_next()

        # ввели дату доставки
        today = date.today()
        tomorrow = "{}.{}.{}".format(1, today.month+1, today.year)
        page_order.fill_date(tomorrow)

        # ввели срок аренды
        page_order.click_how_long(TestLocatorsOrder.day)

        # указали цвет
        page_order.choose_color(TestLocatorsOrder.black_color)

        # оставили комментарий
        page_order.fill_comment('тест')

        # нажали Заказать под формой заказа
        page_order.click_order_under_the_form()

        # подтвердили заказ
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(TestLocatorsOrder.button_yes))

        page_order.click_yes()


        # проверили, что появилось окно с подтверждением заказа
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocatorsOrder.confirm_window))

        assert page_order.confirm_is_displayed()

    def test_make_an_order_for_last_day_of_next_month_7days_grey_sokolniki_phone_with_8_without_comment(self):
        # перешли на страницу заказа
        self.driver.get('https://qa-scooter.praktikum-services.ru/order')

        # создали объект класса страницы заказа
        page_order = PageOrder(self.driver)

        # заполнили поле Имя
        page_order.fill_name('Саша')

        # заполнили поле Фамилия
        page_order.fill_surname('Иванов')

        # заполнили поле Адрес
        page_order.fill_address('улица Новодмитровская, дом 45 стр 1 кв 5')

        # указали станцию метро
        page_order.fill_station(TestLocatorsOrder.station_sokolniki)

        # заполнили поле Телефон
        page_order.fill_phone('89096666666')

        # нажали "Далее"
        page_order.click_next()

        # ввели дату доставки
        today = date.today()
        next_month = "{}.{}.{}".format(30, today.month+1, today.year)
        page_order.fill_date(next_month)

        # ввели срок аренды
        page_order.click_how_long(TestLocatorsOrder.seven_days)

        # указали цвет
        page_order.choose_color(TestLocatorsOrder.grey_color)

        # нажали Заказать под формой заказа
        page_order.click_order_under_the_form()

        # подтвердили заказ
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(TestLocatorsOrder.button_yes))

        page_order.click_yes()

        # проверили, что появилось окно с подтверждением заказа
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocatorsOrder.confirm_window))

        assert page_order.confirm_is_displayed()

    def test_click_logo_scooter_open_main_page_scooter(self):
        # перешли на страницу заказа
        self.driver.get('https://qa-scooter.praktikum-services.ru/order')

        # создали объект класса страницы заказа
        page_order = PageOrder(self.driver)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(TestLocatorsOrder.logo_scooter))

        # перешли со страницы заказа на главную
        page_order.click_logo_scooter()

        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocatorsOrder.header_scooter))

        # проверили, что открылась главная страница приложения
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @classmethod
    def teardown_class(cls):
        # Закрыли браузер
        cls.driver.quit()

