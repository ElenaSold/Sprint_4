from Pages.page_order import PageOrder
from Pages.base_page import BasePage
from locators.order_page_locators import TestLocatorsOrder
from locators.base_page_locators import TestLocatorsBasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from datetime import date

class TestOrderPage:

    def test_make_an_order_for_tomorrow_1day_black_aeroport_phone_with_7_with_comment(self, driver):
        self.driver = driver

        # перешли на страницу заказа
        self.driver.get('https://qa-scooter.praktikum-services.ru/order')

        # создали объект класса страницы заказа
        page_order = PageOrder(self.driver)

        # приняли куки
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(TestLocatorsBasePage.cookie_button))
        base_page = BasePage(self.driver)
        base_page.click_cookie_button()

        # заполнили первую страницу заказа
        page_order.complete_first_page('Елена', 'Солдатенкова', 'Жукова,3', TestLocatorsOrder.station_aeroport, '+79099999999')

        #дата доставки
        today = date.today()
        tomorrow = "{}.{}.{}".format(today.day + 1, today.month, today.year)

        # заполнили вторую страницу заказа
        page_order.complete_second_page(tomorrow, TestLocatorsOrder.day, TestLocatorsOrder.black_color, 'тест')

        # подтвердили заказ
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(TestLocatorsOrder.button_yes))

        page_order.click_yes()

        # проверили, что появилось окно с подтверждением заказа
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocatorsOrder.confirm_window))

        assert page_order.confirm_is_displayed()

    def test_make_an_order_for_next_month_7days_grey_sokolniki_phone_with_8_without_comment(self, driver):
        self.driver = driver

        # перешли на страницу заказа
        self.driver.get('https://qa-scooter.praktikum-services.ru/order')

        # создали объект класса страницы заказа
        page_order = PageOrder(self.driver)

        # приняли куки
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(TestLocatorsBasePage.cookie_button))
        base_page = BasePage(self.driver)
        base_page.click_cookie_button()

        # заполнили первую страницу заказа
        page_order.complete_first_page('Саша', 'Иванов', 'улица Новодмитровская, дом 45 стр 1 кв 5', TestLocatorsOrder.station_sokolniki, '89096666666')

        # дата доставки
        today = date.today()
        next_month = "{}.{}.{}".format(1, today.month + 1, today.year)

        # заполнили вторую страницу заказа
        page_order.complete_second_page(next_month, TestLocatorsOrder.seven_days, TestLocatorsOrder.grey_color, '')

        # подтвердили заказ
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(TestLocatorsOrder.button_yes))

        page_order.click_yes()

        # проверили, что появилось окно с подтверждением заказа
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocatorsOrder.confirm_window))

        assert page_order.confirm_is_displayed()

    def test_click_logo_scooter_open_main_page_scooter(self, driver):
        self.driver = driver

        # перешли на страницу заказа
        self.driver.get('https://qa-scooter.praktikum-services.ru/order')

        # создали объект класса страницы заказа
        page_order = PageOrder(self.driver)

        # приняли куки
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(TestLocatorsBasePage.cookie_button))
        base_page = BasePage(self.driver)
        base_page.click_cookie_button()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(TestLocatorsOrder.logo_scooter))

        # перешли со страницы заказа на главную
        page_order.click_logo_scooter()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocatorsOrder.header_scooter))

        # проверили, что открылась главная страница приложения
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'


