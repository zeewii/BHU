#coding:utf-8
#描述：主要编写门户认证-基本设置的控制层模块
#作者：尹霞

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import random,string
from publicControl import public_control
from connect import ssh
#描述:进入网络页面-移动鼠标到网络，点击“门户认证”，进入门户认证默认页面
#输入:self
#输出:None
def wifidog_menu(self):
    public_control.menu(self,u"网络",u"门户认证")

#描述:进入系统-》“基本设置”子菜单
#输入:self
#输出:None
def tabmenu_general(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        tabmenu = driver.find_element_by_link_text(u"基本设置")
        tabmenu.click()
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-基本设置页面跳转失败,原因如下：%s" %str(e)

#描述:获取页面门户认证开关的状态
#输入:self
#输出:status-1开启，0关闭
def get_wifidog_enable(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        wifidog_enable = driver.find_element_by_id("cbid.wifidog.default.wifidog_enable")
        status = wifidog_enable.is_selected()
        return status
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-获取开关失败,原因如下：%s" %str(e)

#描述:设置页面门户认证开关的状态
#输入:self,status-设置的状态1-开，0-关
#输出:None
def set_wifidog_enable(self,status):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        wifidog_enable = driver.find_element_by_id("cbid.wifidog.default.wifidog_enable")
        before = get_wifidog_enable(self)
        if before == status:
            print u"门户认证开关状态已经变为%s"%status
        else:
            wifidog_enable.click()
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-设置开关失败,原因如下：%s" %str(e)

#描述:获取页面门户认证的认证模式
#输入:self
#输出:status-remote-远程认证,local-本地认证
def get_wifidog_mode(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        mode = driver.find_element_by_id("cbid.wifidog.default.mode")
        status = mode.get_attribute('value')
        return status
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-获取认证模式失败,原因如下：%s" %str(e)

#描述:设置页面门户认证的认证模式
#输入:self,str-模修改的模式：remote/local
#输出:None
def set_wifidog_mode(self,mode):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        Mode = driver.find_element_by_id("cbid.wifidog.default.mode")
        option = "//option[@value='%s']" %mode
        ActionChains(driver).click_and_hold(Mode).perform()
        Mode.find_element_by_xpath(option).click()
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-设置认证模式失败,原因如下：%s" %str(e)

#描述:获取页面门户认证的网管id
#输入:self
#输出:网关id
def get_gatewayId(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        GatewayID = driver.find_element_by_id("cbid.wifidog.default.GatewayID")
        gatewayId = GatewayID.get_attribute('value')
        return gatewayId
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-获取网关id失败,原因如下：%s" %str(e)

#描述:设置页面门户认证的网管id
#输入:self,id-网关id
#输出:None
def set_gatewayId(self,id):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        GatewayID = driver.find_element_by_id("cbid.wifidog.default.GatewayID")
        GatewayID.clear()
        if id!=None:
            GatewayID.send_keys(id)
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-设置网关id失败,原因如下：%s" %str(e)

#描述:随机设置页面门户认证的网关id
#输入:self,函数自动随机生成12位的网关id,id由数字和字母组成
#输出:None
def set_rand_gatewayId(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        GatewayID = driver.find_element_by_id("cbid.wifidog.default.GatewayID")
        GatewayID.clear()

        tmp = random.sample('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',12)
        id =''.join(tmp)

        GatewayID.send_keys(id)
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-随机设置网关id失败,原因如下：%s" %str(e)

#描述:获取页面门户认证的检查时隔
#输入:self
#输出:检查时隔
def get_checkInterval(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        CheckInterval = driver.find_element_by_id("cbid.wifidog.default.CheckInterval")
        checkInterval = CheckInterval.get_attribute('value')
        return checkInterval
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-获取检查时隔失败,原因如下：%s" %str(e)

#描述:设置页面门户认证的检查时隔
#输入:self，checkInterval-检查时隔
#输出:None
def set_checkInterval(self,checkInterval):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        CheckInterval = driver.find_element_by_id("cbid.wifidog.default.CheckInterval")
        CheckInterval.clear()
        CheckInterval.send_keys(checkInterval)
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-设置检查时隔失败,原因如下：%s" %str(e)

#描述:获取页面门户认证的客户端超时数
#输入:self
#输出:客户端超时数
def get_clientTimeout(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        ClientTimeout = driver.find_element_by_id("cbid.wifidog.default.ClientTimeout")
        clientTimeout = ClientTimeout.get_attribute('value')
        return clientTimeout
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-获取客户端超时数失败,原因如下：%s" %str(e)

#描述:设置页面门户认证的客户端超时数
#输入:self
#输出:客户端超时数
def set_clientTimeout(self,clientTimeout):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        ClientTimeout = driver.find_element_by_id("cbid.wifidog.default.ClientTimeout")
        ClientTimeout.clear()
        ClientTimeout.send_keys(clientTimeout)
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-设置客户端超时数失败,原因如下：%s" %str(e)

#描述:获取基本设置-认证服务器主机名
#输入:self
#输出:hostname-主机名
def get_wifidog_hostname(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        Hostname = driver.find_element_by_id("cbid.wifidog.default.Hostname")
        hostname = Hostname.get_attribute('value')
        return hostname
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-获取认证服务器主机名失败,原因如下：%s" %str(e)

#描述:设置基本设置-认证服务器主机名
#输入:self,hostname-主机名
#输出:None
def set_wifidog_hostname(self,hostname):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        Hostname = driver.find_element_by_id("cbid.wifidog.default.Hostname")
        Hostname.clear()
        Hostname.send_keys(hostname)
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-设置认证主机名失败,原因如下：%s" %str(e)

#描述:获取基本设置-认证服务器web端口
#输入:self
#输出:hostname-web端口
def get_wifidog_httpPort(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        HTTPPort = driver.find_element_by_id("cbid.wifidog.default.HTTPPort")
        httpPort = HTTPPort.get_attribute('value')
        return httpPort
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-获取认证服务器web端口失败,原因如下：%s" %str(e)

#描述:设置基本设置-认证服务器web端口
#输入:self,httpPort-web端口
#输出:None
def set_wifidog_httpPort(self,httpPort):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        HTTPPort = driver.find_element_by_id("cbid.wifidog.default.HTTPPort")
        HTTPPort.clear()
        HTTPPort.send_keys(httpPort)
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-设置认证服务器web端口失败,原因如下：%s" %str(e)

#描述:获取基本设置-认证服务器的url路径
#输入:self
#输出:url路径
def get_wifidog_url(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        Path = driver.find_element_by_id("cbid.wifidog.default.Path")
        url = Path.get_attribute('value')
        return url
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-获取认证服务器url路径失败,原因如下：%s" %str(e)

#描述:基本设置-认证服务器的url路径
#输入:self，url路径
#输出:None
def set_wifidog_url(self,url):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        Path = driver.find_element_by_id("cbid.wifidog.default.Path")
        Path.clear()
        Path.send_keys(url)
    except (NoSuchElementException,Exception) as e:
        print u"门户认证-设置认证服务器url路径失败,原因如下：%s" %str(e)

#描述:点击页面的保存&应用
#输入:self
#输出:None
def apply(self):
    public_control.apply(self)

#描述:点击复位按钮
#输入:self
#输出:None
def reset(self):
    public_control.reset(self)

#描述:ssh-重启路由器
#输入:None
#输出:None
def ssh_reboot():
    data = ssh.ssh_cmd2("reboot")


