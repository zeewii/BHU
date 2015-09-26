#coding=utf-8

#描述：DMZ基本控制层
#作者：张均

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from publicControl import public_control
import time

#描述:备份/升级配置页面菜单
#输入:self
#输出：None
def flashops_menu(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        public_control.menu(self,u"系统",u"备份/升级")
    except (NoSuchElementException,Exception) as e:
        print u"页面跳转到DMZ失败,原因如下：%s" % e

#描述:添加恢复备份配置的文件
#输入:self，bakconf，bakconf为需要上传的配置路径
#输出：错误提示和详细错误信息
def set_bakconf(self,bakconf):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_id("archive").send_keys(bakconf)
        time.sleep(2)
    except (NoSuchElementException,Exception) as e:
        print u"备份配置上传失败,原因如下：%s" % e

#描述:点击上传备份配置按钮
#输入:self
#输出：错误提示和详细错误信息
def bakconf_upload(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_name("restore").click()
    except (NoSuchElementException,Exception) as e:
        print u"上传备份按钮点击失败,原因如下：%s" % e

#描述:获取保留配置选项勾选状态
#输入:self
#输出：状态为勾选时返回1，未勾选时返回0
def get_savconf_status(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
       configbox = driver.find_element_by_id("keep")
       status = configbox.is_selected()
       return status
    except (NoSuchElementException,Exception) as e:
        print u"保留配置开关定位失败,原因如下：%s" % e

#描述:设置保留配置选项为勾选状态
#输入:self
#输出：None
def set_savconf_enable(self):
    driver = self.driver
    enable = get_savconf_status(self)
    if enable == 1:
        print u"保留配置选项为勾选状态，不需要再次勾选"
    else:
        driver.find_element_by_id("keep").click()
        print u"保留配置选项为禁用状态，已勾选为启用状态"

#描述:设置保留配置选项为未勾选状态
#输入:self
#输出：None
def set_savconf_disable(self):
    driver = self.driver
    enable = get_savconf_status(self)
    if enable == 0:
        print u"保留配置选项已经是禁用状态"
    else:
        driver.find_element_by_id("keep").click()
        print u"保留配置选项为启用状态，已勾选为禁用状态"

#描述:上传需要升级的固件
#输入:self，flash    flash为需要升级的固件路径【特别注意：路径中部分斜杆需要转义】
#输出：错误提示和详细错误信息
def flash_upload(self,flash):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_id("image").send_keys(flash)
        time.sleep(2)
    except (NoSuchElementException,Exception) as e:
        print u"固件上传失败,原因如下：%s" % e

#描述:点击刷写固件按钮
#输入:self
#输出：错误提示和详细错误信息
def flash_upgrade(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        buttons = driver.find_elements_by_class_name("cbi-input-apply")
        buttons[-1].click()
        time.sleep(10)
    except (NoSuchElementException,Exception) as e:
        print u"固件刷写按钮点击失败,原因如下：%s" % e

#描述:点击提交按钮
#输入:self
#输出：错误提示和详细错误信息
def flash_submit(self):
    driver = self.driver
    driver.implicitly_wait(30)
    try:
        driver.find_element_by_class_name("cbi-button-apply").click()
    except (NoSuchElementException,Exception) as e:
        print u"提交按钮点击失败,原因如下：%s" % e

#描述:获取固件上传错误信息
#输入:self
#输出：1.错误提示框定位失败时，会打印错误日志和详细信息
#      2.错误信息内容不符合时，会打印错误日志
def get_error(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_class_name("cbi-section-error")
    except (NoSuchElementException,Exception) as e:
        print u"错误提示框定位失败,原因如下：%s" % e
    message = driver.find_element_by_class_name("cbi-section-error").text
    message2 = u"不支持所上传的文件格式。请确认选择的文件无误。"
    if message == message2:
        print u"错误提示内容与期望一致"
    else:
        raise ValueError(u"错误提示内容与期望不一致")

#描述:获取固件刷写时的进度条
#输入:self
#输出：打印错误日志和详细信息
def get_Progress(self):
    driver = self.driver
    try:
        driver.find_element_by_id("ProgressBar")
    except (NoSuchElementException,Exception) as e:
        print u"刷写进度框定位失败,原因如下：%s" % e


#描述:点击恢复出厂值按钮
#输入:self
#输出：打印错误日志和详细信息
def set_rstdefault(self):
    public_control.reset(self)


#描述:获取警告弹窗并点击确认
#输入:self
#输出：打印错误日志和详细信息
def get_alert(self):
    driver = self.driver
    try:
        alert = driver.switch_to_alert()
        alert.accept()
    except (NoSuchElementException,Exception) as e:
        print u"警告窗处理失败，原因如下：%s" % e




__author__ = 'Administrator'
