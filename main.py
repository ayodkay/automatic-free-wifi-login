from selenium import webdriver


class FreeWifi:
    def __init__(self):
        self.browser = webdriver.   Chrome()

    def set_up(self):
        self.browser.get(url='http://www.msftconnecttest.com/redirect')
        self.browser.maximize_window()

    def login_user(self):
        self.set_up()
        self.browser.find_element_by_id('formVideo').submit()


if __name__ == '__main__':
    free = FreeWifi()

    free.login_user()
