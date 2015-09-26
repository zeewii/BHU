#coding=utf-8
#描述：该模块为lan设置的业务逻辑模块.
#作者：曾祥卫

from selenium import webdriver
from data import data
from login import login_control
from network.interface import interface_business,interface_control
import commonconfig_control,dhcpserver_control,lan_control,lan_network_control
import time

#描述:进入lan页面
def goin_lan(self):
    try:
        #登录路由并进入接口页面
        interface_business.goin_interface(self)
        #点击LAN上的修改按钮
        interface_control.lan_edit(self)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"进入lan页面失败，原因如下：\n%s"%e

#描述：使用默认ip登录lan页面
def goin_default_lan(self):
    try:
        interface_business.goin_default_interface(self)
        #点击LAN上的修改按钮
        interface_control.lan_edit(self)
     #捕捉异常并打印异常信息
    except Exception,e:
        print u"使用默认ip登录wan页面失败，原因如下：\n%s"%e


###############################################
#以下是lan页面的测试步骤
###############################################

#描述：测试用例100msh0054,100msh0055测试步骤----修改LAN IP和A,B,C类子网掩码
def step_100msh0054_100msh0055(self):
    try:
        driver = self.driver
        #取出测试所需的ip和子网掩码列表
        ip,netmask = data.ip_netmask()
        result = []
        i = 0
        #ip和子网掩码列表共有4项，循环取值测试
        while(i<4):
            #修改IP和子网掩码
            commonconfig_control.set_lan_custom_netmask(self,ip[i],netmask[i])
            #点击保存应用
            lan_control.apply(self)
            time.sleep(60)

            #禁用网卡,然后再启用网卡(必须root用户)
            lan_network_control.networkcard_disable_enable()

            #ping路由ip,返回0为ping通，其他为不通
            m = lan_network_control.get_ping(ip[i])
            #把每次ping返回的值传给result列表
            result.append(m)
            driver.refresh()
            driver.implicitly_wait(10)

            #进入lan页面
            goin_lan(self)
            #完成后取ip和netmask的其他测试数据进行测试
            i +=1
        return result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"修改lan ip和netmask过程失败，原因如下：\n%s"%e

#描述：测试用例100msh0056测试步骤----lan自定义子网掩码设置
def step_100msh0056(self):
    try:
        driver = self.driver
        #取出测试所需的ip和子网掩码列表
        ip,netmask = data.custom_ip_netmask()
        result = []
        i = 0
        #ip和子网掩码列表共有4项，循环取值测试
        while(i<4):
            #修改IP和子网掩码
            commonconfig_control.set_lan_custom_netmask(self,ip[i],netmask[i])
            #点击保存应用
            lan_control.apply(self)
            time.sleep(60)

            #禁用网卡,然后再启用网卡(必须root用户)
            lan_network_control.networkcard_disable_enable()

            #登录ssh取路由lan的子网掩码
            m = lan_network_control.router_lan_inet(ip[i])
            #如果子网掩码正确，把数字1传给result,否则传数字0
            if netmask[i] in m:
                result.append(1)
            else:
                result.append(0)
            driver.implicitly_wait(20)

            #进入lan页面
            goin_lan(self)
            #完成后取ip和netmask的其他测试数据进行测试
            i +=1
        return result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"lan自定义子网掩码设置过程失败，原因如下：\n%s"%e

#描述：测试用例100msh0057测试步骤----lan广播地址配置有效性测试
def step_100msh0057(self):
    try:
        driver = self.driver
        time.sleep(5)
        result = []
        #取出测试所需的广播地址
        for broadcast in data.lan_broadcast():
            #修改广播地址
            commonconfig_control.set_lan_broadcast(self,broadcast)
            #点击保存应用
            lan_control.apply(self)
            time.sleep(60)
            ssh_user = data.ssh_user()
            #登录ssh输入ifconfig
            m = lan_network_control.router_lan_inet(ssh_user[0])
            #如果广播地址正确，把数字1传给result,否则传数字0
            if broadcast in m:
                result.append(1)
            else:
                result.append(0)

            #使用默认ip登录lan页面
            goin_default_lan(self)

        return result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"修改lan广播地址过程失败，原因如下：\n%s"%e

#描述：测试用例100msh0059测试步骤----IP地址池默认起始值检查
def step_100msh0059(self):
    try:
        driver = self.driver
        #取出IP地址池默认起始值
        result = dhcpserver_control.get_lan_dhcp_startip(self)
        return result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"IP地址池默认起始值检查过程失败，原因如下：\n%s"%e

#描述：测试用例100msh0067,68测试步骤----异常输入测试
def step_100msh0067_100msh0068(self):
    try:
        driver = self.driver
        result = []
        for character in data.lan_illegal_character():
            #修改LAN IP地址为非法字符
            commonconfig_control.set_lan_ip(self,character)
            lan_control.apply(self)
            #获取页面上的警告信息
            alert=lan_control.get_alert(self)
            assert alert,u"异常输入没有警告信息,无法进行下一步"
            #得到警告信息的文本信息
            text = alert.text
            #如果警告信息的文本信息正确，把数字1传给result,否则传数字0
            if text == u'一些项目的值无效，无法保存！':
                result.append(1)
            else:
                result.append(0)
            #点击警告信息的确认按钮
            alert.accept()
            #点击复位恢复默认配置
            lan_control.reset(self)
        return result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"异常输入测试过程失败，原因如下：\n%s"%e


__author__ = 'zeng'
