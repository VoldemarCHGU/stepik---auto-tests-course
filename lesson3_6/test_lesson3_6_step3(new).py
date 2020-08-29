import math
import time

import pytest
from selenium import webdriver

test_links = []
with open("links_for_test") as f:
    test_links = f.readlines()
test_links = [line.rstrip() for line in test_links]


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome("../chromedriver.exe")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('url', test_links)
def test_selenium_3_6_3(browser, url):
    link = "{}".format(url)
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element_by_css_selector(".textarea").send_keys(str(math.log(int(time.time()))))
    browser.find_element_by_class_name("submit-submission").click()
    ans = browser.find_element_by_class_name("smart-hints__hint").text
    try:
        assert "Correct!" in ans
    except:
        with open("3_6_3_test_Errors.log", "a") as f:
            f.write(ans)
        raise AssertionError('Error! See "3_6_3_test_Errors.log"')
