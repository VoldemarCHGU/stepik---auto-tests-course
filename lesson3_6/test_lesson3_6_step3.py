import math
import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Указаны полные ссылки для дальнейшего расширения с такой же проверкой
# т.е. если есть другие ссылки (не только отличающиеся номера)
# можно из файла/БД. Пока так
link_test = ["https://stepik.org/lesson/236895/step/1", \
             "https://stepik.org/lesson/236896/step/1", \
             "https://stepik.org/lesson/236897/step/1", \
             "https://stepik.org/lesson/236898/step/1", \
             "https://stepik.org/lesson/236899/step/1", \
             "https://stepik.org/lesson/236903/step/1", \
             "https://stepik.org/lesson/236904/step/1", \
             "https://stepik.org/lesson/236905/step/1"]


# выведено отдельно, т.к. формулу поменять тут легче при изменении
def correct_answer():
    return str(math.log(int(time.time())))


@pytest.fixture(scope="function")
def browser():
    # print("\n_____start browser for test..______")
    browser = webdriver.Chrome("../chromedriver.exe")
    browser.implicitly_wait(5)
    yield browser
    # print("\n_____quit browser..______")
    browser.quit()


@pytest.mark.parametrize('links', link_test)
def test_see(browser, links):
    link = f"{links}"
    browser.get(link)

    textarea = WebDriverWait(browser, 10).until \
        (EC.presence_of_element_located((By.CSS_SELECTOR, ".textarea")))
    textarea.send_keys(correct_answer())

    send_btn = browser.find_element_by_class_name("submit-submission").click()

    # ждём появления фидбека
    WebDriverWait(browser, 10).until \
        (EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
    feedback = browser.find_element_by_class_name("smart-hints__hint").text
    assert 'Correct!' == feedback, f'Получен другот ответ: {feedback}'
