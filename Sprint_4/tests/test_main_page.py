from selenium import webdriver
from Pages.main_page import MainPage
from locators.main_page_locators import TestLocatorsMainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestMainPage:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()

    def test_click_order_at_the_top(self):
        # перешли на страницу приложения
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(TestLocatorsMainPage.order_button_at_the_top))

        # создали объект класса главной страницы
        main_page = MainPage(self.driver)

        # кликнули по кнопке заказ вверху страницы
        main_page.click_order(TestLocatorsMainPage.order_button_at_the_top)

        # ожидание загрузки страницы
        WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located(TestLocatorsMainPage.header_for_whom))

        # проверили, что открылась страница заказа
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/order'

    def test_click_order_at_the_bottom(self):
        # перешли на страницу приложения
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        # создали объект класса главной страницы
        main_page = MainPage(self.driver)

        # проскроллили до кнопки Заказ
        main_page.scroll_t0_order()

        # кликнули по кнопке заказ внизу страницы
        main_page.click_order(TestLocatorsMainPage.order_button_at_the_bottom)

        # ожидание загрузки страницы
        WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located(TestLocatorsMainPage.header_for_whom))

        # проверили, что открылась страница заказа
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/order'

    def test_click_logo_yandex_open_main_page_yandex(self):
        # перешли на страницу приложения
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        # создали объект класса главной страницы
        main_page = MainPage(self.driver)

        # нажали логотип Яндекс
        main_page.click_yandex()

        # проверили, что открылась вторая вкладка в браузере
        assert len(self.driver.window_handles) == 2

    @classmethod
    def teardown_class(cls):
        # Закрыли браузер
        cls.driver.quit()