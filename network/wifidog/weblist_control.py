#coding:utf-8
#描述:网站白名单控制层功能
#作者：尹霞
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from connect import ssh
#描述:进入系统-》“终端白名单”子菜单
#输入:self
#输出:None
def tabmenu_weblist(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        tabmenu = driver.find_element_by_link_text(u"网站白名单")
        tabmenu.click()
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-网站白名单页面跳转失败,原因如下：%s" %e

#描述:获取所有的域名白名单列表
#输入:self
#输出:weblist-域名白名单列表
def get_weblist(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        list = driver.find_elements_by_name("cbid.wifidog.default.__Accessname")
        weblist = []
        for i in list:
            tmp = i.get_attribute('value')
            weblist.append(tmp)
        return weblist
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-获取网站白名单列表信息失败,原因如下：%s" %e

#描述:获取某一个域名白名单
#输入:self，num-第几个域名
#输出:web-域名白名单地址
def get_web(self,num):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        list = driver.find_elements_by_name("cbid.wifidog.default.__Accessname")
        web = list[num-1].get_attribute('value')
        return web
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-获取单个网站白名单信息失败,原因如下：%s" %e

#描述:设置web域名信息
#输入:self,num-修改第几个,url-web地址,直接修改最后一个num输入0
#输出:None
def set_web(self,num,url):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        maclist = driver.find_elements_by_name("cbid.wifidog.default.__Accessname")
        maclist[num-1].clear()
        maclist[num-1].send_keys(url)
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-修改web白名单信息失败,原因如下：%s" %e

#描述:点击添加按钮,该页面有个不易去区分的元素imagelist-其包括了终端白名单中的增加、删除按钮
#输入:self
#输出:None
def add_button(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        imagelist = driver.find_elements_by_class_name("cbi-image-button")
        imagelist[-1].click()
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-网站白名单点击添加按钮失败,原因如下：%s" %e

#描述:点击删除按钮或清空数据,总个数-终端白名单的个数=网站白名单数
#输入:self,num-第几个》=1
#输出:None
def remove_button(self,num):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        maclist = driver.find_elements_by_name("cbid.wifidog.default.__mac_list")
        weblist = driver.find_elements_by_name("cbid.wifidog.default.__Accessname")
        imagelist = driver.find_elements_by_class_name("cbi-image-button")
        if len(weblist)>1:
            result = len(maclist)+num -1
            imagelist[result].click()
        else:
            weblist[0].clear()
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-网站白名单点击删除按钮失败,原因如下：%s" %e

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
        print u"门户认证-网站白名单点击保存&应用按钮失败,原因如下：%s" %e

#描述:通过ssh下达命令“cat /etc/config/wifidog”,获取Accessname信息
#输入:self
#输出:wifidog配置信息
def ssh_get_weblist():
    try:
        cmd = "cat /etc/config/wifidog"
        result = ssh.ssh_cmd2(cmd)
        return result
    except Exception,e:
        print u"ssh获取wifidog配置信息失败，原因如下：%s"%e


