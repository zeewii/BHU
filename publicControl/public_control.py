#coding:utf-8
#描述：基本控制层模块，作为公共模块存在，存放公共函数
#作者：尹霞
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import uuid,os,commands

#描述:进入系统二级菜单
#输入:self
#输出:None
def menu(self,link1,link2):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        first = driver.find_element_by_link_text(link1)
        ActionChains(driver).move_to_element(first).perform()
        driver.find_element_by_link_text(link2).click()
    except (NoSuchElementException,Exception) as e:
        print u"页面跳转到%s-%s失败,原因如下：%s" %link1,link2,e

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
        print u"点击“保存&应用”失败,原因如下：%s" %str(e)

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
        print u"点击“复位”失败,原因如下：%s" %str(e)

#描述:获取本地mac地址
#输入:
#输出:mac-字符串类型，本地mac
def get_localmac():
    try:
        tmp = uuid.UUID(int=uuid.getnode()).hex[-12:]
        mac = ":".join([tmp[e:e+2] for e in range(0,11,2)])
        return mac
    except Exception,e:
        print u"获取本机mac地址失败。原因如下：%s"%e

#描述:ping
#输入:str-ip地址或域名
#输出:ping结果1-真，反之
def get_ping(str):

    try:
        ping = "ping %s -c 4"%str
        result = os.system(ping)
        return result
    except Exception,e:
        print u"ping命令执行失败。原因如下：%s"%e

#描述：Client端在终端输入命令,命令结果返回给函数
#输入：self,cmd-client在终端输入的命令
#输出：output-在终端显示的结果
def client_cmd(cmd):
    try:
        #Client端在终端输入命令,命令结果返回给函数
        status,output = commands.getstatusoutput(cmd)
        return output
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"Client端在终端输入命令失败，原因如下：\n%s"%e

