#coding=utf-8
#描述：该模块为LAN设置页面中的DHCP服务器的模块控制层
#作者：曾祥卫

from selenium import webdriver
from login import login_control
import time,os,commands
from connect import ssh
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

#编号：Func_lan_03
#描述：点击LAN设置页面中DHCP服务器下的基本设置
#输入：self
#输出：None
def lan_dhcpserver_generalsetup(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #点击LAN设置页面中DHCP服务器下的基本设置
        driver.find_element_by_xpath(".//*[@id='tab.dhcp.lan.general']/a").click()
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"进入LAN设置页面中DHCP服务器下的基本设置失败，原因如下：\n%s"%e

#编号：Func_lan_04
#描述：点击LAN设置页面中DHCP服务器下的高级设置
#输入：self
#输出：None
def lan_dhcpserver_advancedsettings(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #点击LAN设置页面中DHCP服务器下的高级设置
        driver.find_element_by_xpath(".//*[@id='tab.dhcp.lan.advanced']/a").click()
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"进入LAN设置页面中DHCP服务器下的高级设置失败，原因如下：\n%s"%e

#编号：Func_lan_16
#描述：关闭或开启路由器DHCP server
#输入：self
#输出：None
def set_lan_dhcp_disable_enable(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #关闭或开启路由器DHCP server
        driver.find_element_by_id("cbid.dhcp.lan.ignore").click()
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"关闭或开启路由器DHCP server失败，原因如下：\n%s"%e

#编号：Func_lan_17
#描述：获取路由器DHCP server的状态
#输入：self
#输出：Status
def get_lan_dhcp_status(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #定位DHCP的元素
        m = driver.find_element_by_id("cbid.dhcp.lan.ignore")
        #判断是否选择勾选checkbox
        status = m.is_selected()
        #结果返回给函数
        return status
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"获取路由器DHCP server的状态失败，原因如下：\n%s"%e

#编号：Func_lan_18
#描述：设置DHCP起始基址
#输入：self, value-DHCP起始基址
#输出：None
def set_lan_dhcp_startip(self,value):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #设置DHCP起始基址
        driver.find_element_by_id("cbid.dhcp.lan.start").clear()
        driver.find_element_by_id("cbid.dhcp.lan.start").send_keys(value)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"设置DHCP起始基址失败，原因如下：\n%s"%e

#编号：Func_lan_19
#描述：获取DHCP起始基址
#输入：self
#输出：value-DHCP起始基址
def get_lan_dhcp_startip(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #获取DHCP起始基址
        value = driver.find_element_by_id("cbid.dhcp.lan.start").get_attribute("value")
        #将起始基址返回给函数
        return value
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"获取DHCP起始基址失败，原因如下：\n%s"%e

#编号：Func_lan_20
#描述：设置DHCP客户数
#输入：self,value-DHCP客户数
#输出：None
def set_lan_dhcp_limitip(self,value):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #设置DHCP客户数
        driver.find_element_by_id("cbid.dhcp.lan.limit").clear()
        driver.find_element_by_id("cbid.dhcp.lan.limit").send_keys(value)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"设置DHCP客户数失败，原因如下：\n%s"%e

#编号：Func_lan_21
#描述：获取DHCP客户数
#输入：self
#输出：value-DHCP客户数
def get_lan_dhcp_limitip(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #获取DHCP客户数
        value = driver.find_element_by_id("cbid.dhcp.lan.limit").get_attribute("value")
        #将客户数返回给函数
        return value
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"获取DHCP客户数失败，原因如下：\n%s"%e

#编号：Func_lan_22
#描述：设置DHCP server的过期时间
#输入：Self,time-DHCP server的过期时间
#输出：None
def set_lan_dhcp_leasetime(self,time):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #设置DHCP server的过期时间
        driver.find_element_by_id("cbid.dhcp.lan.leasetime").clear()
        driver.find_element_by_id("cbid.dhcp.lan.leasetime").send_keys(time)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"设置DHCP server的过期时间失败，原因如下：\n%s"%e

#编号：Func_lan_23
#描述：获取DHCP server的过期时间
#输入：self
#输出：time-DHCP server的过期时间
def get_lan_dhcp_leasetime(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #获取DHCP server的过期时间
        value = driver.find_element_by_id("cbid.dhcp.lan.leasetime").get_attribute("value")
        #将过期时间返回给函数
        return value
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"获取DHCP server的过期时间失败，原因如下：\n%s"%e

#编号：Func_lan_24
#描述：设置动态DHCP开启或关闭
#输入：self
#输出：None
def set_lan_dhcp_dynamicdhcp(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #设置动态DHCP开启或关闭
        driver.find_element_by_id("cbid.dhcp.lan.dynamicdhcp").click()
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"设置动态DHCP开启或关闭失败，原因如下：\n%s"%e

#编号：Func_lan_25
#描述：获取动态DHCP状态
#输入：self
#输出：status
def get_lan_dhcp_dynamicdhcp_status(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #定位动态DHCP的元素
        m = driver.find_element_by_id("cbid.dhcp.lan.dynamicdhcp")
        #判断是否选择勾选checkbox
        status = m.is_selected()
        #结果返回给函数
        return status
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"获取动态DHCP状态失败，原因如下：\n%s"%e

#编号：Func_lan_26
#描述：启用或禁用强制开启DHCP
#输入：self
#输出：None
def set_lan_dhcp_force(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #启用或禁用强制开启DHCP
        driver.find_element_by_id("cbid.dhcp.lan.force").click()
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"启用或禁用强制开启DHCP失败，原因如下：\n%s"%e

#编号：Func_lan_27
#描述：获取强制开启DHCP的状态
#输入：self
#输出：status
def get_lan_dhcp_force_status(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #定位强制开启DHCP的元素
        m = driver.find_element_by_id("cbid.dhcp.lan.force")
        #判断是否选择勾选checkbox
        status = m.is_selected()
        #结果返回给函数
        return status
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"获取强制开启DHCP的状态失败，原因如下：\n%s"%e




__author__ = 'zeng'
