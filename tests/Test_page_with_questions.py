from Pages.Page_with_Questions import PageWithQuestions
from Pages.base_page import BasePage
from locators.questions_about_important_locators import TestLocatorsQuestions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestQuestions:
    def test_show_answer_how_much(self, driver):

        # перешли на страницу приложения
        driver.get('https://qa-scooter.praktikum-services.ru/')

        # создали объект класса страницы с вопросами
        questions_page = PageWithQuestions(driver)

        # приняли куки
        base_page = BasePage(driver)
        base_page.click_cookie_button()

        # скролл до вопроса
        questions_page.scroll(TestLocatorsQuestions.q_how_much)

        # кликнули по вопросу "Сколько это стоит? и как оплатить?"
        questions_page.click_q(TestLocatorsQuestions.q_how_much)

        # ожидание отображения ответа
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocatorsQuestions.a_how_much))

        # проверили, что ответ на вопрос отображается
        assert questions_page.find_answer(TestLocatorsQuestions.a_how_much) and questions_page.text_answer(TestLocatorsQuestions.a_how_much) == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    def test_show_answer_want_some_scooters(self, driver):

        # перешли на страницу приложения
        driver.get('https://qa-scooter.praktikum-services.ru/')

        # создали объект класса страницы с вопросами
        questions_page = PageWithQuestions(driver)

        # приняли куки
        base_page = BasePage(driver)
        base_page.click_cookie_button()

        # скролл до вопроса
        questions_page.scroll(TestLocatorsQuestions.q_want_some_scooters)

        # кликнули по вопросу "Сколько это стоит? и как оплатить?"
        questions_page.click_q(TestLocatorsQuestions.q_want_some_scooters)

        # ожидание отображения ответа
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocatorsQuestions.a_want_some_scooters))

        # проверили, что ответ на вопрос отображается
        assert questions_page.find_answer(TestLocatorsQuestions.a_want_some_scooters) and questions_page.text_answer(TestLocatorsQuestions.a_want_some_scooters) == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    def test_show_answer_how_calculated(self, driver):

        # перешли на страницу приложения
        driver.get('https://qa-scooter.praktikum-services.ru/')

        # создали объект класса страницы с вопросами
        questions_page = PageWithQuestions(driver)

        # приняли куки
        base_page = BasePage(driver)
        base_page.click_cookie_button()

        # скролл до вопроса
        questions_page.scroll(TestLocatorsQuestions.q_how_calculated)

        # кликнули по вопросу "Сколько это стоит? и как оплатить?"
        questions_page.click_q(TestLocatorsQuestions.q_how_calculated)

        # ожидание отображения ответа
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocatorsQuestions.a_how_calculated))

        # проверили, что ответ на вопрос отображается
        assert questions_page.find_answer(TestLocatorsQuestions.a_how_calculated) and questions_page.text_answer(TestLocatorsQuestions.a_how_calculated) == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    def test_show_answer_can_i_order(self, driver):

        # перешли на страницу приложения
        driver.get('https://qa-scooter.praktikum-services.ru/')

        # создали объект класса страницы с вопросами
        questions_page = PageWithQuestions(driver)

        # приняли куки
        base_page = BasePage(driver)
        base_page.click_cookie_button()

        # скролл до вопроса
        questions_page.scroll(TestLocatorsQuestions.q_can_i_order)

        # кликнули по вопросу "Сколько это стоит? и как оплатить?"
        questions_page.click_q(TestLocatorsQuestions.q_can_i_order)

        # ожидание отображения ответа
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocatorsQuestions.a_can_i_order))

        # проверили, что ответ на вопрос отображается
        assert questions_page.find_answer(TestLocatorsQuestions.a_can_i_order) and questions_page.text_answer(TestLocatorsQuestions.a_can_i_order) == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    def test_show_answer_possible_to_prolong(self, driver):

        # перешли на страницу приложения
        driver.get('https://qa-scooter.praktikum-services.ru/')

        # создали объект класса страницы с вопросами
        questions_page = PageWithQuestions(driver)

        # приняли куки
        base_page = BasePage(driver)
        base_page.click_cookie_button()

        # скролл до вопроса
        questions_page.scroll(TestLocatorsQuestions.q_possible_to_prolong)

        # кликнули по вопросу "Сколько это стоит? и как оплатить?"
        questions_page.click_q(TestLocatorsQuestions.q_possible_to_prolong)

        # ожидание отображения ответа
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocatorsQuestions.a_possible_to_prolong))

        # проверили, что ответ на вопрос отображается
        assert questions_page.find_answer(TestLocatorsQuestions.a_possible_to_prolong) and questions_page.text_answer(TestLocatorsQuestions.a_possible_to_prolong) == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    def test_show_answer_do_u_bring_charger(self, driver):

        # перешли на страницу приложения
        driver.get('https://qa-scooter.praktikum-services.ru/')

        # создали объект класса страницы с вопросами
        questions_page = PageWithQuestions(driver)

        # приняли куки
        base_page = BasePage(driver)
        base_page.click_cookie_button()

        # скролл до вопроса
        questions_page.scroll(TestLocatorsQuestions.q_do_u_bring_charger)

        # кликнули по вопросу "Сколько это стоит? и как оплатить?"
        questions_page.click_q(TestLocatorsQuestions.q_do_u_bring_charger)

        # ожидание отображения ответа
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocatorsQuestions.a_do_u_bring_charger))

        # проверили, что ответ на вопрос отображается
        assert questions_page.find_answer(TestLocatorsQuestions.a_do_u_bring_charger) and questions_page.text_answer(TestLocatorsQuestions.a_do_u_bring_charger) == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    def test_show_answer_cancel_an_order(self, driver):

        # перешли на страницу приложения
        driver.get('https://qa-scooter.praktikum-services.ru/')

        # создали объект класса страницы с вопросами
        questions_page = PageWithQuestions(driver)

        # приняли куки
        base_page = BasePage(driver)
        base_page.click_cookie_button()

        # скролл до вопроса
        questions_page.scroll(TestLocatorsQuestions.q_cancel_an_order)

        # кликнули по вопросу "Сколько это стоит? и как оплатить?"
        questions_page.click_q(TestLocatorsQuestions.q_cancel_an_order)

        # ожидание отображения ответа
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocatorsQuestions.a_cancel_an_order))

        # проверили, что ответ на вопрос отображается
        assert questions_page.find_answer(TestLocatorsQuestions.a_cancel_an_order) and questions_page.text_answer(TestLocatorsQuestions.a_cancel_an_order) == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    def test_show_answer_bring_from_mcad(self, driver):

        # перешли на страницу приложения
        driver.get('https://qa-scooter.praktikum-services.ru/')

        # создали объект класса страницы с вопросами
        questions_page = PageWithQuestions(driver)

        # приняли куки
        base_page = BasePage(driver)
        base_page.click_cookie_button()

        # скролл до вопроса
        questions_page.scroll(TestLocatorsQuestions.q_bring_from_mcad)

        # кликнули по вопросу "Сколько это стоит? и как оплатить?"
        questions_page.click_q(TestLocatorsQuestions.q_bring_from_mcad)

        # ожидание отображения ответа
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocatorsQuestions.a_bring_from_mcad))

        # проверили, что ответ на вопрос отображается
        assert questions_page.find_answer(TestLocatorsQuestions.a_bring_from_mcad) and questions_page.text_answer(TestLocatorsQuestions.a_bring_from_mcad) == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
