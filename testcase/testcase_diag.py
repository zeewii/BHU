#coding=utf-8

import unittest
from selenium import webdriver
from system.admin import admin_control,admin_business
from login import login_business,login_control
from data import data
from network.diagnostics import diagnostics_control
import time


#########################################################
host1 = '192.168.11.111'
host2 = 'www.qq.com'
host3 = 'www.163.com'

#调戏时使用，与setup中的 admin_login对应
'''
url = "http://192.168.11.1"
user = 'root'
passwd = 'bm100@rut!%v2'
'''
#########################################################


class AdminTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        #login_business.admin_login(self,url,user,passwd)
        login_business.default_login(self)
        diagnostics_control.diag_menu(self)
        print u'网络诊断页面已打开'


    #网络诊断:ping命令测试
    def test_diag_ping(self):
        diagnostics_control.set_ping(self,host2)
        diagnostics_control.ping_run(self)
        diagnostics_control.diag_output(self)
        diagnostics_control.pass_result(self)


    #网络诊断:tracert命令测试
    def test_diag_tracert(self):
        diagnostics_control.set_tracert(self,host2)
        diagnostics_control.tracert_run(self)
        diagnostics_control.diag_output(self)
        diagnostics_control.pass_result(self)


    ##网络诊断:nslookup命令测试
    def test_diag_nslookup(self):
        diagnostics_control.set_nslookup(self,host3)
        diagnostics_control.nslookup_run(self)
        diagnostics_control.diag_output(self)
        diagnostics_control.pass_result(self)




    #退出
    def tearDown(self):
         self.driver.quit()

if __name__=='__main__':
    unittest.main()
    #nose.main()






__author__ = 'super'
