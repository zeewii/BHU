#coding=utf-8


from connect import ssh
import linecache
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from publicControl import public_control
#作者：孔志兵
#描述：该模块实现了从页面获取版本号，从后台获取版本号，用于以后判断版本号是否显示正确，便于以后在线升级进行版本号判断


#描述：menu函数用以进入状态-总览页面
#输出：总览页面的标题，方便后续判断页面是否正确跳转到状态-总览页面
def menu(self):
    public_control.menu(self,u'状态',u'总览')
    '''
    driver = self.driver
    try :
        element = driver.find_element_by_link_text(u'状态')
        ActionChains(driver).move_to_element(element).perform()
        driver.find_element_by_link_text(u'总览').click()
        return driver.title
    except (NoSuchElementException ,Exception ) as e:
        print  u"点击导航中系统-总览页面跳转失败,跳转失败原因：%s" %e
    '''

#描述：get_web_version函数用以获取页面的版本号
#输出：页面版本号
def get_web_version(self):
    driver = self.driver
    #从页面获取软件版本version1
    try :
        version1 = driver.find_element_by_xpath("/html/body/div/p[2]").text
        return version1
    except :
        print u'未从页面上获取到版本信息'


#描述：get_houtai_version函数用以获取页面的版本号
#输出：后台显示的版本号
def get_houtai_version(self):
    #从后台获取软件版本version2
    try :
        version2 = ssh.ssh_cmd("192.168.11.1","root","BHU@100msh$%^","cat /etc/version/version")
        version2 = version2.strip()
        return version2
    except :
        print u'未从后台获取到版本信息'




__author__ = 'kzb'
