#coding=utf-8
#描述：该模块为wan设置的业务逻辑模块.
#作者：曾祥卫

from data import data
from network.interface import interface_business,interface_control
import wan_control,wan_network_control
from publicControl import public_control
from network.wifidog import network_control
from connect import ssh
import time

#描述:进入wan页面
def goin_wan(self):
    try:
        #点击WAN上的修改按钮
        interface_control.wan_edit(self)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"进入wan页面页面失败，原因如下：\n%s"%e

#描述：使用默认ip登录wan页面
def goin_default_wan(self):
    try:
        interface_business.goin_default_interface(self)
        goin_wan(self)
     #捕捉异常并打印异常信息
    except Exception,e:
        print u"使用默认ip登录wan页面失败，原因如下：\n%s"%e

#描述：把路由WAN口改为static ip
def change_staticip(self,ip,gw,dns):
    try:
        driver = self.driver
        #协议选择staticip
        wan_control.set_wan_protrocol(self,'staticip')
        #点击切换协议
        wan_control.set_wan_switchprotocol(self)
        driver.implicitly_wait(10)
        #输入wan ip
        wan_control.set_wan_staticip_ip(self,ip)
        #选择C类掩码
        wan_control.set_wan_staticip_netmask(self,'C')
        #输入wan 网关
        wan_control.set_wan_staticip_gateway(self,gw)
        #输入DNS
        wan_control.set_wan_staticip_dns(self,dns)
        wan_control.apply(self)
        time.sleep(60)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"把路由WAN口改为static ip的过程失败，原因如下：\n%s"%e

#描述：把路由WAN口改为DHCP
def change_dhcp(self):
    try:
        driver = self.driver
        #协议选择dhcp
        wan_control.set_wan_protrocol(self,'dhcp')
        #点击切换协议
        wan_control.set_wan_switchprotocol(self)
        driver.implicitly_wait(10)
        #点击保存应用
        wan_control.apply(self)
        time.sleep(60)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"把路由WAN口改为DHCP的过程失败，原因如下：\n%s"%e

#描述：把路由WAN口改为pppoe
def change_pppoe(self,username,password):
    try:
        driver = self.driver
        driver.implicitly_wait(10)
        #协议选择pppoe
        wan_control.set_wan_protrocol(self,'pppoe')
        #点击切换协议
        wan_control.set_wan_switchprotocol(self)
        driver.implicitly_wait(10)
        wan_control.set_wan_pppoe_userpwd(self,username,password)
        #点击保存应用
        wan_control.apply(self)
        time.sleep(60)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"把路由WAN口改为pppoe的过程失败，原因如下：\n%s"%e

#描述：修改wan mac
def change_mac(self,mac):
    try:
        #使用默认ip登录wan页面
        goin_default_wan(self)
        wan_control.wan_advancedsettings(self)
        wan_control.set_wan_mac(self,mac)
        wan_control.apply(self)
        time.sleep(60)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"修改mac过程失败，原因如下：\n%s"%e

#描述：修改mtu值
def change_mtu(self,mtu):
    try:
        #使用默认ip登录wan页面
        goin_default_wan(self)
        wan_control.wan_advancedsettings(self)
        wan_control.set_wan_mtu(self,mtu)
        wan_control.apply(self)
        time.sleep(60)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"修改mtu值过程失败，原因如下：\n%s"%e

#描述：点击接口页面中wan的关闭/连接
def wan_disconnect_connect(self):
    try:
        interface_control.wan_stop(self)
        interface_control.wan_connect(self)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"点击接口页面中wan的关闭/连接的过程失败，原因如下：\n%s"%e

#描述：wan为dhcp时设置主机名
def change_hostname(self,hostname):
    try:
        #设置DHCP的主机名
        wan_control.set_wan_dhcp_hostname(self,hostname)
        wan_control.apply(self)
        time.sleep(60)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"wan为dhcp时设置主机名的过程失败，原因如下：\n%s"%e

#描述：改变pppoe的用户名和密码
def change_pppoe_id_passwd(self,username,password):
    try:
        wan_control.set_wan_pppoe_userpwd(self,username,password)
        #点击保存应用
        wan_control.apply(self)
        time.sleep(60)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"改变pppoe的用户名和密码的过程失败，原因如下：\n%s"%e

###############################################
#以下是wan为static ip时的测试步骤
###############################################

#描述：测试用例100msh0069测试步骤----WAN设置为静态IP地址
def step_100msh0069(self):
    try:
        result = []
        d = data.wan_staticip_data()
        #协议切换成static ip
        change_staticip(self,d[0],d[1],d[2])
        #路由能否访问网络
        ping = wan_network_control.router_access_internet()
        result.append(ping)
        #路由wifidog进程是否存在
        wifidog = wan_network_control.ssh_wifidog()
        result.append(wifidog)
        return result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"WAN设置为静态IP地址过程失败，原因如下：\n%s"%e

#描述：测试用例100msh0070测试步骤----WAN广播地址有效性
def step_100msh0070(self):
    try:
        result = []
        #取出测试所需的广播地址
        for broadcast in data.wan_broadcast():
            #修改广播地址
            wan_control.set_wan_staticip_broadcast(self,broadcast)
            #点击保存应用
            wan_control.apply(self)
            time.sleep(60)
            #登录ssh输入ifconfig
            m = wan_network_control.router_wan_inet()
            #如果广播地址正确，把数字1传给result,否则传数字0
            if broadcast in m:
                result.append(1)
            else:
                result.append(0)
            #使用默认ip登录wan页面
            goin_default_wan(self)
        return result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"修改wan广播地址过程失败，原因如下：\n%s"%e

#描述：测试用例100msh0071测试步骤----自定义DNS的有效性
def step_100msh0071(self):
    try:
        result = []
        #取出测试所需的dns地址
        for dns in data.wan_dns():
            #修改DNS
            wan_control.set_wan_staticip_dns(self,dns)
            #点击保存应用
            wan_control.apply(self)
            time.sleep(60)
            #登录ssh ping 外网
            m = wan_network_control.router_access_internet()
            #把结果加入result列表
            result.append(m)
            #使用默认ip登录wan页面
            goin_default_wan(self)
        return result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"修改wan广播地址过程失败，原因如下：\n%s"%e


#描述：测试用例100msh0072测试步骤----wan口MAC地址克隆
def step_100msh0072(self):
    try:
        #获取路由wan口默认mac
        default_mac = wan_control.get_wan_mac(self)
        #获取PC的mac
        pc_mac = public_control.get_localmac()
        #mac字母改为大写
        PC_MAC = pc_mac.upper()
        #修改路由WAN口mac为pc的mac地址
        change_mac(self,PC_MAC)
        time.sleep(60)
        mac = wan_network_control.router_wan_inet()
        if PC_MAC in mac:
            result = 1
        else:
            result = 0

        #使用默认ip登录wan页面
        goin_default_wan(self)
        #测试完成后修改回默认的mac地址
        change_mac(self,default_mac)
        return result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"wan MAC地址克隆过程失败，原因如下：\n%s"%e

#描述：测试用例100msh0073测试步骤----MTU值有效性确认(使用正确的mtu值测试)
def step_100msh0073_1(self):
    try:
        result = []
        a = wan_network_control.get_ping('www.baidu.com')
        if a != 0:
            #client点击连接网络上网
            network_control.redirect(self,"http://www.haosou.com/")
            time.sleep(10)
        #测试默认mtu值（1500），client端ping数据包大小（减28个字节）来判断MTU值的有效性
        ping1 = wan_network_control.get_mtu('1472')
        ping2 = wan_network_control.get_mtu('1473')
        #print ping1,ping2
        if ping1 == 0 and ping2 != 0:
            result.append(1)
        else:
            result.append(0)

        #使用正确的mtu值测试，并验证有效性
        mtu,mtu_low,mtu_up = data.wan_mtu()
        i = 0
        while(i<2):
            time.sleep(10)
            #修改mtu值
            change_mtu(self,mtu[i])
            time.sleep(10)
            b = wan_network_control.get_ping('www.baidu.com')
            if b != 0:
                #client点击连接网络上网
                network_control.redirect(self,"http://www.haosou.com/")
                time.sleep(10)
            #client端ping数据包大小（减28个字节）来判断MTU值的有效性
            ping3 = wan_network_control.get_mtu(mtu_low[i])
            ping4 = wan_network_control.get_mtu(mtu_up[i])
            #print ping3,ping4
            if ping3 == 0 and ping4 != 0:
                result.append(1)
            else:
                result.append(0)
            i +=1
        return result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"设置正确的mtu值的过程失败，原因如下：\n%s"%e

#描述：测试用例100msh0073测试步骤----MTU值有效性确认(使用错误的mtu值测试)
def step_100msh0073_2(self):
    try:
        result = []
        illegal_mtu = data.wan_illegal_mtu()
        for mtu in illegal_mtu:
            #修改mtu值
            change_mtu(self,mtu)
            alert = wan_control.get_alert(self)
            assert alert ,u"输入错误的mtu值没有警告信息,无法进行下一步"
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
            wan_control.reset(self)
        return result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"输入错误的mtu值的过程失败，原因如下：\n%s"%e


###############################################
#以下是wan为DCHP时的测试步骤
###############################################

#描述：测试用例100msh0074测试步骤----WAN口DHCP获取上网IP
def step_100msh0074(self):
    try:
        result = []
        #切换协议为dhcp
        change_dhcp(self)
        #路由能否访问网络
        ping = wan_network_control.router_access_internet()
        result.append(ping)
        #路由wifidog进程是否存在
        wifidog = wan_network_control.ssh_wifidog()
        result.append(wifidog)
        return result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"把路由WAN口改为DHCP的过程失败，原因如下：\n%s"%e

#描述：测试用例100msh0075测试步骤----重启/重新上电后上网测试
def step_100msh0075(self):
    try:
        wan_network_control.reboot_router()
        time.sleep(10)
        ping = wan_network_control.get_ping('www.baidu.com')
        if ping != 0:
            #client点击连接网络上网
            network_control.redirect(self,"http://www.haosou.com/")
            time.sleep(10)
        #client ping外网返回结果
        result = wan_network_control.get_ping('www.baidu.com')
        return result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"重启/重新上电后上网的过程失败，原因如下：\n%s"%e


#描述：测试用例100msh0076测试步骤----WAN口反复关闭后重新获取IP
def step_100msh0076(self):
    try:
        ping = wan_network_control.get_ping('www.baidu.com')
        if ping != 0:
            #client点击连接网络上网
            network_control.redirect(self,"http://www.haosou.com/")
            time.sleep(10)
        #使用默认ip登录接口页面
        interface_business.goin_default_interface(self)
        i = 0
        #点击WAN口关闭/连接10次
        while(i<11):
            #点击接口页面中wan的关闭/连接
            wan_disconnect_connect(self)
            time.sleep(10)
            assert ping == 0,u"第'%s'次关闭/连接wan口，client不能够上网,无法进行下一步"%(i+1)
            i +=1
        return ping
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"WAN口反复关闭的过程失败，原因如下：\n%s"%e

#描述：测试用例100msh0078测试步骤----主副DNS有效性检查
def step_100msh0078(self):
    try:
        #登录路由取dns值
        dns = ssh.ssh_cmd2('cat /tmp/resolv.conf.auto')
        return dns
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"登录路由取dns值的过程失败，原因如下：\n%s"%e


#描述：测试用例100msh0080测试步骤----发送主机名功能检查
def step_100msh0080(self):
    try:
        #设置主机名
        change_hostname(self,'100msh.com')
        #登录路由取hostname值
        hostname = ssh.ssh_cmd2('cat /etc/config/network | grep hostname')
        return hostname
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"设置主机名的过程失败，原因如下：\n%s"%e


###############################################
#以下是wan为pppoe时的测试步骤
###############################################


#描述：测试用例100msh0083测试步骤----PPPOE拨号功能测试
def step_100msh0083(self):
    try:
        result = []
        id_passwd = data.pppoe_id_passwd()
        #切换协议为pppoe
        change_pppoe(self,id_passwd[0],id_passwd[1])
        #路由能否访问网络
        ping = wan_network_control.router_access_internet()
        result.append(ping)
        #路由wifidog进程是否存在
        wifidog = wan_network_control.ssh_wifidog()
        result.append(wifidog)
        return result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"把路由WAN口改为PPPOE的过程失败，原因如下：\n%s"%e


#描述：测试用例100msh0088测试步骤----错误和正常账号密码交替输入
def step_100msh0088(self):
    try:
        result = []
        i = 0
        #PPPoE错误和正确用户名交替使用3次
        while(i<3):
            #取出正确的和错误的用户名和密码
            id_passwd = data.pppoe_id_passwd()
            err_id_passwd = data.pppoe_err_id_passwd()
            #登录默认ip下路由器的wan设置页面
            goin_default_wan(self)
            #改变pppoe的用户名和密码
            change_pppoe_id_passwd(self,err_id_passwd[0],err_id_passwd[1])
            #路由能否访问网络，错误的用户名和密码应该不能访问网络，返回False
            result_err = wan_network_control.router_access_internet()
            result.append(result_err)
            #登录默认ip下路由器的wan设置页面
            goin_default_wan(self)
            #改变pppoe的用户名和密码
            change_pppoe_id_passwd(self,id_passwd[0],id_passwd[1])
            #路由能否访问网络,正确的用户名和密码应该不能访问网络，返回True
            result_correct = wan_network_control.router_access_internet()
            result.append(result_correct)
            assert result_err == False and result_correct == True,\
                u"第'%s'次错误和正常账号密码交替输入出现错误,无法进行下一步"%(i+1)
            i +=1
        return result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"错误和正常账号密码交替输入的过程失败，原因如下：\n%s"%e






__author__ = 'zeng'
