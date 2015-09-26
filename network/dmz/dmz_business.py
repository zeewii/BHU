#coding=utf-8
#描述：该模块为dmz设置的业务逻辑模块.
#作者：张均

from selenium import webdriver
import dmz_control
from connect import ssh
from data import data
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import time

#描述:调试时使用
########################################################
'''
ip = '192.168.11.111'
host = '192.168.11.1'
usr = 'root'
pwd = 'BHU@100msh$%^'
'''
########################################################

#查看iptables表,并查找DMZ策略
def iptables_nat(self,ip):
    iptable = 'iptables -t nat -L |grep %s'%ip  #查看iptables的nat表，并过滤IP地址
    list = ssh.ssh_cmd2(iptable)
    #list = ssh.ssh_cmd(host,usr,pwd,iptable)   #单独调试时使用
    dmz_host1 = '/* DMA */ to:%s'%ip        #防火墙WAN_rule策略查找
    dmz_host2 = '/* DMA (reflection) */ to:%s'%ip   ##防火墙LAN_rule策略查找
    lan_rule = False
    wan_rule = False

    #在iptables查询结果中搜索需要的值，如果搜到就将wan_rule置为True，否则抛异常
    if dmz_host1 in list:
        wan_rule = True
    else:
        raise ValueError(u'未在iptables wan_rule策略中查找到DMZ主机')

    #在iptables查询结果中搜索需要的值，如果搜到就将lan_rule置为True，否则抛异常
    if dmz_host2 in list:
        lan_rule = True
    else:
        raise ValueError(u'未在iptables lan_rule策略中查找到DMZ主机')


    #当lan_rule和wan_rule同时满足条件时，打印策略成功，否则抛异常
    if lan_rule and wan_rule == True:
        print u'DMZ策略设置成功'
    else:
        raise ValueError(u'DMZ策略设置失败')



#描述:启用DMZ
#输入:self
#输出：打印状态信息
def set_status_enable(self):
    driver = self.driver
    driver.implicitly_wait(10)
    enable = dmz_control.dmz_status(self)
    if enable == 1:
        print u"DMZ功能已经为开启状态"
    else:
        driver.find_element_by_class_name("cbi-input-checkbox").click()
        print u"DMZ功能为禁用状态，已切换为启用状态"

#描述:禁用DMZ
#输入:self
#输出：打印状态信息
def set_status_disable(self):
    driver = self.driver
    driver.implicitly_wait(10)
    enable = dmz_control.dmz_status(self)
    if enable == 0:
        print u"DMZ功能已经为禁用状态"
    else:
        driver.find_element_by_class_name("cbi-input-checkbox").click()
        print u"DMZ功能为启用状态，已切换为禁用状态"

#描述:设置DMZ协议为all
#输入:self,从dmz_control中的set_protocol(self)函数返回元组(setall,settcpudp,settcp,setudp,seticmp)
#输出：None
def set_all_protocol(self):
    driver = self.driver
    driver.implicitly_wait(10)
    proto = dmz_control.set_protocol(self)
    for protocol_list in proto:
        print protocol_list.text
    proto[0].click()
    time.sleep(2)


#描述:设置DMZ协议为tcp+udp
#输入:self,从dmz_control中的set_protocol(self)函数返回元组(setall,settcpudp,settcp,setudp,seticmp)
#输出：None
def set_tcpudp_protocol(self):
    driver = self.driver
    driver.implicitly_wait(10)
    proto = dmz_control.set_protocol(self)
    proto[1].click()
    time.sleep(2)

#描述:设置DMZ协议为tcp
#输入:self,从dmz_control中的set_protocol(self)函数返回元组(setall,settcpudp,settcp,setudp,seticmp)
#输出：None
def set_tcp_protocol(self):
    driver = self.driver
    driver.implicitly_wait(10)
    proto = dmz_control.set_protocol(self)
    proto[2].click()
    time.sleep(2)

#描述:设置DMZ协议为udp
#输入:self,从dmz_control中的set_protocol(self)函数返回元组(setall,settcpudp,settcp,setudp,seticmp)
#输出：None
def set_udp_protocol(self):
    driver = self.driver
    driver.implicitly_wait(10)
    proto = dmz_control.set_protocol(self)
    proto[3].click()
    time.sleep(2)

#描述:设置DMZ协议为icmp
#输入:self,从dmz_control中的set_protocol(self)函数返回元组(setall,settcpudp,settcp,setudp,seticmp)
#输出：None
def set_icmp_protocol(self):
    driver = self.driver
    driver.implicitly_wait(10)
    proto = dmz_control.set_protocol(self)
    proto[4].click()
    time.sleep(2)

#查看iptables表,并查找DMZ策略
def iptables_dmz_disable(self,ip):
    iptable = 'iptables -t nat -L |grep %s'%ip  #查看iptables的nat表，并过滤IP地址
    list = ssh.ssh_cmd2(iptable)
    #list = ssh.ssh_cmd(host,usr,pwd,iptable)   #单独调试时使用
    dmz_host1 = '/* DMA */ to:%s'%ip        #防火墙WAN_rule策略查找
    dmz_host2 = '/* DMA (reflection) */ to:%s'%ip   ##防火墙LAN_rule策略查找
    lan_rule = False
    wan_rule = False

    #在iptables查询结果中搜索需要的值，如果搜到就将wan_rule置为True，否则抛异常
    if dmz_host1 in list:
        raise ValueError(u'DMZ禁用后，仍在iptables wan_rule策略中查找到DMZ主机')
    else:
        print u'DMZ禁用后，iptables wan_rule策略中DMZ主机已清除'

    #在iptables查询结果中搜索需要的值，如果搜到就将lan_rule置为True，否则抛异常
    if dmz_host2 in list:
        raise ValueError(u'DMZ禁用后，仍在iptables lan_rule策略中查找到DMZ主机')
    else:
        print u'DMZ禁用后，iptables lan_rule策略中DMZ主机已清除'
        print u'DMZ策略禁用成功'

__author__ = 'zhangjun'
