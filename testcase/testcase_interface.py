#coding=utf-8
#描述：该模块为测试interface模块
#作者：曾祥卫

import unittest
from selenium import webdriver
from data import data
from network.interface import interface_business

class TestInterface(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        #将浏览器最大化
        self.driver.maximize_window()
        #使用默认ip登录接口页面
        interface_business.goin_default_interface(self)


    def test_053_description(self):
        u'''LAN接口总览信息检查'''
        interface_business.step_100msh0053(self)
        print u"获取LAN接口总览信息成功，请检查LAN_description.txt"


    #退出清理工作
    def tearDown(self):
         self.driver.quit()


if __name__=='__main__':
    unittest.main()

__author__ = 'zeng'

