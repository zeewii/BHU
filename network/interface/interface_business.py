#coding=utf-8
#描述：该模块为接口的业务逻辑模块.
#作者：曾祥卫

from selenium import webdriver
from data import data
from login import login_control
import interface_control,interface_network_control
import time

#描述:打开浏览器进入路由器的web页面
def open_router_web(self,ip):
    try:
        driver = self.driver
        #打开路由器的web页面
        driver.get('http://%s'%ip)
        driver.implicitly_wait(10)
     #捕捉异常并打印异常信息
    except Exception,e:
        print u"打开浏览器进入路由器页面失败，原因如下：\n%s"%e

#描述：登录路由并进入接口页面
def goin_interface(self):
    try:
        #获取默认web页面登录的ip，用户名和密码
        web_user_password = data.default_web_user_password()
        #登录路由
        login_control.set_user(self,web_user_password[1],web_user_password[2])
        login_control.submit(self)
        #进入接口页面
        interface_control.interface_menu(self)
        time.sleep(5)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"登录路由并进入接口页面失败，原因如下：\n%s"%e

#描述：使用默认ip登录接口页面
def goin_default_interface(self):
    try:
        web_user_password = data.default_web_user_password()
        open_router_web(self,web_user_password[0])
        goin_interface(self)
     #捕捉异常并打印异常信息
    except Exception,e:
        print u"使用默认ip登录接口页面失败，原因如下：\n%s"%e


###############################################
#以下是接口页面的测试步骤
###############################################

#描述：测试用例100msh0053测试步骤
def step_100msh0053(self):
    try:
        #获取LAN口信息
        driver = self.driver
        driver.implicitly_wait(10)
        text = interface_control.get_lan_info(self)
        #创建一个文件，以写打开
        f = file('LAN_description.txt', 'w')
        #以utf-8编码写入,将LAN接口总览信息保持在LAN_description.txt的文件中
        f.write(text.encode('utf-8'))
        f.close()
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"获取LAN接口总览信息失败，原因如下：\n%s"%e










__author__ = 'root'
