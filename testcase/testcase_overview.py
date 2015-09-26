#coding=utf-8

#描述:状态模块用例模块
#作者：孔志兵

import unittest
from data import data
from selenium import webdriver

from login.login_control import logout
from status.overview.overview_business import *

login_data=data.get_login_data()
version=login_data.get("version")#version是需求规定的版本号
ip=login_data.get("ip") #路由器管理IP
user=login_data.get("user") #路由器登录用户名
pwd=login_data.get("pwd")     #路由器登录密码
url='http://%s' %ip  #路由器管理URL

class TestOverview(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(url)
        login_control.set_user(self,user,pwd)
        login_control.submit(self)

    def test_version(self):
        u'''BHU版本号测试'''
        assert version_compare(self,version),u'页面版本号与需求不一致'
        print u'页面版本号与需求一致'

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()


__author__ = 'kzb'
