from Pages.main_page import MainPage
from Pages.base_page import BasePage
from locators.main_page_locators import TestLocatorsMainPage
from locators.base_page_locators import TestLocatorsBasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestMainPage:

    def test_click_order_at_the_top(self, driver):
        self.driver = driver

        # создали объект класса главной страницы
        main_page = MainPage(self.driver)

        # перешли на страницу приложения
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        # приняли куки
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(TestLocatorsBasePage.cookie_button))
        base_page = BasePage(self.driver)
        base_page.click_cookie_button()

        WebDriverWait(self.driver, 15).until(
            expected_conditions.element_to_be_clickable(TestLocatorsMainPage.order_button_at_the_top))

        # кликнули по кнопке заказ вверху страницы
        main_page.click_order(TestLocatorsMainPage.order_button_at_the_top)

        # ожидание загрузки страницы
        WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located(TestLocatorsMainPage.header_for_whom))

        # проверили, что открылась страница заказа
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/order'

    def test_click_order_at_the_bottom(self, driver):
        self.driver = driver

        # создали объект класса главной страницы
        main_page = MainPage(self.driver)

        # перешли на страницу приложения
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        # приняли куки
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(TestLocatorsBasePage.cookie_button))
        base_page = BasePage(self.driver)
        base_page.click_cookie_button()

        # ожидание загрузки страницы
        WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located(TestLocatorsMainPage.header_scooter_for_couple_days))

        # проскроллили до кнопки Заказ
        main_page.scroll_to_order()

        WebDriverWait(self.driver, 15).until(
            expected_conditions.element_to_be_clickable(TestLocatorsMainPage.order_button_at_the_bottom))

        # кликнули по кнопке заказ внизу страницы
        main_page.click_order(TestLocatorsMainPage.order_button_at_the_bottom)

        # ожидание загрузки страницы
        WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located(TestLocatorsMainPage.header_for_whom))

        # проверили, что открылась страница заказа
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/order'

    def test_click_logo_yandex_open_main_page_yandex(self, driver):
        self.driver = driver

        # перешли на страницу приложения
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        # приняли куки
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(TestLocatorsBasePage.cookie_button))
        base_page = BasePage(self.driver)
        base_page.click_cookie_button()

        # создали объект класса главной страницы
        main_page = MainPage(self.driver)

        # нажали логотип Яндекс
        main_page.click_yandex()

        # проверили, что открылась вторая вкладка в браузере
        assert len(self.driver.window_handles) == 2
