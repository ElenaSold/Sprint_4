from selenium.webdriver.common.by import By

class TestLocatorsMainPage:
    # заголовок "Самокат на пару дней"
    header_scooter_for_couple_days = (By.XPATH, ".//div[@class='Home_Header__iJKdX']")

    # кнопка заказать в верхней части страницы
    order_button_at_the_top = (By.XPATH, ".//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']")

    # кнопка заказать внизу страницы
    order_button_at_the_bottom = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")

    # заголовок "Для кого самокат"
    header_for_whom = (By.XPATH, ".//div[@class='Order_Header__BZXOb']")

    # логотип Яндекс
    logo_yandex = (By.XPATH, ".//a[@rel='noopener noreferrer']")
