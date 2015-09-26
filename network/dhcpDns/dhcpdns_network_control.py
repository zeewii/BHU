#coding=utf-8
#描述：该模块为dhcpDns设置下网络模块控制层
#作者：曾祥卫

from publicControl import public_control
from connect import ssh
from data import data
import commands,time

#编号：Func_dhcpdns_15
#描述：Client端解析指定的域名
#输入：self,domain-指定的域名
#输出：output-返回解析的结果
def nslookup(domain):
    try:
        #Client端在终端输入命令,命令结果返回给函数
        status,output = commands.getstatusoutput('nslookup %s'%domain)
        return output
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"Client端在终端输入命令失败，原因如下：\n%s"%e

#编号：Func_dhcpdns_16
#描述：Client端在终端输入命令,命令结果返回给函数
#输入：self,cmd-client在终端输入的命令
#输出：output-在终端显示的结果
def client_cmd(cmd):
    return public_control.client_cmd(cmd)


#编号：Func_dhcpdns_17
#描述：通过ssh登录路由后台,输入reboot重启路由,并等待60s
#输入：self
#输出：None
def reboot_router():
    try:
        ssh_user = data.ssh_user()
        #在路由器中输入reboot
        ssh.ssh_cmd(ssh_user[0],ssh_user[1],ssh_user[2],'reboot')
        time.sleep(60)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"reboot重启路由失败，原因如下：\n%s"%e

__author__ = 'zeng'
