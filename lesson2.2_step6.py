from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


def test():
    try:
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/selects1.html"
        browser.get(link)

        x1 = int(browser.find_element_by_id("num1").text)
        x2 = int(browser.find_element_by_id("num2").text)
        select = Select(browser.find_element_by_id("dropdown"))
        select.select_by_value(str(x1 + x2))
        browser.find_element_by_class_name("btn.btn-default").click()
    # except Exception as err:
    #     print(err)
    finally:
        time.sleep(10)
        browser.quit()
        print("Все процессы завершены...")


test()
