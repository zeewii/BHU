#coding=utf-8

#描述:QOS-IP模块用例模块
#作者：孔志兵

import unittest
import time

from selenium import webdriver

from network.qosIp import qosIP_control,qosIP_business
from login import login_control
from publicControl import public_control
from system.reboot import reboot_control
from selenium.webdriver.common.action_chains import ActionChains
from data import data

#startIP,endIP分别是起始地址，结束地址的值
startIP = '192.168.1.109'
endIP = '192.168.1.209'

#dlSpeed,upSpeed分别是下载速度和上传速度的值
dlSpeed = 3000
upSpeed = 2000

err = 0.3#err是在线测速与设置的速度的允许误差范围
bd = 4096#WAN口接入的带宽
numMax=30#numMax是qos-ip最大能设置多少条规则

login_data=data.get_login_data()
ip=login_data.get("ip") #路由器管理IP
user=login_data.get("user") #路由器登录用户名
pwd=login_data.get("pwd")     #路由器登录密码
url='http://%s' %ip  #路由器管理URL

class QosIPTest(unittest.TestCase):

     def setUp(self):
        self.driver = webdriver.Firefox()

        self.driver.get(url)
        login_control.set_user(self,user,pwd)
        login_control.submit(self)
        self.driver.implicitly_wait(10)
        #public_control.menu(self,u'网络',u'Qos-ip')
        qosIP_control.menu(self)

     #清除环境
     def cleanup(self):
        qosIP_control.delete(self,1)
        qosIP_control.submit(self)

     #验证qos-ip限速默认状态检查---100msh0254
     def test_qosIP_default(self):
         u'''检查qos-ip限速默认状态是否是关闭的 '''
         butt = qosIP_control.get_button(self)
         assert butt==0,u'qos-ip限速默认状态是开启的，与需求不符'
         print u"qos-ip限速默认状态关闭检查--用例编号100msh0254--测试成功"


     #验证qos-ip限速有效性检查---100msh0255
     def test_qosIP(self):
         u'''验证qos-ip限速有效性'''
         driver = self.driver
         #添加规则
         qosIP_control.set_qos_ip_enable(self)
         qosIP_business.set_rule(self,startIP,endIP,dlSpeed,upSpeed,1)
         driver.implicitly_wait(10)
         dl = qosIP_business.dlSpeedCheck(self,dlSpeed,err)
         point = err*100
         assert dl, u"在线测试下载速度与设置的下载速度超过误差"
         print u"qos-ip下载速度功能验证--用例编号100msh0255--测试成功"

     #验证qos-ip重启后规则有效性检查---100msh0256
     def test_qosIP_reboot(self):
         u'''验证qos-ip重启后规则有效性 '''
         driver = self.driver
         qosIP_control.set_qos_ip_enable(self)
         #添加规则
         qosIP_business.set_rule(self,startIP,endIP,dlSpeed,upSpeed,1)
         #重启
         public_control.menu(self,u'系统',u'重启')
         reboot_control.reboot(self)
         time.sleep(60)
         driver.implicitly_wait(10)
         dl = qosIP_business.dlSpeedCheck(self,dlSpeed,err)
         assert dl, u"重启后在线测试下载速度与设置的下载速度超过误差"
         print u"qos-ip重启后规则有效性检查--用例编号100msh0256--测试成功"

     #验证qos-ip空规则效性检查---100msh0257
     def test_qosIP_none(self):
         u'''验证qos-ip空规则效性 '''
         qosIP_control.set_qos_ip_enable(self)
         qosIP_control.submit(self)
         dl = qosIP_business.dlSpeedCheck(self,bd,err)
         assert dl, u"空规则检查失败"
         print u"qos-ip空规则验证--用例编号100msh0257--测试成功"

     #验证qos-ip添加单个IP规则有效性检查---100msh0258
     def test_qosIP_single(self):
         u'''验证qos-ip添加单个IP规则有效性 '''
         driver = self.driver
         #添加规则
         qosIP_business.set_rule(self,startIP,startIP,dlSpeed,upSpeed,1)
         driver.implicitly_wait(10)
         dl = qosIP_business.upCheck(self,upSpeed,err)
         assert dl, u"上传速度限速超过误差范围"
         print u"qos-ip上传速度功能验证--用例编号100msh0255--测试成功"

     #验证qos-ip添加多个IP规则有效性检查---100msh0259
     def test_qosIP_multi(self,numMax):
        u'''验证qos-ip添加多个IP规则有效性'''
        driver = self.driver
        ip = ['192','168','11','100']
        dlSpeed = 1024
        upSpeed = 128
        for i in range(1,numMax):
            ip[3] +=1
            startIp = '.'.join(ip)
            endIp = '.'.join(ip)
            dl = dlSpeed+i*128
            up = upSpeed+i*128
            qosIP_control.add(self)
            qosIP_control.set_ip(self,startIp,endIp,i)
            qosIP_control.set_speed(self,dl,up,i)
        qosIP_control.submit(self)

     #验证qos-ip添加IP段规则规则有效性检查---100msh0260
     def test_qosIP_multiIP(self):
         u'''验证qos-ip添加IP段规则规则有效性 '''
         driver = self.driver
         qosIP_control.set_qos_ip_enable(self)
         #添加规则
         qosIP_business.set_rule(self,startIP,endIP,dlSpeed,upSpeed,1)
         driver.implicitly_wait(10)
         dl = qosIP_business.dlSpeedCheck(self,dlSpeed,err)
         assert dl, u"下载速度限速超过误差范围"
         print u"qos-ip添加IP段规则规则有效性检查--用例编号100msh0260--测试成功"

     #验证qos-ip规则起始地址大于结束地址规则容错性---100msh0261
     def test_qos_ipCheck(self):
         u'''验证qos-ip规则起始地址大于结束地址规则容错性 '''
         #添加IP
         qosIP_control.add(self)
         time.sleep(1)
         qosIP_control.set_ip(self,'192.168.1.101','192.168.1.100',1)
         time.sleep(1)
         qosIP_control.submit(self)
         test = qosIP_business.get_alert_text(self)
         time.sleep(1)
         assert test == u'结束IP地址必须大于起始IP地址，且结束IP地址与起始IP地址的前3段必须相同。\n是否修改结束IP地址？',u'弹窗信息表达错误'
         print u'验证qos-ip规则起始地址大于结束地址规则容错性--用例编号100msh0261--测试成功'

     #验证qos-ip规则只设置起始地址容错性---100msh0262
     def test_qos_endtipCheck(self):
         u'''验证qos-ip规则只设置起始地址容错性'''
         #添加IP
         qosIP_control.set_qos_ip_enable(self)
         qosIP_control.add(self)
         qosIP_control.set_ip(self,'192.168.1.101','',1)
         qosIP_control.add(self)
         time.sleep(1)
         test = qosIP_business.get_alert_text(self)
         assert test == u'结束IP地址必须大于起始IP地址，且结束IP地址与起始IP地址的前3段必须相同。\n是否修改结束IP地址？',u'弹窗信息表达错误'
         print u'验证qos-ip规则只设置起始地址容错性--用例编号100msh0261--测试成功'

     #验证qos-ip规则只设置结束地址容错性---100msh0263
     def test_qos_startipCheck(self):
         u'''验证qos-ip规则只设置结束地址容错性'''
         driver = self.driver
         #添加IP
         qosIP_control.set_qos_ip_enable(self)
         qosIP_control.add(self)
         qosIP_control.set_ip(self,'','192.168.1.101',1)
         time.sleep(1)
         qosIP_control.submit(self)
         element = driver.find_element_by_xpath(".//*[@id='cbi-qos-ip-classify']/div[2]/div[1]/ul/li")
         assert element ,u'qos-ip规则只设置结束地址时，没有弹窗提示信息'
         test = element.text
         assert test == u'无效的起始IP地址或者结束IP地址，结束IP地址必须大于起始IP地址。',u'提示信息错误'
         print  u'验证qos-ip规则只设置结束地址容错性--用例编号100msh0263--测试成功'

     #验证qos-ip规则设置下载速度大于总速度---100msh0264
     def test_qosIP1(self):
         u'''验证qos-ip规则设置下载速度大于总速度'''
         driver = self.driver
         #添加规则
         qosIP_business.set_rule(self,startIP,endIP,9999999999,upSpeed,1)
         driver.implicitly_wait(10)
         dl = qosIP_business.dlSpeedCheck(self,bd,err)
         assert dl, u"qos-ip规则设置下载速度大于总速度时，测速失败"
         print u"qos-ip规则设置下载速度大于总速度--用例编号100msh0264--测试成功"

     #验证qos-ip规则下载速度为0---100msh0265
     def test_qosIP2(self):
         u'''验证qos-ip规则下载速度为0'''
         driver = self.driver
         #添加规则
         qosIP_business.set_rule(self,startIP,endIP,0,upSpeed,1)
         driver.implicitly_wait(10)
         dl = qosIP_business.dlSpeedCheck(self,bd,err)
         assert dl, u"qos-ip规则下载速度为0时，测速失败"
         print u"qos-ip规则下载速度为0--用例编号100msh0265--测试成功"


     #验证qos-ip规则设置下载速度为空---100msh0266
     def test_qosIP3(self):
         u'''验证qos-ip规则设置下载速度为空 '''
         driver = self.driver
         #添加规则
         qosIP_business.set_rule(self,startIP,endIP," ",upSpeed,1)
         driver.implicitly_wait(10)
         dl = qosIP_business.dlSpeedCheck(self,bd,err)
         assert dl, u"qos-ip规则下载速度为空时，测速失败"
         print u"qos-ip规则下载速度为空--用例编号100msh0266--测试成功"

     #验证qos-ip设置多条IP相同速率不同的规则---100msh0267
     def test_qosIP_multi2(self,numMax):
        u'''验证qos-ip设置多条IP相同速率不同的规则'''
        driver = self.driver
        dlSpeed = 1024
        upSpeed = 128
        for i in range(1,numMax):
            dl = dlSpeed+i*128
            up = upSpeed+i*128
            qosIP_control.add(self)
            qosIP_control.set_ip(self,startIP,endIP,i)
            qosIP_control.set_speed(self,dl,up,i)
        qosIP_control.submit(self)
        dl = qosIP_business.dlSpeedCheck(self,dlSpeed,err)
        assert dl, u"在线测试下载速度与设置的下载速度误差超过"
        print u"验证qos-ip设置多条IP相同速率不同的规则--用例编号100msh0267--测试成功"


     #验证qos-ip规则极限带宽验证---100msh0268



     #验证qos-ip规则删除有效性---100msh0269
     def test_qosIP_delete(self):
         u'''验证qos-ip规则删除有效性'''
         qosIP_control.set_qos_ip_enable(self)
         qosIP_business.add_multi(self,numMax)
         qosIP_business.set_rule(self,startIP,endIP,dlSpeed,upSpeed,1)
         qosIP_control.delete_multi(self)
         qosIP_control.submit(self)
         dl = qosIP_business.dlSpeedCheck(self,bd,err)
         assert dl, u"规则删除后，规则依然生效，导致用例测试失败"
         print u"qos-ip规则删除有效性--用例编号100msh0269--测试成功"

     #清理环境
     def tearDown(self):
        self.driver.get(url)
        login_control.set_user(self,user,pwd)
        login_control.submit(self)
        self.driver.implicitly_wait(10)
        qosIP_control.menu(self)
        qosIP_control.set_qos_ip_enable(self)
        qosIP_control.delete_multi(self)
        self.driver.quit()


if __name__=='__main__':
    unittest.main()
    #nose.main()



__author__ = 'kzb'
