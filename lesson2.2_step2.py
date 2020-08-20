import math
import time

from selenium import webdriver


def scroll_to_element(browser, element):
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def test():
    try:
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/execute_script.html"
        browser.get(link)

        x_element = int(browser.find_element_by_id("input_value").text)
        y = calc(x_element)

        browser.find_element_by_id("answer").send_keys(y)

        checkbox = browser.find_element_by_id("robotCheckbox")
        scroll_to_element(browser, checkbox)
        checkbox.click()

        radiobutton = browser.find_element_by_id("robotsRule")
        scroll_to_element(browser, radiobutton)
        radiobutton.click()

        submit = browser.find_element_by_class_name("btn.btn-primary")
        scroll_to_element(browser, submit)
        submit.click()

    finally:
        time.sleep(10)
        browser.quit()
        print("Все процессы завершены...")


test()
