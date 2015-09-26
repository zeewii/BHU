#coding:utf-8

#描述:系统模块用例模块
#作者：孔志兵

import unittest

#import nose
from system.system import system_control,system_business
from selenium import webdriver
from login import login_control
from data import data
import time


login_data=data.get_login_data()
ip=login_data.get("ip")       #路由器管理IP
user=login_data.get("user")   #路由器登录用户名
pwd=login_data.get("pwd")     #路由器登录密码
url='http://%s' %ip           #路由器管理URL
pwd_ssh = login_data.get("pwd_ssh")    #ssh登录密码
cmd = 'reboot'
               #ssh输入重启命令
'''
ip='192.168.11.1'
user='root'
pwd='bm100@rut!%v2'
url='http://192.168.11.1'
pwd_ssh='BHU@100msh$%^'
cmd = 'reboot'
'''


class SystemTest(unittest.TestCase):
     def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        login_control.set_user(self,user,pwd)
        login_control.submit(self)
        system_control.menu(self)
        

     def test_hostname1(self):
        u'''测试默认主机名是否与需求一致---100msh0013 '''
        h= system_control.get_hostname(self)
        assert h ==u'100msh',u'默认主机名与需求不一致'
        print u'默认主机名测试用例 --编号为100msh0013--测试成功'

     #测试默认主机名基本功能---100msh0013
     def test_hostname2(self):
        u'''测试默认主机名基本功能---100msh0013 '''
        h= system_control.get_hostname(self)
        result = system_business.hostnameValidate(h,ip,user,pwd_ssh,cmd)
        assert result,u'默认主机没功能不生效'
        print u'测试默认主机名基本功能---100msh0013--测试成功'

     #测试主机名为纯数字---100msh0014
     def test_hostname3(self):
         u'''测试主机名为纯数字---100msh0014 '''
         system_control.set_hostname(self,'1234567890')
         system_control.submit(self)
         time.sleep(2)
         result = system_control.get_errorbox(self)
         assert result,u'修改主机名为纯数字保存成功'#实际上是不能保存成功
         print u'修改主机名为纯数字测试用例 --编号为100msh0014--测试成功'


     #测试主机名为纯字母---100msh0015
     def test_hostname4(self):
         u'''测试主机名为纯字母---100msh0015 '''
         result = system_business.hostname_logic(self,'qwertyuio',ip,user,pwd_ssh,cmd)
         assert result,u'修改主机名为纯字母功能不生效'
         print u'修改主机名为纯字母测试用例 --编号为100msh0015--测试成功'

     #测试主机名含有特殊字符---100msh0016
     def test_hostname5(self):
         u'''测试主机名含有特殊字符---100msh0016 '''
         system_control.set_hostname(self,'$%&*((^*%#')
         system_control.submit(self)
         alert = system_control.get_alert(self)
         assert alert,u'修改主机名为特殊字符保存成功'
         #info = system_control.get_alert_info(alert)
         #assert info==u'一些项目的值无效，无法保存！',u'提示信息错误'
         print u'修改主机名为特殊字符测试用例 --编号为100msh0016--测试成功'

     #测试主机名含数字字母和特殊字符---100msh0017
     def test_hostname6(self):
         u''' 测试主机名含数字字母和特殊字符---100msh0017'''
         system_control.set_hostname(self,'1023_qpwoe_#$%^')
         alert = system_control.get_alert(self)
         assert alert,u'主机名为数字字母和特殊字符保存成功' #实际上不能保存成功
         #info = system_control.get_alert_info(alert)
         #assert info==u'一些项目的值无效，无法保存！',u'提示信息错误'
         print u'修改主机名为数字字母和特殊字符---100msh0017--测试成功'


     #测试主机名为中文---100msh0018
     def test_hostname7(self):
         u'''测试主机名为中文---100msh0018 '''
         system_control.set_hostname(self,u'我爱中国')
         system_control.submit(self)
         alert = system_control.get_alert(self)
         assert alert,u'主机名为中文保存成功' #实际上不能保存成功
         #info = system_control.get_alert_info(alert)
         #assert info==u'一些项目的值无效，无法保存！',u'提示信息错误'
         print u'修改主机名为中文测试用例 --编号为100msh0018--测试成功'

     #测试主机名为空---100msh0019
     def test_hostname8(self):
         u'''测试主机名为空---100msh0019 '''
         h= system_control.get_hostname(self)
         system_control.set_hostname(self ,'')
         system_control.submit(self)
         h1= system_control.get_hostname(self)
         print h1
         assert h ==h1 ,u'修改主机名为空保存后主机名应该为之前的直'
         print u'默认主机名测试用例 --编号为100msh0013--测试成功'

     #测试主机名为1字节---100msh0020
     def test_hostname9(self):
         u'''测试主机名为1字节---100msh0020 '''
         result = system_business.hostname_logic(self,'a',ip,user,pwd_ssh,cmd)
         assert result,u'修改主机名为一个字节功能不生效'
         print u'测试主机名为空---100msh0019--测试成功'


     #测试主机名在最小与最大范围内的---100msh0021
     def test_hostnamea(self):
         u'''测试主机名在最小与最大范围内的---100msh0021 '''
         result = system_business.hostname_logic(self,'kongzhibing',ip,user,pwd_ssh,cmd)
         assert result,u'修改主机名为指定范围内字符功能不生效'
         print u'修改主机名为指定范围内字符测试用例 --编号为100msh0021--测试成功'

     #测试主机名为最大20字节---100msh0022
     def test_hostnameb(self):
         u''' 测试主机名为最大20字节---100msh0022'''
         result = system_business.hostname_logic(self,'1234567890qwertyuiop',ip,user,pwd_ssh,cmd)
         assert result,u'修改主机名为最大字节字符功能不生效'
         print u'修改主机名为最大字节字符测试用例 --编号为100msh0022--测试成功'

     #测试主机名为最大+1字节---100msh0023
     def test_hostnamec(self):
         u''' 测试主机名为最大+1字节---100msh0023'''
         system_control.set_hostname(self,'1234567890qwertyuiop1')
         system_control.submit(self)
         alert = system_control.get_alert(self)
         assert alert,u'主机名为最大+1字节保存成功，没有提示信息' #实际上不能保存成功
         #info = system_control.get_alert_info(alert)
         #assert info==u'一些项目的值无效，无法保存！',u'提示信息错误'
         print u'修改主机名为最大+1字节字符测试用例 --编号为100msh0023--测试成功'

     #测试主机名超长字节---100msh0024
     def test_hostnamed(self):
         u'''测试主机名超长字节---100msh0024 '''
         system_control.set_hostname(self,'qqeueigfrgtiyohjfkhgoierutrtfgrhjhdsuygtiohfgw')
         system_control.submit(self)
         alert = system_control.get_alert(self)
         assert alert,u'主机名超长字节保存成功，没有提示信息' #实际上不能保存成功
         #info = system_control.get_alert_info(alert)
         #assert info==u'一些项目的值无效，无法保存！',u'提示信息错误'
         print u'修改主机名为超长字节测试用例 --编号为100msh0024--测试成功'

     #测试同步浏览器的时间
     def test_localTime(self):
         u'''测试同步浏览器时间 '''
         web_time = system_business.get_local_time(self)
         pc_time = system_business.get_pc_time(self)
         assert web_time==pc_time,u'同步浏览器时间不准'

     #退出
     def tearDown(self):
         self.driver.quit()


if __name__=='__main__':
    unittest.main()
    #nose.main()

__author__ = 'kzb'