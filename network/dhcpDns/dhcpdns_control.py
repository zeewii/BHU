#coding=utf-8
#描述：该模块为dhcp/dns页面设置的模块控制层,包括域名绑定页面设置，静态地址分配页面设置
#作者：曾祥卫

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from login import login_control
import time,os,commands
from connect import ssh
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from data import data
from publicControl import public_control


#####################################
#以下为域名绑定页面设置
#####################################

#编号：Func_dhcpdns_01
#描述：进入网络页面-移动鼠标到网络，点击DHCP/DNS进入DHCP/DNS页面
#输入：self
#输出：None
def dhcpdns_menu(self):
    public_control.menu(self,u"网络",u"DHCP/DNS")

#编号：Func_dhcpdns_02
#描述：点击域名绑定页面上的添加按钮
#输入：self
#输出：None
def add_domain_hijacking_settings(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #点击域名绑定页面上的添加按钮
        driver.find_element_by_xpath(".//*[@id='cbi-dhcp-domain']/div[2]/div/input").click()
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"点击域名绑定页面上的添加按钮失败，原因如下：\n%s"%e

#编号：Func_dhcpdns_03
#描述：域名绑定页面上中第一组输入域名和对应的ip
#输入：self,domain-需要绑定的域名,ip-需要绑定的ip
#输出：None
def set_first_dhs(self,domain,ip):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #域名绑定页面上中第一组输入域名
        driver.find_element_by_id("cbid.dhcp.cfg08f37d.name").clear()
        driver.find_element_by_id("cbid.dhcp.cfg08f37d.name").send_keys(domain)
        driver.implicitly_wait(10)
        #域名绑定页面上中第一组输入ip
        driver.find_element_by_id("cbid.dhcp.cfg08f37d.ip").clear()
        driver.find_element_by_id("cbid.dhcp.cfg08f37d.ip").send_keys(ip)
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"点击域名绑定页面上的添加按钮失败，原因如下：\n%s"%e

#编号：Func_dhcpdns_04
#描述：域名绑定页面上中所有组输入对应的域名和ip
#输入：self,domain-需要绑定的域名,ip-需要绑定的ip
#输出：None
def set_all_dhs(self,domain,ip):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        m = []
        n = []
        #取所有class name为cbi-input-text的元素，即取出要输入的所有输入框
        inputs = driver.find_elements_by_class_name("cbi-input-text")
        #逐个取出每个输入框
        for input in inputs:
            #取出每个输入框的id元素
            id = input.get_attribute('id')
            #取id字符串内容的第4段做判断
            s = id.split('.')[3]
            #如果为域名输入框
            if s == 'name':
                #把所有域名输入框的元素加入m
                m.append(input)
            #如果为ip输入框
            if s == 'ip':
                #把所有ip输入框的元素加入n
                n.append(input)
        #列表从第一组开始取值
        i = 0
        #当i小于元素列表长度时循环
        while(i<len(m)):
            #每个域名输入框输入对应的域名
            m[i].clear()
            m[i].send_keys(domain[i])
            #每个ip输入框输入对应的ip
            n[i].clear()
            n[i].send_keys(ip[i])
            i +=1
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"域名绑定页面上中所有组输入域名和对应的ip失败，原因如下：\n%s"%e

#编号：Func_dhcpdns_05
#描述：域名绑定页面上第一组点击删除按钮
#输入：self
#输出：None
def delete_first_dhs(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #域名绑定页面上第一组点击删除按钮
        driver.find_element_by_name("cbi.rts.dhcp.cfg08f37d").click()
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"域名绑定页面上第一组点击删除按钮失败，原因如下：\n%s"%e

#编号：Func_dhcpdns_06
#描述：域名绑定页面上所有组点击删除按钮
#输入：self
#输出：None
def delete_all_dhs(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #取删除键所有的元素
        tmp = driver.find_elements_by_css_selector(".cbi-button.cbi-button-remove")
        i = 0
        #当i小于所有元素的个数时进行循环
        while(i<len(tmp)):
            #再次取当前页面的删除键的所有元素
            inputs = driver.find_elements_by_css_selector(".cbi-button.cbi-button-remove")
            #点击最后一个删除按钮
            inputs[-1].click()
            i +=1
            driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"域名绑定页面上所有组点击删除按钮失败，原因如下：\n%s"%e


#####################################
#以下为静态地址分配页面设置
#####################################

#编号：Func_dhcpdns_07
#描述：点击静态地址分配页面上的添加按钮
#输入：self
#输出：None
def add_static_leases(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #点击静态地址分配页面上的添加按钮
        driver.find_element_by_xpath(".//*[@id='cbi-dhcp-host']/div[2]/div/input").click()
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"点击静态地址分配页面上的添加按钮失败，原因如下：\n%s"%e

#编号：Func_dhcpdns_08
#描述：静态地址分配页面上中第一组输入mac和对应的ip
#输入：self,mac-需要绑定的域名,ip-需要指定的ip
#输出：None
def set_first_static_leases(self,mac,ip):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #定位mac地址输入框
        m = Select(driver.find_element_by_id("cbi.combobox.cbid.dhcp.cfg08fe63.mac"))
        #在下拉框中选择自定义
        m.select_by_visible_text(u"-- 自定义 --")
        #输入mac地址
        driver.find_element_by_id("cbid.dhcp.cfg08fe63.mac").clear()
        driver.find_element_by_id("cbid.dhcp.cfg08fe63.mac").send_keys(mac)
        #定位ip地址输入框
        n = Select(driver.find_element_by_id("cbi.combobox.cbid.dhcp.cfg08fe63.ip"))
        #在下拉框中选择自定义
        n.select_by_visible_text(u"-- 自定义 --")
        #输入ip地址
        driver.find_element_by_id("cbid.dhcp.cfg08fe63.ip").clear()
        driver.find_element_by_id("cbid.dhcp.cfg08fe63.ip").send_keys(ip)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"静态地址分配页面上中第一组输入mac和对应的ip失败，原因如下：\n%s"%e

#编号：Func_dhcpdns_09
#描述：静态地址分配页面上中所有组输入mac和对应的ip
#输入：self,mac-需要绑定的域名,ip-需要指定的ip
#输出：None
def set_all_static_leases(self,mac,ip):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        m = []
        m1 = []
        n = []
        n1 = []
        #取所有class name为cbi-input-select的元素，即取出要输入的所有输入框
        inputs = driver.find_elements_by_class_name("cbi-input-select")
        #逐个取出每个输入框
        for input in inputs:
            #取出每个输入框的id元素
            id = input.get_attribute('id')
            #取id字符串内容的第6段做判断
            s = id.split('.')[5]
            #如果为mac输入框
            if s == 'mac':
                #把所有域名输入框的元素加入m
                m.append(input)
                #把对应的id元素的值加入m1
                s1=id.split('combobox.')[1]
                m1.append(s1)
            #如果为ip输入框
            if s == 'ip':
                #把所有ip输入框的元素加入n
                n.append(input)
                #把对应的id元素的值加入n1
                s2=id.split('combobox.')[1]
                n1.append(s2)
        #列表从第一组开始取值
        i = 0
        #当i小于元素列表长度时循环
        while(i<len(m)):
            #定位每个mac地址输入框
            a = Select(m[i])
            #在每个下拉框中选择自定义
            a.select_by_visible_text(u"-- 自定义 --")
            #在每个输入框中输入对应的mac地址
            driver.find_element_by_id(m1[i]).clear()
            driver.find_element_by_id(m1[i]).send_keys(mac[i])
            #定位每个ip地址输入框
            b = Select(n[i])
            #在每个下拉框中选择自定义
            b.select_by_visible_text(u"-- 自定义 --")
            #在每个输入框中输入对应的ip地址
            driver.find_element_by_id(n1[i]).clear()
            driver.find_element_by_id(n1[i]).send_keys(ip[i])
            #i加1进行下一个循环
            i +=1
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"静态地址分配页面上中所有组输入mac和对应的ip失败，原因如下：\n%s"%e

#编号：Func_dhcpdns_10
#描述：静态地址分配页面上点击第一组删除按钮
#输入：self
#输出：None
def delete_first_static_leases_(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #静态地址分配页面上点击第一组删除按钮
        driver.find_element_by_name("cbi.rts.dhcp.cfg08fe63").click()
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"静态地址分配页面上点击第一组删除按钮失败，原因如下：\n%s"%e

#编号：Func_dhcpdns_11
#描述：静态地址分配页面上点击所有组删除按钮
#输入：self
#输出：None
def delete_all_static_leases_(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #取删除键所有的元素
        tmp = driver.find_elements_by_css_selector(".cbi-button.cbi-button-remove")
        i = 0
        #当i小于所有元素的个数时进行循环
        while(i<len(tmp)):
            #再次取当前页面的删除键的所有元素
            inputs = driver.find_elements_by_css_selector(".cbi-button.cbi-button-remove")
            #点击最后一个删除按钮
            inputs[-1].click()
            i +=1
            driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"静态地址分配页面上点击所有组删除按钮失败，原因如下：\n%s"%e

#编号：Func_dhcpdns_12
#描述：点击“保存&应用”提交表单
#输入：self
#输出：None
def apply(self):
    public_control.apply(self)

#编号：Func_dhcpdns_13
#描述：点击“复位”
#输入：self
#输出：None
def reset(self):
    public_control.reset(self)

#编号：Func_dhcpdns_14
#描述：获取页面弹出的警告框
#输入：self
#输出：Alert(警告框)
def get_alert(self):
    try:
        driver = self.driver
        #获取页面上的警告信息
        alert=driver.switch_to_alert()
        #返回警告信息
        return alert
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"获取页面弹出的警告框失败，原因如下：\n%s"%e



__author__ = 'zeng'