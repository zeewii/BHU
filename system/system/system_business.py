#coding=utf-8

#作者：孔志兵

from system.system import system_control
from login import login_control
import os,time
from connect.ssh import ssh_cmd


#描述：将路由器的时间转变成星期 月 日 时 分 Sep 16 13:42:03 年格式
def get_local_time(self):
    system_control.get_time_button(self)
    local_time = system_control.get_local_time(self)
    #以下将显示的时间分割成年，月，日，星期，时和分
    list1 = local_time.split(' ')
    list2 = list1.pop(3)
    list3 = list2.split(':')
    list4 = list3.pop()
    return list1.extend(list3)

#描述：将本地时间转变成星期 月 日 时 分 Sep 16 13:42:03 年格式
def get_pc_time(self):
    pc_time = system_control.get_pc_time(self)
      #以下将显示的时间分割成年，月，日，星期，时和分
    list1 = pc_time.split(' ')
    list2 = list1.pop(2)
    list3 = list1.pop(3)
    list4 = list3.split(':')
    list5 = list4.pop()
    return list1.extend(list4)

#测试默认主机没是否有效
def hostnameValidate(hostname,host,user,pwd,cmd):
        ssh_cmd(host,user,pwd,cmd)
        time.sleep(50)
        str1= 'ping %s -c 3' %hostname
        #通过ping主机名来判断主机名是否验证成功
        ping = os.system(str1)
        if ping == 0 :
            return True
        else :
            return  False

#描述：测试修改后的主机名是否有效
def hostname_logic(self,hostname,host,user,pwd,cmd):
     system_control.set_hostname(self,hostname)
     system_control.submit(self)
     result = hostnameValidate(hostname,host,user,pwd,cmd)
     return result



__author__ = 'kzb'
