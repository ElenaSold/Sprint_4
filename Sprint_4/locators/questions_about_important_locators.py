from selenium.webdriver.common.by import By

class TestLocatorsQuestions:
    # вопрос "Сколько это стоит? и как оплатить?"
    q_how_much = (By.ID, "accordion__heading-0")
    # вопрос "Хочу сразу несколько..."
    q_want_some_scooters = (By.ID, "accordion__heading-1")
    # вопрос "Как рассчитывается время?"
    q_how_calculated = (By.ID, "accordion__heading-2")
    # вопрос "Можно ли заказать самокат прямо сегодня?"
    q_can_i_order = (By.ID, "accordion__heading-3")
    # вопрос "Можно ли продлить заказ..."
    q_possible_to_prolong = (By.ID, "accordion__heading-4")
    # вопрос "Вы привозите зарядку?"
    q_do_u_bring_charger = (By.ID, "accordion__heading-5")
    # вопрос "Можно ли отменить заказ?"
    q_cancel_an_order = (By.ID, "accordion__heading-6")
    # вопрос "Я живу за МКАДом, привезете?"
    q_bring_from_mcad = (By.ID, "accordion__heading-7")
    # ответ на вопрос "Сколько это стоит? и как оплатить?"
    a_how_much = (By.ID, "accordion__panel-0")
    # ответ на вопрос "Хочу сразу несколько..."
    a_want_some_scooters = (By.ID, "accordion__panel-1")
    # ответ на вопрос "Как рассчитывается время?"
    a_how_calculated = (By.ID, "accordion__panel-2")
    # ответ на вопрос "Можно ли заказать самокат прямо сегодня?"
    a_can_i_order = (By.ID, "accordion__panel-3")
    # ответ на вопрос "Можно ли продлить заказ..."
    a_possible_to_prolong = (By.ID, "accordion__panel-4")
    # ответ на вопрос "Вы привозите зарядку?"
    a_do_u_bring_charger = (By.ID, "accordion__panel-5")
    # ответ на вопрос "Можно ли отменить заказ?"
    a_cancel_an_order = (By.ID, "accordion__panel-6")
    # ответ на вопрос "Я живу за МКАДом, привезете?"
    a_bring_from_mcad = (By.ID, "accordion__panel-7")
