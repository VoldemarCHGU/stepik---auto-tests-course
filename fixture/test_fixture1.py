from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nСейчас я тут 1")
        self.browser = webdriver.Chrome("../chromedriver.exe")

    @classmethod
    def teardown_class(self):
        print("Сейчас я тут 2")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('Сейчас я тут 3')
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('Сейчас я тут 4')
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("start 1")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit 2")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('start 3')
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('start 4')
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")
