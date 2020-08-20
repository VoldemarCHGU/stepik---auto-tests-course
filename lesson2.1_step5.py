import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def decarator(func):
    try:
        browser = webdriver.Chrome()
    finally:
        func(browser).quit()
        print("Все процессы завершены...")


@decarator
def qqq(browser):
    try:

        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/get_attribute.html"
        browser.get(link)
        x_element = browser.find_element_by_id("treasure").get_attribute("valuex")

        y = calc(x_element)

        browser.find_element_by_id("answer").send_keys(y)
        browser.find_element_by_id("robotCheckbox").click()
        browser.find_element_by_id("robotsRule").click()
        browser.find_element_by_class_name("btn.btn-default").click()
        time.sleep(10)
    except Exception as err:
        print(err)
    finally:
        return browser
