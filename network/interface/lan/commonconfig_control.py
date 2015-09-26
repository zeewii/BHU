#coding=utf-8
#描述：该模块为LAN设置页面中的一般设置的模块控制层
#作者：曾祥卫

from selenium import webdriver
from login import login_control
import time,os,commands
from connect import ssh
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


#编号：Func_lan_01
#描述：点击LAN设置页面中一般设置下的基本设置
#输入：self
#输出：None
def lan_commonconfig_generalsetup(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #点击LAN设置页面中一般设置下的基本设置
        driver.find_element_by_xpath(".//*[@id='tab.network.lan.general']/a").click()
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"进入LAN设置页面中一般设置下的基本设置失败，原因如下：\n%s"%e

#编号：Func_lan_02
#描述：点击LAN设置页面中一般设置下的高级设置
#输入：self
#输出：None
def lan_commonconfig_advancedsettings(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #点击LAN设置页面中一般设置下的基本设置
        driver.find_element_by_xpath(".//*[@id='tab.network.lan.advanced']/a").click()
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"进入LAN设置页面中一般设置下的高级设置失败，原因如下：\n%s"%e

#编号：Func_lan_05
#描述：设置路由器LAN口ip
#输入：self,ip-设置的ip地址
#输出：None
def set_lan_ip(self,ip):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #设置路由器LAN口的ip
        driver.find_element_by_id("cbid.network.lan.ipaddr").clear()
        driver.find_element_by_id("cbid.network.lan.ipaddr").send_keys(ip)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"设置ip失败，原因如下：\n%s"%e

#编号：Func_lan_06
#描述：获取路由器LAN口ip
#输入：self
#输出：Ip-路由器LAN口ip
def get_lan_ip(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #获取路由器LAN口的ip
        ip = driver.find_element_by_id("cbid.network.lan.ipaddr").get_attribute("value")
        #将ip地址返回给函数
        return ip
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"获取ip失败，原因如下：\n%s"%e

#编号：Func_lan_07
#描述：设置路由器LAN口A,B,C类子网掩码
#输入：self ,mode为子网掩码类型:A,B,C类
#输出：None
def set_lan_netmask(self,mode):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #子网掩码选择A类：255.0.0.0
        m = driver.find_element_by_id("cbi.combobox.cbid.network.lan.netmask")
        #子网掩码选择A类：255.0.0.0
        if mode == 'A':
            m.find_element_by_xpath("//option[@value='255.0.0.0']").click()
        #子网掩码选择A类：255.255.0.0
        elif mode == 'B':
            m.find_element_by_xpath("//option[@value='255.255.0.0']").click()
        #子网掩码选择A类：255.255.255.0
        elif mode == 'C':
            m.find_element_by_xpath("//option[@value='255.255.255.0']").click()
        else:
            print u"mode类型请输入A，B，C"
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"设置路由器LAN口A,B,C类子网掩码失败，原因如下：\n%s"%e

#编号：Func_lan_08
#描述：设置路由器LAN口ip和自定义子网掩码
#输入：self , ip-LAN口ip,netmask:设置的自定义子网掩码
#输出：None
def set_lan_custom_netmask(self,ip,netmask):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #设置路由器LAN口的ip
        driver.find_element_by_id("cbid.network.lan.ipaddr").clear()
        driver.find_element_by_id("cbid.network.lan.ipaddr").send_keys(ip)
        #子网掩码选择自定义
        m = driver.find_element_by_id("cbi.combobox.cbid.network.lan.netmask")
        m.find_element_by_xpath("//option[@value='']").click()
        #输入测试的子网掩码
        driver.find_element_by_id("cbid.network.lan.netmask").clear()
        driver.find_element_by_id("cbid.network.lan.netmask").send_keys(netmask)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"设置路由器LAN口ip和自定义子网掩码失败，原因如下：\n%s"%e

#编号：Func_lan_09
#描述：获取路由器LAN口子网掩码
#输入：self
#输出：Netmask-LAN口子网掩码
def get_lan_netmask(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #获取路由器LAN口子网掩码
        netmask = driver.find_element_by_id("cbid.network.lan.netmask").get_attribute("value")
        #将子网掩码返回给函数
        return netmask
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"获取路由器LAN口子网掩码失败，原因如下：\n%s"%e

#编号：Func_lan_10
#描述：设置路由器LAN口广播地址
#输入：self ,broadcast: 路由器LAN口广播地址
#输出：None
def set_lan_broadcast(self,broadcast):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #设置路由器LAN口广播地址
        driver.find_element_by_id("cbid.network.lan.broadcast").clear()
        driver.find_element_by_id("cbid.network.lan.broadcast").send_keys(broadcast)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"设置路由器LAN口广播地址失败，原因如下：\n%s"%e

#编号：Func_lan_11
#描述：获取路由器LAN口mac地址
#输入：self
#输出：broadcast: 路由器LAN口广播地址
def get_lan_broadcast(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #获取路由器LAN口广播地址
        mac = driver.find_element_by_id("cbid.network.lan.broadcast").get_attribute("value")
        #将路由器LAN口广播地址
        return mac
    except Exception,e:
        print u"获取路由器LAN口广播地址失败，原因如下：\n%s"%e

#编号：Func_lan_12
#描述：克隆路由器LAN口mac地址
#输入：self , mac:克隆的mac地址
#输出：None
def set_lan_mac(self,mac):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #设置路由器LAN口mac地址
        driver.find_element_by_id("cbid.network.lan.macaddr").clear()
        driver.find_element_by_id("cbid.network.lan.macaddr").send_keys(mac)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"设置路由器LAN口mac地址失败，原因如下：\n%s"%e

#编号：Func_lan_13
#描述：获取路由器LAN口mac地址
#输入：self
#输出：mac-路由器LAN口mac地址
def get_lan_mac(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #获取路由器LAN口mac地址
        mac = driver.find_element_by_id("cbid.network.lan.macaddr").get_attribute("placeholder")
        #将路由LAN口的mac返回给函数
        return mac
    except Exception,e:
        print u"获取路由器LAN口mac地址失败，原因如下：\n%s"%e

#编号：Func_lan_14
#描述：设置路由器LAN口mtu值
#输入：self , mtu:设置LAN口的mtu值
#输出：None
def set_lan_mtu(self,mtu):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #设置路由器LAN口mtu值
        driver.find_element_by_id("cbid.network.lan.mtu").clear()
        driver.find_element_by_id("cbid.network.lan.mtu").send_keys(mtu)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"设置路由器LAN口mtu值失败，原因如下：\n%s"%e

#编号：Func_lan_15
#描述：获取路由器LAN口的mtu值
#输入：self
#输出：mtu-LAN口的mtu值
def get_lan_mtu(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #获取路由器LAN口的mtu值
        mtu = driver.find_element_by_id("cbid.network.lan.mtu").get_attribute("placeholder")
        #将路由LAN口的mtu值返回给函数
        return mtu
    except Exception,e:
        print u"获取路由器LAN口的mtu值失败，原因如下：\n%s"%e








__author__ = 'zeng'
