#coding=utf-8


import time
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from publicControl import public_control

#作者：孔志兵

#描述：menu函数用以进入系统-重启页面
#输出：重启页面的标题，方便后续判断页面是否正确跳转到系统-重启页面
def menu(self):
    public_control.menu(self,u'系统',u'重启')
    '''
    driver = self.driver
    try :
        element = driver.find_element_by_link_text(u'系统')
        ActionChains(driver).move_to_element(element).perform()
        driver.find_element_by_link_text(u'重启').click()
        return driver.title
    except (NoSuchElementException,Exception) as e :
        print  u"点击导航中系统-重启页面跳转失败,失败原因如下：%s" %e
    '''

#描述：实现页面重启动作
def reboot(self):
    driver = self.driver
    try:
        driver.find_element_by_link_text(u'执行重启').click()
    except (NoSuchElementException,Exception) as e :
        print  u"重启失败,失败原因如下：%s" %e



__author__ = 'kzb'