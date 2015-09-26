#coding=utf-8
#描述：该模块为interface设置下网络模块控制层
#作者：曾祥卫

from publicControl import public_control
from connect import ssh
from data import data

#编号：Func_interface_09
#描述：Client端ping str(ip地址或域名)
#输入：self,str
#输出：ping(为0-能够ping通,不为0-不能ping通)
def get_ping(str):
    ping = public_control.get_ping(str)
    return

#编号：Func_interface_13
#描述：通过ssh登录路由后台,检查路由是否能够访问网络
#输入：self
#输出：True-能上网，Flase-不能上网
def router_access_internet(self):
    try:
        result = ssh.ssh_cmd2('ping www.baidu.com -c 3')
        return "0% packet loss" in result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"ssh登录路由取值失败，原因如下：\n%s"%e


__author__ = 'zeng'
