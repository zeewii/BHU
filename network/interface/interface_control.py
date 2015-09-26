#coding=utf-8
#描述：该模块为接口页面设置的模块控制层
#作者：曾祥卫

from selenium import webdriver
from login import login_control
import time,os,commands
from connect import ssh
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from data import data
from publicControl import public_control


#####################################
#以下为接口页面设置
#####################################

#编号：Func_interface_01
#描述：进入网络页面-移动鼠标到“网络”，点击“接口”，进入接口页面
#输入：self
#输出：None
def interface_menu(self):
    public_control.menu(self,u"网络",u"接口")

#编号：Func_interface_02
#描述：点击接口页面中LAN-连接按钮
#输入：self
#输出：None
def lan_connect(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #点击LAN上的“连接”按钮
        lan_connect_path = u"(//input[@value='连接'])[1]"
        driver.find_element_by_xpath(lan_connect_path).click()
        time.sleep(20)
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"点击LAN上的连接按钮失败，原因如下：\n%s"%e

#编号：Func_interface_03
#描述：点击接口页面中LAN-关闭按钮
#输入：self
#输出：None
def lan_stop(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #点击LAN上的“关闭”按钮
        lan_stop_path = u"(//input[@value='关闭'])[1]"
        driver.find_element_by_xpath(lan_stop_path).click()
        #获取页面上的警告信息
        alert=driver.switch_to_alert()
        #点击警告信息的确认
        alert.accept()
        driver.implicitly_wait(5)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"点击LAN上的关闭按钮失败，原因如下：\n%s"%e

#编号：Func_interface_04
#描述：点击接口页面中LAN-修改按钮,进入LAN设置页面
#输入：self
#输出：None
def lan_edit(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #点击LAN上的“修改”按钮
        driver.find_element_by_id("lan-ifc-edit").click()
        driver.implicitly_wait(5)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"点击接口页面中LAN-修改按钮失败，原因如下：\n%s"%e

#编号：Func_interface_05
#描述：获取lan口状态信息
#输入：self
#输出：info:lan的状态信息
def get_lan_info(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #获取lan口信息
        info = driver.find_element_by_id("lan-ifc-description").text
        #信息返回给函数
        return info
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"获取lan口状态信息失败，原因如下：\n%s"%e

#编号：Func_interface_06
#描述：点击接口页面中WAN-连接按钮
#输入：self
#输出：None
def wan_connect(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #点击WAN上的“连接”按钮
        wan_connect_path = u"(//input[@value='连接'])[2]"
        driver.find_element_by_xpath(wan_connect_path).click()
        time.sleep(20)
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"点击WAN上的连接按钮失败，原因如下：\n%s"%e

#编号：Func_interface_07
#描述：点击接口页面中WAN-关闭按钮
#输入：self
#输出：None
def wan_stop(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #点击WAN上的“关闭”按钮
        wan_stop_path = u"(//input[@value='关闭'])[2]"
        driver.find_element_by_xpath(wan_stop_path).click()
        #获取页面上的警告信息
        alert = driver.switch_to_alert()
        #点击警告信息的确认
        alert.accept()
        driver.implicitly_wait(5)
    #捕捉异常并打印异常信息
    except Exception, e:
        print u"点击WAN上的关闭按钮失败，原因如下：\n%s"%e

#编号：Func_interface_08
#描述：点击接口页面中WAN-修改按钮,进入WAN设置页面
#输入：self
#输出：None
def wan_edit(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #点击WAN上的“修改”按钮
        driver.find_element_by_id("wan-ifc-edit").click()
        driver.implicitly_wait(5)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"点击接口页面中WAN-修改按钮，原因如下：\n%s"%e

#编号：Func_interface_09
#描述：获取wan口状态信息
#输入：self
#输出：info:wan的状态信息
def get_wan_info(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #获取wan口信息
        info = driver.find_element_by_id("wan-ifc-description").text
        #信息返回给函数
        return info
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"获取wan口状态信息失败，原因如下：\n%s"%e





__author__ = 'zeng'