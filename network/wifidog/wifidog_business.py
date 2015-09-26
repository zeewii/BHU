#coding:utf-8
#描述：主要编写门户认证-的业务层模块
#作者：尹霞

import general_control,terlist_control,weblist_control,network_control
from network.privoxy import privoxy_control

import time,random

#描述：修改门户认证开关状态-保存-检查是否存在wifidog进程
#输入：self,status-状态
#输出：True-存在，反之
def edit_wifidog(self,status):
    general_control.set_wifidog_enable(self,status)
    general_control.apply(self)
    time.sleep(40)
    return network_control.ssh_wifidog()

#描述：任证-访问网页查看广告
#输入：self,status-状态
#输出：js代码
def redirest_network(self):
    result1 = network_control.ssh_wifidog()
    assert result1 ,u"wifidog进程没起来，无法进行下一步"
    result2 = network_control.rand_redirect(self)
    assert result2,u"网页认证不成功，无法进行下一步"
    result3 = network_control.rand_network(self)
    assert result3,u"认证后网页访问失败，无法进行下一步"
    data = privoxy_control.get_js(self)
    return data

#描述：修改网关id->保存->获取
#输入：self,status-状态
#输出：none
def edit_gatewayid(self,id):
    general_control.set_gatewayId(self,id)
    general_control.apply(self)
    time.sleep(40)

#描述：修改认证服务器->保存->获取-》查看wifidog进程
#输入：self,hostname-认证服务器
#输出：none
def edit_hostname(self,hostname):
    general_control.set_wifidog_hostname(self,hostname)
    general_control.apply(self)
    time.sleep(40)
    result = network_control.ssh_wifidog()
    assert result ,u"wifidog进程没起来，无法进行下一步"

#描述：设置本机mac为终端白名单逻辑流程：进入终端白名单页面-》获取本机mac->
#     设置本机mac为终端白名单->保存->获取trusted表中的值-》访问网页
#输入：self,hostname-认证服务器
#输出：none
def edit_one_terlist(self):
    terlist_control.tabmenu_terlist(self)
    localmac = terlist_control.get_localmac()
    terlist_control.set_maclist(self,0,localmac)
    terlist_control.apply(self)
    time.sleep(40)
    data = terlist_control.ssh_get_trusted()
    assert localmac.upper() in data,u"本地mac地址没有加入iptables表中，无法进行下一步"
    print network_control.rand_network(self)
    return network_control.rand_network(self)

#描述：设置多条终端白名单流程：进入终端白名单页面-》判断添加的数量是否大于1->
#    添加终端白名单->保存->获取并返回trusted表中的值
#输入：self,maclist-mac列表，count-添加条数
#输出：none
def edit_terlist(self,maclist,count):
    terlist_control.tabmenu_terlist(self)
    if count>1:
        i = 0
        while(i<count-1):
            terlist_control.set_maclist(self,0,maclist[i])
            terlist_control.add_button(self)
            i+=1
        terlist_control.set_maclist(self,0,maclist[i])
        terlist_control.apply(self)
        time.sleep(40)
        data = terlist_control.ssh_get_trusted()
        return data
    else:
        print u"没有添加数据"


#描述：设置终端白名单输入容错性流程：进入终端白名单页面-》设置mac地址>保存->获取弹框
#输入：self,mac
#输出：none
def edit_errorlist(self,mac):
    terlist_control.tabmenu_terlist(self)
    terlist_control.set_maclist(self,0,mac)
    terlist_control.apply(self)
    time.sleep(2)
    return terlist_control.validate(self)

#描述：清空终端白名单流程：进入终端白名单页面-》判断添加的数量是否大于1->
#    添加终端白名单->保存->获取并返回trusted表中的值
#输入：self
#输出：none
def remove_terlist(self):
    terlist_control.tabmenu_terlist(self)
    while(1):
        terlist_control.remove_button(self,1)
        tmp = terlist_control.get_maclist(self)
        if tmp==['']:break
    terlist_control.apply(self)
    time.sleep(40)


#描述：设置网站白名单流程：进入网站白名单页面-》设置白名单地址>保存->获取弹框
#输入：self,网站地址列表
#输出：none
def add_weblist(self,weblist):
    weblist_control.tabmenu_weblist(self)
    for i in weblist:
        weblist_control.add_button(self)
        weblist_control.set_web(self,0,i)
    weblist_control.apply(self)
    time.sleep(40)
    result = network_control.ssh_wifidog()
    assert result ,"wifidog进程没起来，无法进行下一步"

#描述：删除网站白名单流程：进入网站白名单页面-》获取weblist列表做验证使用>
# 清空网站白名单-》保存->验证wifidog起来-》从weblist中验证个是否能正常进行认证
#输入：self
#输出：none
def remove_web(self):
    weblist_control.tabmenu_weblist(self)
    weblist = weblist_control.get_weblist(self)
    while(1):
        weblist_control.remove_button(self,1)
        tmp = weblist_control.get_weblist(self)
        if tmp==['']:break
    weblist_control.apply(self)
    time.sleep(40)
    result = network_control.ssh_wifidog()
    assert result ,"wifidog进程没起来，无法进行下一步"
    web = random.sample(weblist,1)
    print u"现在验证删除网站白名单的%s,是否生效"%web
    return network_control.redirect(self,web)

#描述：修改一般设置为默认状态
#输入：self
#输出：None
def default_general(self):
    general_control.set_wifidog_enable(self,True)
    general_control.set_gatewayId(self,"44060430603381")
    general_control.set_checkInterval(self,300)
    general_control.set_clientTimeout(self,50)
    general_control.set_wifidog_hostname(self,"wifi.100msh.com")
    general_control.set_wifidog_url(self,"/index/")
    general_control.apply(self)
    time.sleep(40)

#描述：修改网站白名单为默认状态
#输入：self
#输出：None
def default_weblist(self):
    weblist_control.tabmenu_weblist(self)
    while(1):
        weblist_control.remove_button(self,1)
        tmp = weblist_control.get_weblist(self)
        if tmp==['']:break
    weblist_control.set_web(self,1,"img.100msh.net")
    weblist_control.add_button(self)
    weblist_control.set_web(self,2,"wifiauth.100msh.com")
    weblist_control.add_button(self)
    weblist_control.set_web(self,3,"m.100msh.com")
    general_control.apply(self)
    time.sleep(40)

#描述：重启路由器
#输入：None
#输出：None
def reboot(self):
    general_control.ssh_reboot()
    time.sleep(120)

