#coding=utf-8
#描述：该模块为dhcpdns设置的业务逻辑模块.
#作者：曾祥卫

from data import data
from network.interface import interface_business,interface_control
from login import login_control
import dhcpdns_control,dhcpdns_network_control
from publicControl import public_control
from network.wifidog import network_control
from connect import ssh
import time


#描述：使用默认ip登录DHCP/DNS页面
def goin_default_dhcpdns(self):
    try:
        driver = self.driver
        #默认IP登录路由web页面
        web_user_password = data.default_web_user_password()
        interface_business.open_router_web(self,web_user_password[0])
        #登录路由
        login_control.set_user(self,web_user_password[1],web_user_password[2])
        login_control.submit(self)
        #进入DHCP/DNS页面
        dhcpdns_control.dhcpdns_menu(self)
        driver.implicitly_wait(10)
     #捕捉异常并打印异常信息
    except Exception,e:
        print u"使用默认ip登录DHCP/DNS页面失败，原因如下：\n%s"%e

#描述：添加第一项域名绑定
def add_dns(self,domain,ip):
    try:
        driver = self.driver
        #点击域名绑定中的添加按钮
        dhcpdns_control.add_domain_hijacking_settings(self)
        #添加第一条规则
        dhcpdns_control.set_first_dhs(self,domain,ip)
        #点击保存应用
        dhcpdns_control.apply(self)
        driver.implicitly_wait(20)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"添加第一项域名绑定的过程失败，原因如下：\n%s"%e

#描述：删除页面上所有的规则
def delete_all_list(self):
    try:
        driver = self.driver
        #删除所有规则
        dhcpdns_control.delete_all_dhs(self)
        #点击保存应用
        dhcpdns_control.apply(self)
        driver.implicitly_wait(20)
        time.sleep(10)
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"使删除页面上所有的规则失败，原因如下：\n%s"%e

###############################################
#以下是域名绑定的测试步骤
###############################################


#描述：测试用例100msh0160测试步骤----有效域名绑定测试
def step_100msh0160(self):
    try:
        #添加域名绑定规则
        domain,ip = data.domain_hijacking_1()
        add_dns(self,domain[0],ip[0])
        time.sleep(20)
        #client解析该域名
        nslookup = dhcpdns_network_control.nslookup(domain[0])
        #解析正确返回1,错误返回0
        if ip[0] in nslookup:
            result =1
        else:
            result =0
        #删除页面上所有的规则
        delete_all_list(self)
        #结果返回给函数
        return result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"绑定有效的域名的过程失败，原因如下：\n%s"%e

#描述：测试用例100msh0161测试步骤----无效域名绑定测试
def step_100msh0161(self):
    try:
        #添加域名绑定规则
        domain,ip = data.domain_hijacking_1()
        add_dns(self,domain[1],ip[1])
        time.sleep(20)
        #client解析该域名
        nslookup = dhcpdns_network_control.nslookup(domain[1])
        #解析正确返回1,错误返回0
        if ip[1] in nslookup:
            result =1
        else:
            result =0

        #结果返回给函数
        return result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"绑定无效的域名的过程失败，原因如下：\n%s"%e

#描述：测试用例100msh0163测试步骤----域名绑定后重启测试
def step_100msh0163(self):
    try:
        #重启路由
        dhcpdns_network_control.reboot_router()
        domain,ip = data.domain_hijacking_1()
        #client解析该域名
        nslookup = dhcpdns_network_control.nslookup(domain[1])
        #解析正确返回1,错误返回0
        if ip[1] in nslookup:
            result =1
        else:
            result =0
        #结果返回给函数
        return result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"域名绑定后重启的过程失败，原因如下：\n%s"%e

#描述：测试用例100msh0164测试步骤----域名绑定最大限制测试
def step_100msh0164(self):
    try:
        driver = self.driver
        #点击添加按钮30次
        i = 0
        while(i<30):
            dhcpdns_control.add_domain_hijacking_settings(self)
            i +=1
        #点击保存应用
        dhcpdns_control.apply(self)
        driver.implicitly_wait(20)
        time.sleep(20)

        a = []
        #选出所有规则的输入框
        classes = driver.find_elements_by_class_name("cbi-input-text")
        #逐个取出每个输入框
        for b in classes:
            #把所有元素添加到a序列中
            a.append(b)
        #print len(a)
        #总共28条，56个输入框
        assert len(a) == 56,u"域名绑定最大规则数不为28条，fail"

        #所有组输入对应的域名和ip
        domain,ip = data.domain_hijacking_all()
        dhcpdns_control.set_all_dhs(self,domain,ip)
        #点击保存应用
        dhcpdns_control.apply(self)
        driver.implicitly_wait(20)
        time.sleep(10)

        #随机域名解析3个添加的域名
        nslookup0 = dhcpdns_network_control.nslookup(domain[0])
        nslookup14 = dhcpdns_network_control.nslookup(domain[14])
        nslookup27 = dhcpdns_network_control.nslookup(domain[27])
        #解析正确返回1,错误返回0
        if ip[0] in nslookup0 and ip[14] in nslookup14 and ip[27] in nslookup27:
            result =1
        else:
            result =0

        #删除所有规则
        delete_all_list(self)
        #结果返回给函数
        return result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"设置域名绑定最大限制的过程失败，原因如下：\n%s"%e

#描述：测试用例100msh0165测试步骤----域名相同IP不同时绑定
def step_100msh0165(self):
    try:
        driver = self.driver
        #点击添加按钮10次
        i = 0
        while(i<10):
            dhcpdns_control.add_domain_hijacking_settings(self)
            i +=1
        domain,ip = data.domain_hijacking_2()
        #所有组输入对应的域名和ip
        dhcpdns_control.set_all_dhs(self,domain,ip)
        #点击保持应用
        dhcpdns_control.apply(self)
        driver.implicitly_wait(20)
        time.sleep(20)

        #client解析该域名，判断最后一项规则是否生效
        nslookup = dhcpdns_network_control.nslookup(domain[9])
        #解析正确返回1,错误返回0
        if ip[9] in nslookup:
            result =1
        else:
            result =0
        #结果返回给函数
        return result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"域名相同IP不同时绑定的过程失败，原因如下：\n%s"%e

#描述：测试用例100msh0166测试步骤----IP相同域名不同时绑定
def step_100msh0166(self):
    try:
        driver = self.driver
        domain,ip = data.domain_hijacking_3()
        #所有组输入对应的域名和ip
        dhcpdns_control.set_all_dhs(self,domain,ip)
        #点击保持应用
        dhcpdns_control.apply(self)
        driver.implicitly_wait(20)
        time.sleep(20)

        #随机域名解析3个添加的域名
        nslookup0 = dhcpdns_network_control.nslookup(domain[0])
        nslookup4 = dhcpdns_network_control.nslookup(domain[4])
        nslookup9 = dhcpdns_network_control.nslookup(domain[9])
        #解析正确返回1,错误返回0
        if ip[0] in (nslookup0 and nslookup4 and nslookup9):
            result =1
        else:
            result =0
        #删除所有规则
        delete_all_list(self)
        #结果返回给函数
        return result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"IP相同域名不同时绑定的过程失败，原因如下：\n%s"%e

#描述：测试用例100msh0167测试步骤----域名绑定时不绑定网络名
def step_100msh0167(self):
    try:
        result = []
        #有两项规则，取两次数据进行测试
        i = 0
        while(i<2):
            domain,ip = data.domain_hijacking_4()
            #添加第一条规则
            add_dns(self,domain[i],ip[i])
            time.sleep(20)
            #client解析该域名
            nslookup = dhcpdns_network_control.nslookup('www.baidu.com')
            #解析正确返回1,错误返回0
            if ip[i] in nslookup:
                result.append(1)
            else:
                result.append(0)
            #删除页面上所有的规则
            delete_all_list(self)
            i +=1
        #结果返回给函数
        return result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"域名绑定时不绑定网络名的过程失败，原因如下：\n%s"%e

#描述：测试用例100msh0168测试步骤----域名绑定时只绑定主机名
def step_100msh0168(self):
    try:
        domain,ip = data.domain_hijacking_5()
        #添加第一条规则
        add_dns(self,domain[0],ip[0])
        time.sleep(20)
        #client解析该域名
        nslookup = dhcpdns_network_control.nslookup('www.baidu.com')
        #解析正确返回1,错误返回0
        if ip[0] not in nslookup:
            result = 1
        else:
            result = 0
        #删除页面上所有的规则
        delete_all_list(self)
        #结果返回给函数
        return result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"域名绑定时只绑定主机名的过程失败，原因如下：\n%s"%e


###############################################
#以下是自定义静态ip的测试步骤
###############################################

#描述：测试用例100msh0169测试步骤----DHCP静态地址分配
def step_100msh0169(self):
    try:
        driver = self.driver

        #点击自定义静态ip上的添加按钮
        dhcpdns_control.add_static_leases(self)
        #取client自己的mac
        mac = public_control.get_localmac()
        #ip从lan_broadcast中取第一个ip
        ip = data.lan_broadcast()
        dhcpdns_control.set_first_static_leases(self,mac,ip[0])
        #点击保持应用
        dhcpdns_control.apply(self)
        driver.implicitly_wait(20)
        time.sleep(10)
        #重启路由
        dhcpdns_network_control.reboot_router()
        #取client的ip
        ifconfig = dhcpdns_network_control.client_cmd('ifconfig eth0 | grep inet')
        #如果所设ip是client现在的ip，返回1,否则返回0
        if ip[0] in ifconfig:
            result = 1
        else:
            result = 0

        #使用默认ip登录DHCP/DNS页面
        goin_default_dhcpdns(self)
        #删除页面上所有的规则
        delete_all_list(self)
        #结果返回给函数
        return result
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"添加DHCP静态地址的过程失败，原因如下：\n%s"%e


__author__ = 'zeng'
