#coding=utf-8


import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException,ErrorInResponseException,NoAlertPresentException
from random import choice
import string
from publicControl import public_control
#作者：孔志兵

#描述：menu函数用以进入系统-管理权页面
#输出：管理权页面的标题，方便后续判断页面是否正确跳转到系统-管理权页面
def menu(self):
    public_control.menu(self,u'系统',u'管理权')
    '''
    driver = self.driver
    try :
        element = driver.find_element_by_link_text(u'系统')
        ActionChains(driver).move_to_element(element).perform()
        driver.find_element_by_link_text(u'管理权').click()
        return driver.title
    except (NoSuchElementException,Exception) as e :
        print  u"点击导航中系统-管理权页面跳转失败,失败原因如下：%s" %e
    '''


#描述：set_pwd函数用以设置修改密码和确认密码
def set_pwd(self,password,password1):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        #修改密码
        driver.find_element_by_id("cbid.system._pass.pw1").clear()
        driver.find_element_by_id("cbid.system._pass.pw1").send_keys(password)
        #修改确认密码
        driver.find_element_by_id("cbid.system._pass.pw2").clear()
        driver.find_element_by_id("cbid.system._pass.pw2").send_keys(password1)
        return password,password1
    except (NoSuchElementException,Exception) as e :
        print u'设置密码和确认密码失败原因如下：%s' %e

#描述：get_alert实现页面弹出的警告框
#输出：警告框
def get_alert(self):
    driver = self.driver
    try:
        alert = driver.switch_to_alert()
        return alert
    except (NoAlertPresentException,Exception) as e:
        print u'无错误信息提示，详情如下:%s' %e

#描述：实现获取页面弹出警告框中的信息
#输出：提示信息
def get_aler_info(alert):
    try:
        info = alert.text
        alert.accept()
        return info
    except Exception as e:
        alert.accept()
        print u'获取提示信息失败，详情如下：%s' %e


#描述：submit函数实现修改密码的提交动作
def submit(self):
    driver = self.driver
    try:
        driver.find_element_by_class_name("cbi-button-apply").click()
    except (ErrorInResponseException ,Exception) as e:
        print u'提交失败的原因如下：%s' %e

#描述：get_errorbox得到页面的提示信息
#输出：提示信息盒
def get_errorbox(self):
    driver = self.driver
    try:
        errorbox = driver.find_element_by_class_name('errorbox')
        return errorbox
    except (NoAlertPresentException,Exception) as e:
        print u'无错误信息提示，详情如下:%s' %e

#描述：get_errof_info实现页面提示信息的内容
#输出：提示信息
def get_errof_info(errorbox):
    try:
        info = errorbox.text
        return info
    except Exception as e:
        print u'获取提示信息失败，详情如下：%s' %e


#描述：get_randomNum获取某长度的随机数
#输入：该随机数的长度
#输出：length长度的随机数
def get_randomNum(length):
    return ''.join(choice(string.ascii_letters+string.digits) for i in range(length))



__author__ = 'kzb'