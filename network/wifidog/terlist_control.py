#coding:utf-8
#描述:编写门户认证-终端白名单控制层代码
#作者：尹霞
from connect import ssh
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from publicControl import public_control

#描述:进入“终端白名单”子菜单
#输入:self
#输出:None
def tabmenu_terlist(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        tabmenu = driver.find_element_by_link_text(u"终端白名单")
        tabmenu.click()
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-终端白名单页面跳转失败,原因如下：%s" %e

#描述:获取mac列表
#输入:self
#输出:maclist- mac列表注意是list类型的值
def get_maclist(self):
    driver = self.driver
    driver.implicitly_wait(10)
    maclist = []
    try:
        list = driver.find_elements_by_name("cbid.wifidog.default.__mac_list")
        for i in list:
            tmp = i.get_attribute('value')
            maclist.append(tmp)
        return maclist
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-终端白名单获取mac列表失败,原因如下：%s" %e

#描述:获取一个mac地址
#输入:self，num-第几个mac,0为最后一个
#输出:mac地址
def get_mac(self,num):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        list = driver.find_elements_by_name("cbid.wifidog.default.__mac_list")
        mac = list[num-1].get_attribute('value')
        return mac
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-终端白名单获取mac列表失败,原因如下：%s" %e

#描述:设置mac信息
#输入:self,num-修改第几个mac,mac-要修改的MAC 地址,直接修改最后一个num输入0
#输出:None
def set_maclist(self,num,mac):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        maclist = driver.find_elements_by_name("cbid.wifidog.default.__mac_list")
        maclist[num-1].clear()
        maclist[num-1].send_keys(mac)
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-修改mac信息失败,原因如下：%s" %e

#描述:点击添加按钮
#输入:self
#输出:None
def add_button(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        maclist = driver.find_elements_by_name("cbid.wifidog.default.__mac_list")
        imagelist = driver.find_elements_by_class_name("cbi-image-button")
        count = len(maclist)
        imagelist[count-1].click()
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-点击添加按钮失败,原因如下：%s" %e

#描述:点击删除按钮,只能从前往后删除，最后一个不能删除
#输入:self，num-删除第几个mac
#输出:None
def remove_button(self,num):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        imagelist = driver.find_elements_by_class_name("cbi-image-button")
        if len(imagelist)==1:
            imagelist[-1].clear()
        imagelist[num-1].click()
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-点击删除mac地址按钮失败,原因如下：%s" %e

#描述:无效的MAC 地址是否显示提示框信息
#输入:self
#输出:提示框数据
def validate(self):
    driver = self.driver
    try:
    #获取页面警告信息
        alert = driver.switch_to_alert()
        data = alert.text
        alert.accept()
        return data
    except (NoAlertPresentException,Exception),e:
        print u"提示框弹出失败,原因如下：%s" %e

#描述:点击页面的保存&应用
#输入:self
#输出:None
def apply(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        apply = driver.find_element_by_name("cbi.apply")
        apply.click()
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-点击应用失败,原因如下：%s" %e

#描述:从ssh远程命令获取后台WiFiDog_br-lan_Trusted中的终端白名单数据
#输入:None
#输出:truse-iptables中WiFiDog_br-lan_Trusted数据，即终端白名单数据
def ssh_get_trusted():
    try:
        truse = ssh.ssh_cmd2("iptables -t mangle -L WiFiDog_br-lan_Trusted")
        return truse
    except Exception,e:
        print u"从ssh获取iptables表中终端百白名单失败。原因如下：%s"%e

#描述:获取本机mac地址-从public中继承
#输入:None
#输出:本机mac
def get_localmac():
    return public_control.get_localmac()






