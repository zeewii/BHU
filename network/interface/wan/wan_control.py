#coding=utf-8
#描述：该模块为WAN设置页面中的模块控制层
#作者：曾祥卫

from selenium import webdriver
from login import login_control
import time,os,commands
from connect import ssh
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from publicControl import public_control

#####################################
#以下为WAN设置页面中页面设置
#####################################

#编号：Func_wan_01
#描述：点击WAN设置页面中一般设置下的基本设置
#输入：self
#输出：None
def wan_generalsetup(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #点击WAN设置页面中一般设置下的基本设置
        driver.find_element_by_xpath(".//*[@id='tab.network.wan.general']/a").click()
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"进入WAN设置页面中一般设置下的基本设置失败，原因如下：\n%s"%e

#编号：Func_wan_02
#描述：点击WAN设置页面中一般设置下的高级设置
#输入：self
#输出：None
def wan_advancedsettings(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #点击WAN设置页面中一般设置下的高级设置
        driver.find_element_by_xpath(".//*[@id='tab.network.wan.advanced']/a").click()
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"进入WAN设置页面中一般设置下的高级设置失败，原因如下：\n%s"%e

#编号：Func_wan_03
#描述：WAN设置页面中协议选择3种登录方式: dhcp,staticip,pppoe
#输入：self,mode:dhcp,静态ip,pppoe
#输出：None
def set_wan_protrocol(self,mode):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        a = driver.find_element_by_id("cbid.network.wan.proto")
        #WAN设置页面中协议选择dhcp
        if mode == 'dhcp':
            a.find_element_by_id("cbi-network-wan-proto-dhcp").click()
        #WAN设置页面中协议选择static ip
        elif mode == 'staticip':
            a.find_element_by_id("cbi-network-wan-proto-static").click()
        #WAN设置页面中协议选择pppoe
        elif mode == 'pppoe':
            a.find_element_by_id("cbi-network-wan-proto-pppoe").click()
        else:
            print u"mode类型请输入dhcp，staticip，pppoe"
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"WAN设置页面中协议选择3种登录方式失败，原因如下：\n%s"%e

#编号：Func_wan_04
#描述：WAN设置页面中切换协议时点击切换协议
#输入：self
#输出：None
def set_wan_switchprotocol(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #点击切换协议
        driver.find_element_by_id("cbid.network.wan._switch").click()
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"WAN设置页面中切换协议时点击切换协议失败，原因如下：\n%s"%e

#编号：Func_wan_05
#描述：WAN设置页面中协议为dhcp时设置路由器主机名
#输入：self,hostname-路由器对外的主机名
#输出：None
def set_wan_dhcp_hostname(self,hostname):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #dhcp时设置路由器主机名
        driver.find_element_by_id("cbid.network.wan.hostname").clear()
        driver.find_element_by_id("cbid.network.wan.hostname").send_keys(hostname)
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"WAN设置页面中协议为dhcp时设置路由器主机名失败，原因如下：\n%s"%e

#编号：Func_wan_06
#描述：WAN设置页面中协议为dhcp时获取路由器主机名
#输入：self
#输出：hostname-路由器对外的主机名
def get_wan_dhcp_hostname(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #dhcp时获取路由器主机名
        hostname = driver.find_element_by_id("cbid.network.wan.hostname").get_attribute('value')
        #将主机名返回给函数
        return hostname
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"WAN设置页面中协议为dhcp时获取路由器主机名失败，原因如下：\n%s"%e

#编号：Func_wan_07
#描述：WAN设置页面中协议为静态ip时设置WAN口ip地址
#输入：Self,ip-WAN口ip地址
#输出：None
def set_wan_staticip_ip(self,ip):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #设置WAN口ip地址
        driver.find_element_by_id("cbid.network.wan.ipaddr").clear()
        driver.find_element_by_id("cbid.network.wan.ipaddr").send_keys(ip)
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"WAN设置页面中协议为静态ip时设置WAN口ip地址失败，原因如下：\n%s"%e

#编号：Func_wan_08
#描述：WAN设置页面中协议为静态ip时获取WAN口ip地址
#输入：Self
#输出：ip-WAN口ip地址
def get_wan_staticip_ip(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #获取WAN口ip地址
        ip = driver.find_element_by_id("cbid.network.wan.ipaddr").get_attribute('value')
        #将ip地址返回给函数
        return ip
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"WAN设置页面中协议为静态ip时获取WAN口ip地址失败，原因如下：\n%s"%e

#编号：Func_wan_09
#描述：WAN设置页面中协议为静态ip时设置WAN口ip的子网掩码为A,B,C类
#输入：self ,mode:A,B,C类
#输出：None
def set_wan_staticip_netmask(self,mode):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        m = driver.find_element_by_id("cbi.combobox.cbid.network.wan.netmask")
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
        print u"WAN设置页面中协议为静态ip时设置WAN口ip的子网掩码为A,B,C类失败，原因如下：\n%s"%e

#编号：Func_wan_10
#描述：WAN设置页面中协议为静态ip时设置WAN口ip的子网掩码为自定义子网掩码
#输入：Self ,ip-WAN口ip,netmask-自定义子网掩码
#输出：None
def set_wan_staticip_customnetmask(self,ip,netmask):#描述：
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #设置路由器WAN口的ip
        driver.find_element_by_id("cbid.network.wan.ipaddr").clear()
        driver.find_element_by_id("cbid.network.wan.ipaddr").send_keys(ip)
        driver.implicitly_wait(10)
        #子网掩码选择自定义
        m = driver.find_element_by_id("cbi.combobox.cbid.network.wan.netmask")
        m.find_element_by_xpath("//option[@value='']").click()
        driver.implicitly_wait(10)
        #输入测试的子网掩码
        driver.find_element_by_id("cbid.network.wan.netmask").clear()
        driver.find_element_by_id("cbid.network.wan.netmask").send_keys(netmask)
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"静态ip时设置WAN口ip的子网掩码为自定义子网掩码失败，原因如下：\n%s"%e

#编号：Func_wan_11
#描述：WAN设置页面中协议为静态ip时获取WAN口ip的子网掩码
#输入：self
#输出：netmask-WAN口ip的子网掩码
def get_wan_staticip_netmask(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #静态ip时获取WAN口ip的子网掩码
        netmask = driver.find_element_by_id("cbid.network.wan.netmask").get_attribute("value")
        #将子网掩码返回给函数
        return netmask
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"静态ip时获取WAN口ip的子网掩码失败，原因如下：\n%s"%e

#编号：Func_wan_12
#描述：WAN设置页面中协议为静态ip时设置WAN口ip的网关
#输入：self ,gateway-WAN口的网关
#输出：None
def set_wan_staticip_gateway(self,gateway):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #静态ip时获取WAN口ip的子网掩码
        driver.find_element_by_id("cbid.network.wan.gateway").clear()
        driver.find_element_by_id("cbid.network.wan.gateway").send_keys(gateway)
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"静态ip时设置WAN口ip的网关失败，原因如下：\n%s"%e

#编号：Func_wan_13
#描述：WAN设置页面中协议为静态ip时获取WAN口ip的网关
#输入：self
#输出：gateway-WAN口的网关
def get_wan_staticip_gateway(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #静态ip时获取WAN口ip的网关
        gateway = driver.find_element_by_id("cbid.network.wan.gateway").get_attribute("value")
        #将子网掩码返回给函数
        return gateway
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"静态ip时获取WAN口ip的网关失败，原因如下：\n%s"%e

#编号：Func_wan_14
#描述：WAN设置页面中协议为静态ip时设置WAN口ip的广播地址
#输入：self ,broadcast-广播地址
#输出：None
def set_wan_staticip_broadcast(self,broadcast):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #静态ip时设置WAN口ip的广播地址
        driver.find_element_by_id("cbid.network.wan.broadcast").clear()
        driver.find_element_by_id("cbid.network.wan.broadcast").send_keys(broadcast)
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"静态ip时设置WAN口ip的广播地址失败，原因如下：\n%s"%e

#编号：Func_wan_15
#描述：WAN设置页面中协议为静态ip时获取WAN口ip的广播地址
#输入：self
#输出：broadcast-广播地址
def get_wan_staticip_broadcast(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #静态ip时获取WAN口ip的广播地址
        gateway = driver.find_element_by_id("cbid.network.wan.broadcast").get_attribute("value")
        #将广播地址返回给函数
        return gateway
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"静态ip时获取WAN口ip的广播地址失败，原因如下：\n%s"%e

#编号：Func_wan_16
#描述：WAN设置页面中协议为静态ip时设置WAN口ip的dns
#输入：self , dns-dns地址
#输出：None
def set_wan_staticip_dns(self,dns):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #静态ip时设置WAN口ip的dns
        driver.find_element_by_id("cbid.network.wan.dns.1").clear()
        driver.find_element_by_id("cbid.network.wan.dns.1").send_keys(dns)
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"静态ip时设置WAN口ip的dns失败，原因如下：\n%s"%e

#编号：Func_wan_17
#描述：WAN设置页面中协议为静态ip时获取WAN口ip的dns
#输入：self
#输出：dns-dns地址
def get_wan_staticip_dns(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #静态ip时获取WAN口ip的dns
        dns = driver.find_element_by_id("cbid.network.wan.dns.1").get_attribute("value")
        #将广播地址返回给函数
        return dns
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"静态ip时获取WAN口ip的dns失败，原因如下：\n%s"%e

#编号：Func_wan_18
#描述：设置pppoe的类型:normal,wayos
#输入：self ,mode:通用,wayos
#输出：None
def set_wan_pppoe_mode(self,mode):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        m = driver.find_element_by_id("cbid.network.wan.ppptype")
        #pppoe时,设置类型为通用
        if mode == 'normal':
            m.find_element_by_id("cbi-network-wan-ppptype-normal").click()
        #pppoe时,设置类型为维盟
        elif mode == 'wayos':
            m.find_element_by_id("cbi-network-wan-ppptype-wayos").click()
        else:
            print u"mode类型请输入normal,wayos"
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"设置pppoe的类型:normal,wayos失败，原因如下：\n%s"%e

#编号：Func_wan_19
#描述：WAN设置页面中协议为pppoe时,设置用户名和密码
#输入：self,username-pppoe的用户名,password-pppoe的密码
#输出：None
def set_wan_pppoe_userpwd(self,username,password):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #设置用户名和密码
        driver.find_element_by_id("cbid.network.wan.username").clear()
        driver.find_element_by_id("cbid.network.wan.username").send_keys(username)
        driver.find_element_by_id("cbid.network.wan.password").clear()
        driver.find_element_by_id("cbid.network.wan.password").send_keys(password)
        driver.implicitly_wait(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"pppoe时,设置用户名和密码失败，原因如下：\n%s"%e

#编号：Func_wan_20
#描述：WAN设置页面中克隆mac地址
#输入：self,mac-克隆mac地址
#输出：None
def set_wan_mac(self,mac):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #设置路由器WAN口mac地址
        driver.find_element_by_id("cbid.network.wan.macaddr").clear()
        driver.find_element_by_id("cbid.network.wan.macaddr").send_keys(mac)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"设置路由器WAN口mac地址失败，原因如下：\n%s"%e

#编号：Func_wan_21
#描述：WAN设置页面中获取WAN口的mac地址
#输入：self
#输出：mac- WAN口的mac地址
def get_wan_mac(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #获取路由器WAN口mac地址
        mac = driver.find_element_by_id("cbid.network.wan.macaddr").get_attribute("placeholder")
        #将路由WAN口的mac返回给函数
        return mac
    except Exception,e:
        print u"获取路由器WAN口mac地址失败，原因如下：\n%s"%e

#编号：Func_wan_22
#描述：WAN设置页面中设置mtu的值
#输入：self,mtu-WAN口的mtu值
#输出：None
def set_wan_mtu(self,mtu):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #设置路由器WAN口mtu值
        driver.find_element_by_id("cbid.network.wan.mtu").clear()
        driver.find_element_by_id("cbid.network.wan.mtu").send_keys(mtu)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"设置路由器WAN口mtu值失败，原因如下：\n%s"%e

#编号：Func_wan_23
#描述：WAN设置页面中获取mtu的值
#输入：self
#输出：mtu-WAN口的mtu值
def get_wan_mtu(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #获取路由器WAN口的mtu值
        mtu = driver.find_element_by_id("cbid.network.wan.mtu").get_attribute("placeholder")
        #将路由WAN口的mtu值返回给函数
        return mtu
    except Exception,e:
        print u"获取路由器WAN口的mtu值失败，原因如下：\n%s"%e

#编号：Func_wan_24
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

#编号：Func_wan_25
#描述：点击“保存&应用”提交表单
#输入：self
#输出：None
def apply(self):
    public_control.apply(self)

#编号：Func_wan_26
#描述：点击“复位”
#输入：self
#输出：None
def reset(self):
    public_control.reset(self)



__author__ = 'zeng'
