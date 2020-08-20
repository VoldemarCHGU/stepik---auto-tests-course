import math
from selenium import webdriver
import time

from selenium import webdriver


def scroll_to_element(browser, element):
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def test():
    try:
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/alert_accept.html"
        browser.get(link)
        browser.find_element_by_class_name("btn.btn-primary").click()
        confirm = browser.switch_to.alert
        confirm.accept()
        x_element = int(browser.find_element_by_id("input_value").text)
        y = calc(x_element)

        browser.find_element_by_id("answer").send_keys(y)

        submit = browser.find_element_by_class_name("btn.btn-primary")
        scroll_to_element(browser, submit)
        submit.click()
    finally:
        time.sleep(10)
        browser.quit()
        print("Все процессы завершены...")


test()
