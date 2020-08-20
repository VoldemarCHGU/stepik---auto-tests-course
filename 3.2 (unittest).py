import time
import unittest

from selenium import webdriver


class TestAbs(unittest.TestCase):

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        labels = ["First name*",
                  "Last name*",
                  "Email*",
                  "Phone:",
                  "Address:"]

        for text_label in labels:
            xpath = "//label[text()='{0}']/following-sibling::input".format(text_label)
            browser.find_element_by_xpath(xpath).send_keys(text_label)

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(2)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        browser.quit()
        assert "Congratulations! You have successfully registered!" == welcome_text

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        labels = ["First name*",
                  "Last name*",
                  "Email*",
                  "Phone:",
                  "Address:"]

        for text_label in labels:
            xpath = "//label[text()='{0}']/following-sibling::input".format(text_label)
            browser.find_element_by_xpath(xpath).send_keys(text_label)

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(2)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        browser.quit()
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text


if __name__ == "__main__":
    unittest.main()
