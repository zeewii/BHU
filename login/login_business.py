#coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from data import data
import login_control



#作者：张均
#描述：登录模块的逻辑处理


#描述：打开路由器登录界面并登录，
#      此函数为可配置，方便路由器IP和密码有修改的情况下使用
#url为路由器的IP地址
#usr为登录用户名
#pwd为登录密码
def admin_login(self,url,usr,pwd):
    self.driver.get(url)
    login_control.set_user(self,usr,pwd)
    login_control.submit(self)


#描述：使用默认IP地址和用户名登录
#      此函数使用default_web_login.txt文件中的参数进行登录
def default_login(self):
    sheet = 'basic_conf'                      #数据存放的工作表名
    url = data.xls_data(sheet,3,1)              #路由器登录IP
    general_usr = data.xls_data(sheet,5,1)      #普通用户用户名
    general_pwd = data.xls_data(sheet,6,1)      #普通用户密码
    self.driver.get('http://%s'%url)
    login_control.set_user(self,general_usr,general_pwd)
    login_control.submit(self)


__author__ = 'Administrator'