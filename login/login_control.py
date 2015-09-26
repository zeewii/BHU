#coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

#作者：孔志兵
#描述：该模块实现路由器管理界面的登录和推出

#描述：得到输入框中的默认的用户名和密码
#输出：用户名和密码框中默认值
def get_user(self):
    driver = self.driver
    driver.implicitly_wait(10)
    username = driver.find_element_by_name('username').text
    password = driver.find_element_by_id('focus_password').text
    return username,password


#描述：实现用户名和密码的输入
#usr----登录用户名
#pwd----登录密码
def set_user(self,usr,pwd):
    driver = self.driver
    driver.implicitly_wait(10)
    driver.find_element_by_name('username').clear()
    driver.find_element_by_name('username').send_keys(usr)
    driver.find_element_by_id('focus_password').clear()
    driver.find_element_by_id('focus_password').send_keys(pwd)

#描述：实现用户名和密码的提交动作
def submit(self):
    driver = self.driver
    driver.find_element_by_css_selector('input.cbi-button.cbi-button-apply').click()
    driver.implicitly_wait(10)

#描述：实现管理界面的输出
def logout(self):
    driver = self.driver
    driver.find_element_by_link_text(u'退出').click()

#描述： 提取登录出错信息并输出判断结果
def get_error(self):
    driver = self.driver
    driver.implicitly_wait(10)
    error = driver.find_element_by_class_name("error").text
    if u"无效的用户名和/或密码!" in error:
        print u"错误提示结果与期望一致，结果正常"
    else:
        raise ValueError(u"错误提示与期望不一致")

#描述： 点击登录界面reset按钮
def login_reset(self):
    driver = self.driver
    driver.find_element_by_css_selector('input.cbi-button.cbi-button-reset').click()
    driver.implicitly_wait(10)


__author__ = 'kzb'