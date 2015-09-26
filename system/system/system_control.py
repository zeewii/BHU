#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os,time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from publicControl import public_control

#作者：孔志兵
#描述：该模块实现了从页面获取默认主机名，设置主机名，保存配置等动作


#描述：menu函数用以进入系统-系统页面
#输出：系统页面的标题，方便后续判断页面是否正确跳转到系统-系统页面
def menu(self):
    #public_control.menu(self,u'系统',u'系统')

    driver = self.driver
    try :
        element = driver.find_element_by_link_text(u'系统')
        ActionChains(driver).move_to_element(element).perform()
        driver.find_element_by_xpath(u'/html/body/header/div/div/ul/li[2]/ul/li[1]/a').click()
        return driver.title
    except (NoSuchElementException,Exception) as e  :
        print  u"点击导航中系统-系统页面跳转失败,失败原因如下：%s" %e



#描述：get_hostname函数用以i获取页面默认的主机名，以便后续判断主机名是否和需求相同，判断默认主机没是否生效
#输出：页面默认主机名
def get_hostname(self):
    driver = self.driver
    try :
        hostname = driver.find_element_by_id('cbid.system.cfg02e48a.hostname').get_attribute('value')
        return hostname
    except :
        print u'未从页面获取到主机名'


#描述：set_hostname函数用以设置主机名
def set_hostname(self,hostname):
    driver = self.driver
    try:
        driver.find_element_by_id('cbid.system.cfg02e48a.hostname').clear()
        driver.find_element_by_id('cbid.system.cfg02e48a.hostname').send_keys(hostname)
    except (NoSuchElementException,Exception) as e :
        print  u"设置主机名失败,失败原因如下：%s" %e


#描述：get_time_button函数实现查找并点击同步浏览器时间按钮
def get_time_button(self):
    driver = self.driver
    elements = driver.find_elements_by_tag_name('input')
    try:
        for element in elements:
            if element.get_attribute('value')==u'同步浏览器时间':
                element.click()
    except Exception as e:
        print u'点击同步浏览器时间失败，具体原因如下：%s' %e


#描述：get_local_time函数实现获取页面上本地时间
#输出：页面上显示的本地时间local_time
def get_local_time(self):
    driver = self.driver
    try:
        local_time = driver.find_element_by_id("_systime-clock-status").text
        return local_time
    except (NoSuchElementException,Exception) as e :
        print u'未获取到本地时间，具体原因如下：%s' %e


#描述：get_zone_time(self)函数用以实现获取时区列表
def get_zone_time(self):
    driver = self.driver
    element = driver.find_element_by_id('cbid.system.cfg02e48a.zonename')


#描述：set_zone_time(self)函数用以设置某一时区列表
#输入：某一时区的id
def set_zone_time(self,zoneId):
    driver = self.driver
    element = driver.find_element_by_id('cbid.system.cfg02e48a.zonename')
    element.find_element_by_id(zoneId).click()


#描述：get_pc_time函数用以获取本地电脑上的时间
def get_pc_time(self):
    try:
        pc_time = time.ctime()
        return pc_time
    except Exception as e:
        print u'获取电脑上的时间失败，详情如下：%s' %e


#描述：submit函数用以保存配置
def submit(self):
    driver = self.driver
    try:
        #driver.find_element_by_class_name('cbi-button-apply').click()
        driver.find_element_by_name('cbi.apply').click()
    except (NoSuchElementException,Exception) as e :
        print  u"保存配置失败,失败原因如下：%s" %e


#描述：ping函数用以ping 主机名，来判断主机没是否生效
#输出：ping主机名的结果
def ping(hostname):
    public_control.get_ping(hostname)
    '''
    str2= 'ping %s -c 3' %hostname
    try:
        ping = os.system(str2)
        return ping
    except:
        print u'调用系统命令失败'
    '''

#描述：get_errorbox函数用以获取主机名填写错误时的提示信息定位
def get_errorbox(self):
    driver = self.driver
    element = driver.find_element_by_xpath('/html/body/div/form/div[2]/fieldset/fieldset/div[4]/ul/li')
    return element

#描述： get_alert函数用以获取页面的弹框
#输出：警告框
def get_alert(self):
    driver =self.driver
    try:
        alert = driver.switch_to_alert()
        return alert
    except (NoAlertPresentException ,Exception) as e:
        print u'没有弹警告框：%s' %e


# 描述：get_alert_info函数用以获取页面弹框中的文字信息
#输出：警告框中的提示信息
def get_alert_info(alert):
    try :
        return alert.text
    except (SyntaxError ,Exception) as e:
        print u'未获取到警告框中的信息，原因如下：%s' %e
    alert.accept()





__author__ = 'kzb'
