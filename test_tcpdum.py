#coding=utf-8
#描述：该模块为测试抓包的模块
#作者：曾祥卫

import unittest,time
from selenium import webdriver
from data import data
from network.tcpdump import tcpdump_bussiness
from network.wifidog import general_control
from login import login_business

class TestInterface(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        #将浏览器最大化
        self.driver.maximize_window()
        #使用默认ip登录门户认证的页面
        login_business.default_login(self)
        time.sleep(3)
        general_control.wifidog_menu(self)


    def test_0287_ping(self):
        u'''ping报文内容字段检查'''
        result = tcpdump_bussiness.step_100msh0287(self)
        print result
        assert result == 1,u"测试ping报文内容字段检查失败"
        print u"测试ping报文内容字段检查成功"

    def test_0286_manage(self):
        u'''分区域管理路由器功能检查'''
        result = tcpdump_bussiness.step_100msh0286(self)
        print result
        assert result == 1,u"测试分区域管理路由器功能检查失败"
        print u"测试分区域管理路由器功能检查成功"

    #退出清理工作
    def tearDown(self):
         self.driver.quit()


if __name__=='__main__':
    unittest.main()

__author__ = 'zeng'

