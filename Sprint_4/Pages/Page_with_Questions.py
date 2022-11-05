from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class PageWithQuestions:

    # конструктор класса
    def __init__(self, driver):
        self.driver = driver

    #метод скроллит до вопроса
    def scroll(self, question):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(question))

        element = self.driver.find_element(*question)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # метод кликает по вопросу
    def click_q(self, question):
        WebDriverWait(self.driver, 10).until(
             expected_conditions.element_to_be_clickable(question))
        self.driver.find_element(*question).click()

    #метод проверяет отображается ли ответ
    def find_answer(self, answer):
        return self.driver.find_element(*answer).is_displayed()

    #метод проверяет правильность текста в ответе
    def text_answer(self, answer):
        return self.driver.find_element(*answer).text

