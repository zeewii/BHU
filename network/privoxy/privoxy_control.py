#coding:utf-8
#描述：如影随行-控制层代码
#作者：尹霞
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from connect import ssh
#描述：进入如影随行页面
#输入：self
#输出：None
def privoxy_menu(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        first = driver.find_element_by_link_text(u"网络")
        ActionChains(driver).move_to_element(first).perform()
        driver.find_element_by_link_text(u"如影随行").click()
    except (NoSuchElementException,Exception) as e:
        print u"异常：页面跳转到如影随行失败,原因如下：%s" %e

#描述：获取如影随行开关状态
#输入：self
#输出：状态，1-开，0-关
def get_redirect_enable(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        wifidog_enable = driver.find_element_by_id("cbid.redirect.Redirect.redirect_enable")
        status = wifidog_enable.is_selected()
        return status
    except (NoSuchElementException,Exception) as e:
        print u"异常：如影随行-获取开关失败,原因如下：%s" %e

#描述:设置如影随行开关的状态
#输入:self
#输出:None
def set_redirect_enable(self,status):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        redirect_enable = driver.find_element_by_id("cbid.redirect.Redirect.redirect_enable")
        if redirect_enable.is_selected()==status:
            print u"如影随行开关已经是%s,不需要再设置"%status
        else:
            redirect_enable.click()
    except (NoSuchElementException,Exception) as e:
        print u"异常：如影随行-设置开关失败,原因如下：%s" %e

#描述:获取如影随行广告服务器信息
#输入:self
#输出:hostname-广告服务器
def get_redirect_Hostname(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        js = driver.find_element_by_id("cbid.redirect.Redirect.Hostname")
        hostname = js.get_attribute('value')
        return hostname
    except (NoSuchElementException,Exception) as e:
        print u"异常：如影随行-获取广告服务器失败,原因如下：%s" %e

#描述:设置如影随行广告服务器信息
#输入:self,str-广告服务器
#输出:None
def set_redirect_Hostname(self,str):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        js = driver.find_element_by_id("cbid.redirect.Redirect.Hostname")
        js.clear()
        if str!=None:
            js.send_keys(str)
    except (NoSuchElementException,Exception) as e:
        print u"异常：如影随行-设置广告服务器失败,原因如下：%s" %e

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
        print u"异常：如影随行-点击“保存&应用”失败,原因如下：%s" %e

#描述:点击复位按钮
#输入:self
#输出:None
def reset(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        reset = driver.find_element_by_class_name('cbi-button-reset')
        reset.click()
    except (NoSuchElementException,Exception) as e:
        print u"异常：如影随行-点击“复位”失败,原因如下：%s" %e

#描述:获取访问网站源码中的JS代码
#输入:self
#输出:源码最后1000个字符
def get_js(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        html = driver.page_source
        str = html
        return str
    except (Exception) as e:
        print u"异常：如影随行-获取网页广告JS失败,原因如下：%s" %e

#描述:ssh获取如影随行进程是否还在
#输入:None
#输出:True-在，反之
def ssh_privoxy():
    result = ssh.ssh_cmd2("ps")
    return "privoxy" in result