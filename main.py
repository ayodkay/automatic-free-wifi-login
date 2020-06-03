from selenium import webdriver
import time
import subprocess
import urllib3
import json


class FreeWifi:
    def __init__(self):
        self.browser = webdriver.Chrome()

    def set_up(self):
        self.browser.get(url='http://www.msftconnecttest.com/redirect')

    def login_user(self):
        self.set_up()
        try:
            self.browser.find_element_by_id('formVideo').submit()
            time.sleep(60)
            self.browser.close()
        except:
            if "#NET-CLARO-WIFI" not in subprocess.check_output("netsh wlan show interface").decode():
                print("please connect to #NET_CLARO_WIFI")
            self.browser.close()


if __name__ == '__main__':
    while True:
        try:
            http = urllib3.PoolManager()
            request = http.request('GET', 'google.com')

            if json.loads(request.data.decode()).get("status") == 400:
                FreeWifi().login_user()
            else:
                continue
        except:
            pass
