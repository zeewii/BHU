#coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time
import login_control


class login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.url = "http://192.168.11.1"
        self.driver.get(self.url)
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_login_error(self):
        login_control.set_user(self,"100msh","111")
        login_control.submit(self)
        login_control.get_error(self)




    def tearDown(self):
            self.driver.quit()
            self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

__author__ = 'Administrator'
