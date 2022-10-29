from selenium.webdriver.common.by import By

class TestLocatorsMainPage:
    # кнопка заказать в верхней части страницы
    order_button_at_the_top = (By.XPATH, ".//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']")

    # кнопка заказать внизу страницы
    order_button_at_the_bottom = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")

    # заголовок "Для кого самокат"
    header_for_whom = (By.XPATH, ".//div[@class='Order_Header__BZXOb']")

    # логотип Яндекс
    logo_yandex = (By.XPATH, ".//a[@rel='noopener noreferrer']")
