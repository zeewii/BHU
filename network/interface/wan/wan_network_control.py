#coding=utf-8
#描述：该模块为WAN设置下：client端输入命令,路由后台命令的模块控制层
#作者：曾祥卫

from selenium import webdriver
import time,os,commands,pexpect
from connect import ssh
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from data import data
from publicControl import public_control
from network.wifidog import network_control

#####################################
#以下为client端输入命令
#####################################

#编号：Func_interface_08
#描述：禁用网卡,然后再启用网卡(必须root用户)
#输入：self
#输出：None
def networkcard_disable_enable():
    try:
        password = data.client_password()
        #禁用eth0网卡
        down = pexpect.spawn('sudo ifconfig eth0 down')
        down.expect(':')
        down.sendline(password)
        time.sleep(10)

        #启用eth0网卡
        up = pexpect.spawn('sudo ifconfig eth0 up')
        up.expect(':')
        up.sendline(password)
        time.sleep(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"禁用网卡,然后再启用网卡失败，原因如下：\n%s"%e

#编号：Func_interface_09
#描述：Client端ping str(ip地址或域名)
#输入：self,str
#输出：ping(为0-能够ping通,不为0-不能ping通)
def get_ping(str):
    ping = public_control.get_ping(str)
    return ping



#####################################
#以下为路由后台命令
#####################################

#编号：Func_interface_12
#描述：通过ssh登录路由后台,查看路由器wan口的网络信息
#输入：none
#输出：ifocnfig-在终端显示的结果
def router_wan_inet():
    try:
        ifocnfig = ssh.ssh_cmd2('ifconfig eth1')
        return ifocnfig
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"查看路由器wan口的网络信息失败，原因如下：\n%s"%e

#编号：Func_interface_13
#描述：通过ssh登录路由后台,输入reboot重启路由,并等待60s
#输入：self
#输出：None
def reboot_router():
    try:
        #在路由器中输入reboot
        ssh.ssh_cmd2('reboot')
        time.sleep(60)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"reboot重启路由失败，原因如下：\n%s"%e

#编号：Func_interface_14
#描述：通过ssh登录路由后台,检查路由是否能够访问网络
#输入：self
#输出：True-能上网，False-不能上网
def router_access_internet():
    try:
        ssh_user = data.ssh_user()
        result = ssh.ssh_cmd2('ping www.baidu.com -c 3')
        if "0% packet loss" in result:
            return True
        else:
            return False
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"ssh登录路由取值失败，原因如下：\n%s"%e

#编号：Func_interface_15
#描述:ssh获取wifidog进程，并判断是否存在
#输入:None
#输出:True-存在，False-不存在
def ssh_wifidog():
    return network_control.ssh_wifidog()

#编号：Func_interface_16
#描述:client端ping mtu的值返回结果
#输入:mtu
#输出:ping结果0-真，反之
def get_mtu(mtu):
    try:
        ping = "ping www.baidu.com -c 3 -s %s -M do"%mtu
        result = os.system(ping)
        return result
    except Exception,e:
        print u"ping命令执行失败。原因如下：%s"%e



__author__ = 'zeng'
