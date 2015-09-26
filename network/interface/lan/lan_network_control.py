#coding=utf-8
#描述：该模块为LAN设置下：client端输入命令,路由后台命令的模块控制层
#作者：曾祥卫

from selenium import webdriver
from login import login_control
import time,os,commands,pexpect
from connect import ssh
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from data import data
from publicControl import public_control

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

#编号：Func_interface_10
#描述：Client端在终端输入命令,命令结果返回给函数
#输入：self,cmd-client在终端输入的命令
#输出：output-在终端显示的结果
def client_cmd(cmd):
    public_control.client_cmd(cmd)


#####################################
#以下为路由后台命令
#####################################

#编号：Func_interface_11
#描述：通过ssh登录路由后台,查看路由器lan口的网络信息
#输入：ip:登录的ip地址
#输出：ifocnfig-在终端显示的结果
def router_lan_inet(ip):
    try:
        ssh_user = data.ssh_user()
        ifocnfig = ssh.ssh_cmd(ip,ssh_user[1],\
                               ssh_user[2],'ifconfig br-lan | grep inet')
        return ifocnfig
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"查看路由器lan口的网络信息失败，原因如下：\n%s"%e

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



__author__ = 'zeng'
