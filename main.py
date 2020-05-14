from selenium import webdriver
import time


class FreeWifi:
    def __init__(self):
        self.browser = webdriver.Chrome()

    def set_up(self):
        self.browser.get(url='http://www.msftconnecttest.com/redirect')

    def login_user(self):
        self.set_up()
        self.browser.find_element_by_id('formVideo').submit()
        time.sleep(120)
        self.browser.close()


if __name__ == '__main__':
    while True:
        free = FreeWifi()

        free.login_user()

        time.sleep(960)
