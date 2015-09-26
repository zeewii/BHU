#coding:utf-8

#描述:恢复出场设置模块用例模块
#作者：孔志兵

import unittest
import time
from selenium import webdriver
from system.flashops.restore import restore_control
from network.wifidog import general_control
from login import login_control
from connect import ssh
from data import data

login_data=data.get_login_data()
ip=login_data.get("ip") #路由器管理IP
user=login_data.get("user") #路由器登录用户名
pwd=login_data.get("pwd")     #路由器登录密码
url='http://%s' %ip  #路由器管理URL

class RestoreTest(unittest.TestCase):
     def setUp(self):
         #driver = self.driver
         self.driver = webdriver.Firefox()
         self.driver.implicitly_wait(10)
         self.driver.get(url)
         login_control.set_user(self,user,pwd)
         login_control.submit(self)

     #验证恢复出厂设置是否有确认信息
     def test_restore(self):
         restore_control.menu(self)
         restore_control.set_restore(self)
         alert = restore_control.get_alert(self)
         assert alert,u'恢复出场设置时，没有向客户进行确认'
         info = restore_control.get_alert_info(alert)
         assert info==u'确定要放弃所有更改？',u'确认信息不符合要求'

     #验证恢复出厂设置功能有效性
     def test_testore_func(self):
         general_control.wifidog_menu(self)
         gatewayId1 = general_control.get_gatewayId(self)
         general_control.set_gatewayId(self,'11111111111')
         general_control.apply(self)
         restore_control.menu(self)
         restore_control.set_restore(self)
         alert = restore_control.get_alert(self)
         alert.accept()
         #time.sleep(60)
         self.driver.implicitly_wait(50)
         self.driver.get(url)
         login_control.set_user(self,user,pwd)
         login_control.submit(self)
         general_control.wifidog_menu(self)
         gatewayId2 = general_control.get_gatewayId(self)
         assert gatewayId1==gatewayId2,u'恢复出场设置后网关ID恢复默认值'

     #验证从后台恢复出场设置
     def test_restore_ssh(self):
         general_control.wifidog_menu(self)
         gatewayId1 = general_control.get_gatewayId(self)
         general_control.set_gatewayId(self,'11111111111')
         ssh.ssh_cmd(ip,user,pwd,'reset')
         self.driver.implicitly_wait(50)
         self.driver.get(url)
         login_control.set_user(self,user,pwd)
         login_control.submit(self)
         general_control.wifidog_menu(self)
         gatewayId2 = general_control.get_gatewayId(self)
         assert gatewayId1==gatewayId2,u'后台恢复出场设置后网关ID恢复默认值'


     #退出
     def tearDown(self):
         self.driver.quit()


if __name__=='__main__':
    unittest.main()
    #nose.main()

__author__ = 'kzb'

