#coding=utf-8

#描述：DMZ基本控制层
#作者：张均

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from publicControl import public_control
import time

#描述:DMZ配置页面菜单
#输入:self
#输出：None
def dmz_menu(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        public_control.menu(self,u"网络",u"DMZ")
    except (NoSuchElementException,Exception) as e:
        print u"页面跳转到DMZ失败,原因如下：%s" % e

#描述:DMZ开关状态获取
#输入:self
#输出：DMZ开关勾选时返回1，未勾选时返回0
def dmz_status(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
       dmz1 = driver.find_element_by_class_name("cbi-input-checkbox")
       status = dmz1.is_selected()
       return status
    except (NoSuchElementException,Exception) as e:
        print u"DMZ状态开关定位失败,原因如下：%s" % e

#描述:设置DMZ主机IP
#输入:self，host   host为主机IP
#输出：None
def set_host(self,host):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_id("cbid.firewall.cfg166ad0.dest_ip").clear()
        driver.find_element_by_id("cbid.firewall.cfg166ad0.dest_ip").send_keys(host)
    except (NoSuchElementException,Exception) as e:
        print u"DMZ主机IP输入框定位失败,原因如下：%s" % e

#描述:设置DMZ协议
#输入:self
#输出：返回元组(setall,settcpudp,settcp,setudp,seticmp)
def set_protocol(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        setall = driver.find_element_by_id("cbi-firewall-cfg166ad0-proto-all")
        settcpudp = driver.find_element_by_id("cbi-firewall-cfg166ad0-proto-tcp udp")
        settcp = driver.find_element_by_id("cbi-firewall-cfg166ad0-proto-tcp")
        setudp = driver.find_element_by_id("cbi-firewall-cfg166ad0-proto-udp")
        seticmp = driver.find_element_by_id("cbi-firewall-cfg166ad0-proto-icmp")
        return setall,settcpudp,settcp,setudp,seticmp
    except (NoSuchElementException,Exception) as e:
        print u"协议框定位失败,原因如下：%s" % e

#描述:设置DMZ端口
#输入:self，port port为需要设置的端口
#输出：None
def set_port(self,port):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_id("cbid.firewall.cfg166ad0.dest_port").clear()
        driver.find_element_by_id("cbid.firewall.cfg166ad0.dest_port").send_keys(port)
    except (NoSuchElementException,Exception) as e:
        print u"端口输入框定位失败,原因如下：%s" % e

#描述:DMZ错误数据警告窗口检查[此函数只在异常测试时使用]
#输入:self
#输出：打印错误信息
def have_alert(self):
    driver = self.driver
    try:
        alert = driver.switch_to_alert()
        alert.accept()
    except (NoSuchElementException,Exception) as e:
        print u"没有错误警告窗弹出，与期望结果不一致，原因如下：%s" % e

#描述:DMZ页面保存&应用按钮点击
#输入:self
#输出：打印错误信息
def dmz_apply(self):
    public_control.apply(self)
    time.sleep(5)


#描述:DMZ页面复位按钮点击
#输入:self
#输出：打印错误信息
def dmz_rst(self):
    public_control.reset(self)


__author__ = 'Administrator'
