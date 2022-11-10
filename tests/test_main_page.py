from Pages.main_page import MainPage
from Pages.base_page import BasePage
from locators.main_page_locators import TestLocatorsMainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestMainPage:

    def test_click_order_at_the_top(self, driver):

        # создали объект класса главной страницы
        main_page = MainPage(driver)

        # перешли на страницу приложения
        driver.get('https://qa-scooter.praktikum-services.ru/')

        # приняли куки
        base_page = BasePage(driver)
        base_page.click_cookie_button()

        # кликнули по кнопке заказ вверху страницы
        main_page.click_order(TestLocatorsMainPage.order_button_at_the_top)

        # ожидание загрузки страницы
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(TestLocatorsMainPage.header_for_whom))

        # проверили, что открылась страница заказа
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/order'

    def test_click_order_at_the_bottom(self, driver):

        # создали объект класса главной страницы
        main_page = MainPage(driver)

        # перешли на страницу приложения
        driver.get('https://qa-scooter.praktikum-services.ru/')

        # приняли куки
        base_page = BasePage(driver)
        base_page.click_cookie_button()

        # проскроллили до кнопки Заказ
        main_page.scroll_to_order()

        # кликнули по кнопке заказ внизу страницы
        main_page.click_order(TestLocatorsMainPage.order_button_at_the_bottom)

        # ожидание загрузки страницы
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(TestLocatorsMainPage.header_for_whom))

        # проверили, что открылась страница заказа
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/order'

    def test_click_logo_yandex_open_main_page_yandex(self, driver):

        # перешли на страницу приложения
        driver.get('https://qa-scooter.praktikum-services.ru/')

        # приняли куки
        base_page = BasePage(driver)
        base_page.click_cookie_button()

        # создали объект класса главной страницы
        main_page = MainPage(driver)

        # нажали логотип Яндекс
        main_page.click_yandex()

        # проверили, что открылась вторая вкладка в браузере
        assert len(driver.window_handles) == 2
