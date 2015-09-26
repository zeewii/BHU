#coding=utf-8
#描述：该模块为测试lan模块
#作者：曾祥卫

import unittest
from selenium import webdriver
import time,os,commands
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from login import login_control
from data import data
from network.interface import interface_control
from connect import ssh
from publicControl import public_control
from network.interface.lan import lan_business
from network.interface import interface_business

class TestLan(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        #将浏览器最大化
        self.driver.maximize_window()
        #使用默认ip登录lan页面
        lan_business.goin_default_lan(self)

    def test_054_055_IP_netmask(self):
        u"""修改LAN IP和A,B,C类子网掩码"""
        #把4次修改LAN IP和子网掩码后client ping修改后ip的值取出
        result = lan_business.step_100msh0054_100msh0055(self)
        print result
        #如果4次都为0则通过，否则不通过
        assert result == [0,0,0,0],u"测试LAN IP和A,B,C类子网掩码失败"
        print u"测试LAN IP和A,B,C类子网掩码成功"

    def test_056_custom_netmask(self):
        u"""lan自定义掩码设置"""
        result = lan_business.step_100msh0056(self)
        print result
        #如果4次都为1则通过，否则不通过
        assert result == [1,1,1,1],u"测试lan自定义掩码设置失败"
        print u"测试lan自定义掩码设置成功"

    def test_057_broadcast(self):
        u"""lan广播地址配置有效性测试"""
        result = lan_business.step_100msh0057(self)
        print result
        #如果2次都为1则通过，否则不通过
        assert result == [1,1],u"测试lan广播地址配置有效性失败"
        print u"测试lan广播地址配置有效性成功"

    def test_059_startip(self):
        u"""IP地址池默认起始值检查"""
        result = lan_business.step_100msh0059(self)
        print result
        #如果IP地址池默认起始值为100则通过，否则不通过
        assert result == '100',u"测试IP地址池默认起始值失败"
        print u"测试IP地址池默认起始值成功"

    def test_067_068_abnormal_input(self):
        u"""lan异常输入测试"""
        result = lan_business.step_100msh0067_100msh0068(self)
        print result
        #如果4次都为1则通过，否则不通过
        assert result == [1,1,1,1],u"测试lan异常输入测试失败"
        print u"lan测试异常输入测试成功"

    #退出清理工作
    def tearDown(self):
        self.driver.quit()


if __name__=='__main__':
    unittest.main()

__author__ = 'zeng'

