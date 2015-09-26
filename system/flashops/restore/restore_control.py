#coding=utf-8
from login import login_control
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException,NoAlertPresentException

#作者：孔志兵
#描述：该模块用以设置恢复出场设置相关信息


#描述：menu函数用以进入系统-备份/恢复页面
#输出：备份/恢复页面的标题，方便后续判断页面是否正确跳转到系统-备份/恢复页面
def menu(self):
    driver = self.driver
    try :
        element = driver.find_element_by_link_text(u'系统')
        ActionChains(driver).move_to_element(element).perform()
        #driver.find_element_by_link_text(u'备份/升级').click()
        driver.find_element_by_xpath('/html/body/header/div/div/ul/li[2]/ul/li[3]/a').click()
        return driver.title
    except (NoSuchElementException,Exception) as e:
        print  u"点击导航中系统-备份/升级页面跳转失败,失败原因如下：%s" %e


#描述：set_restore函数用以点击恢复出场设置按钮
def set_restore(self):
    driver = self.driver
    try:
        driver.find_element_by_class_name('cbi-button-reset').click()
    except (NoSuchElementException,Exception) as e:
        print  u"点击导航中系统-备份/恢复页面跳转失败,失败原因如下：%s" %e


#描述： get_alert函数用以判断是否有确认恢复出场设置提示
#输出：警告框
def get_alert(self):
    driver =self.driver
    try:
        alert = driver.switch_to_alert()
        return alert
    except (NoAlertPresentException ,Exception) as e:
        print u'没有弹警告框：%s' %e


# 描述：get_alert_info函数用以判断提示恢复出场设置信息是否正确
#输出：警告框中的提示信息
def get_alert_info(alert):
    try :
        return  alert.text
    except (SyntaxError ,Exception) as e:
        print u'未获取到警告框中的信息，原因如下：%s' %e


__author__ = 'kzb'
