from selenium.webdriver.common.by import By

class TestLocatorsMainPage:
    # заголовок "Самокат на пару дней"
    header_scooter_for_couple_days = (By.XPATH, ".//div[contains(@class, 'Home_Header')]")

    # кнопка заказать в верхней части страницы
    order_button_at_the_top = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")

    # кнопка заказать внизу страницы
    order_button_at_the_bottom = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")

    # заголовок "Для кого самокат"
    header_for_whom = (By.XPATH, ".//div[contains(@class, 'Order_Header')]")

    # логотип Яндекс
    logo_yandex = (By.XPATH, ".//a[@rel='noopener noreferrer']")
