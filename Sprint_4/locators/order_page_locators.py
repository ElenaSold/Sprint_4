from selenium.webdriver.common.by import By

class TestLocatorsOrder:
    # поле имя
    name = (By.XPATH, ".//input[@placeholder ='* Имя']")
    # поле фамилия
    surname = (By.XPATH, ".//input[@placeholder ='* Фамилия']")
    # поле адрес
    address = (By.XPATH, ".//input[@placeholder ='* Адрес: куда привезти заказ']")
    # поле станция
    station_field = (By.XPATH, ".//input[@placeholder ='* Станция метро']")
    # клик по станции Отрадное
    station_sokolniki = (By.XPATH, ".//button[@value='4']")
    # клик по станции Орехово
    station_aeroport = (By.XPATH, ".//button[@value='27']")
    # поле телефон
    phone = (By.XPATH, ".//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN']")
    # кнопка Далее
    button_next = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    # поле Когда привезти самокат
    date = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    # поле Срок аренды
    how_long = (By.XPATH, ".//span[@class='Dropdown-arrow']")
    # сутки
    day = (By.XPATH, ".//div[text()='сутки']")
    # 7 дней
    seven_days = (By.XPATH, ".//div[text()='семеро суток']")
    # цвет Черный жемчуг
    black_color = (By.ID, "black")
    # цвет Серая безысходность
    grey_color = (By.ID, "grey")
    # поле комментарий
    comment = (By.XPATH, ".//div[@class='Input_InputContainer__3NykH']/input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN']")
    # кнопка Заказать внизу формы
    button_order_under_the_form = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")
    # кнопка Да в окне подтверждения
    button_yes = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Да']")
    # окно Заказ оформлен
    confirm_window = (By.XPATH, ".//div[@class='Order_Modal__YZ-d3']")
    # логотип Самокат
    logo_scooter = (By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']")
    # заголовок на главной странице
    header_scooter = (By.XPATH, ".//div[@class='Home_Header__iJKdX']")