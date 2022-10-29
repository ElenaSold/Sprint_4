class PageWithQuestions:

    # конструктор класса
    def __init__(self, driver):
        self.driver = driver

    #метод скроллит до конца страницы
    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # метод кликает по вопросу
    def click_q(self, question):
        self.driver.find_element(*question).click()

    #метод проверяет отображается ли ответ
    def find_answer(self, answer):
        return self.driver.find_element(*answer).is_displayed()

    #метод проверяет правильность текста в ответе
    def text_answer(self, answer):
        return self.driver.find_element(*answer).text

