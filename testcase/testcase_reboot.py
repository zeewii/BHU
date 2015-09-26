#coding=utf-8

#描述:重启模块用例模块
#作者：孔志兵

#coding:utf-8
import unittest
import time,os

#import nose
from selenium import webdriver

from login import login_control
from system.reboot import reboot_control
from publicControl import public_control
from network.wifidog import network_control
from network.privoxy import privoxy_control
from data import data

login_data=data.get_login_data()
ip=login_data.get("ip") #路由器管理IP
user=login_data.get("user") #路由器登录用户名
pwd=login_data.get("pwd")     #路由器登录密码
url='http://%s' %ip  #路由器管理URL
string='ping 192.168.11.1 -c 3'#string是用来ping路由器的管理地址的，通过其结果来判断有没有重启

class RebootTest(unittest.TestCase):
     def setUp(self):
        self.driver = webdriver.Firefox()

     #验证重启选项有效性检查----100msh0055
     def test_reboot(self):
         self.driver.get(url)
         login_control.set_user(self,user,pwd)
         login_control.submit(self)
         reboot_control.menu(self)
         reboot_control.reboot(self)
         time.sleep(5)
         p = os.system(string)
         assert p !=0 ,u'未进行重启动作'
         print u'正在重启中'
         time.sleep(60)
         p = os.system(string)
         assert p ==0 ,u'页面重启失败'
         print u'页面重启成功'



     #每重启20次路由器后,检测门户认证流程业务是否正常,测试5次.
     def test_rebootLoop(self):
         for i in range(1,6):
             for j in range(0,20):
                 self.driver.get(url)
                 login_control.set_user(self,user,pwd)
                 login_control.submit(self)
                 reboot_control.menu(self)
                 reboot_control.reboot(self)
                 self.driver.implicitly_wait(50)
             login_control.set_user(self,user,pwd)
             login_control.submit(self)
             public_control.menu(self,u'网络',u'门户认证')
             result1 = network_control.network(self,"http://www.sina.com.cn",u"新浪")
             assert result1==True, u'第%d次反复重启20次后门户认证失败，程序中断' %i
             print u'第%d次反复重启20次后门户认证生效' %i
             result2 =privoxy_control.get_js(self)
             assert 'http://chdadd.100msh.com/ad.js' in result2,u'第%d次反复重启20次后如影随行功能不生效' %i

     #退出
     def tearDown(self):
         self.driver.quit()


if __name__=='__main__':
    unittest.main()
    #nose.main()

__author__ = 'kzb'

