#coding=utf-8

import unittest
from selenium import webdriver
from system.admin import admin_control,admin_business
from login import login_business,login_control
from data import data
from network.dmz import dmz_control,dmz_business
import time


#########################################################
sheet = 'basic_conf'
host1 = data.xls_data(sheet,4,1)        #测试主机IP(DMZ)
port1 = data.xls_data(sheet,13,1)       #DMZ端口
port2 = data.xls_data(sheet,14,1)       #DMZ端口
#########################################################


class DmzTest(unittest.TestCase):
    def setUp(self):
        #url = "http://192.168.11.1"
        #user = 'root'
        #passwd = 'bm100@rut!%v2'
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        #login_business.admin_login(self,url,user,passwd)
        login_business.default_login(self)
        dmz_control.dmz_menu(self)
        print u'DMZ页面已打开'

     #DMZ协议为all时
    def test_dmz_all(self):
        dmz_business.set_status_enable(self)
        dmz_control.set_host(self,host1)
        dmz_business.set_all_protocol(self)
        dmz_control.dmz_apply(self)
        dmz_business.iptables_nat(self,host1)

    #DMZ协议为tcpudp时
    def test_dmz_tcpudp(self):
        dmz_business.set_status_enable(self)
        dmz_control.set_host(self,host1)
        dmz_business.set_tcpudp_protocol(self)
        dmz_control.set_port(self,port1)
        dmz_control.dmz_apply(self)
        dmz_business.iptables_nat(self,host1)

    #DMZ协议为tcp时
    def test_dmz_tcp(self):
        dmz_business.set_status_enable(self)
        dmz_control.set_host(self,host1)
        dmz_business.set_tcp_protocol(self)
        dmz_control.set_port(self,port1)
        dmz_control.dmz_apply(self)
        dmz_business.iptables_nat(self,host1)


    #DMZ协议为udp时
    def test_dmz_udp(self):
        dmz_business.set_status_enable(self)
        dmz_control.set_host(self,host1)
        dmz_business.set_udp_protocol(self)
        dmz_control.set_port(self,port1)
        dmz_control.dmz_apply(self)
        dmz_business.iptables_nat(self,host1)

    #DMZ协议为icmp时,先查询开启时iptables策略是否存在，然后查询策略禁用后，iptables中相应的条目是否删除
    def test_dmz_icmp(self):
        dmz_business.set_status_enable(self)
        dmz_control.set_host(self,host1)
        dmz_business.set_icmp_protocol(self)
        dmz_control.dmz_apply(self)
        dmz_business.iptables_nat(self,host1)
        dmz_business.set_status_disable(self)                #测试DMZ策略禁用后是否生效
        dmz_control.dmz_apply(self)
        time.sleep(4)
        dmz_business.iptables_dmz_disable(self,host1)       #测试DMZ策略禁用后是否生效






     #退出
    def tearDown(self):
        #每次密码都要改回原来的，防止前面的错误导致后面的用例运行错误
        dmz_business.set_status_disable(self)
        dmz_control.dmz_apply(self)
        time.sleep(4)
        self.driver.quit()

if __name__=='__main__':
    unittest.main()
    #nose.main()


__author__ = 'super'
