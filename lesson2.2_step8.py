import os
import time

from selenium import webdriver


def scroll_to_element(browser, element):
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)


def test():
    try:
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/file_input.html"
        browser.get(link)

        current_dir = os.path.abspath(
            os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
        file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

        names = ["firstname", "lastname", "email"]
        for i in names:
            browser.find_element_by_name(i).send_keys("*")

        browser.find_element_by_css_selector("[type='file']").send_keys(file_path)
        submit = browser.find_element_by_class_name("btn.btn-primary")

        submit.click()
    finally:
        time.sleep(10)
        browser.quit()
        print("Все процессы завершены...")


test()
