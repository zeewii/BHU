#coding:utf-8
#描述：主要编写网络-网络诊断的控制层模块
#作者：张均

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time, re,sys
from publicControl import public_control
reload(sys)
sys.setdefaultencoding('utf-8') #将系统unicode的编码方式修改为utf-8格式,

#描述:进入网络诊断页面
#输入:self
#输出:跳转失败时输出错误信息
def diag_menu(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        public_control.menu(self,u"网络",u"网络诊断")
    except (NoSuchElementException,Exception) as e:
        print u"网络诊断页面跳转失败,原因如下：%s" %str(e)

#描述:在ping输入框输入主机名
#输入:self,host  host为需要ping的主机名或IP地址
#输出:输入框定位失败时输出错误信息
def set_ping(self,host):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_name("ping").clear()
        driver.find_element_by_name("ping").send_keys(host)
    except (NoSuchElementException,Exception) as e:
        print u"ping输入框定位失败,原因如下：%s" %str(e)

#描述:点击ping按钮并检查是否有结果显示的元素
#输入:self
#输出:检查页面中如果含有结果显示的元素则说明执行成功，否则为失败并打印详细错误提示
def ping_run(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_xpath("/html/body/div/form/div/fieldset/div[1]/input[2]").click()
        time.sleep(20)  #ping不通时命令执行时间会变长，此处需预留足够时间
    except (NoSuchElementException,Exception) as e:
        print u"ping运行按钮定位失败,原因如下：%s" %str(e)


#描述:在traceroute输入框输入主机名
#输入:self,host   host输入需要填写的主机地址或IP
#输出:输入框定位失败时输出错误信息
def set_tracert(self,host):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_name("traceroute").clear()
        driver.find_element_by_name("traceroute").send_keys(host)
    except (NoSuchElementException,Exception) as e:
        print u"traceroute输入框定位失败,原因如下：%s" %str(e)

#描述:点击traceroute按钮并检查是否有结果显示的元素
#输入:self
#输出:检查页面中如果含有结果显示的元素则说明执行成功，否则为失败并打印详细错误提示
def tracert_run(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_xpath("/html/body/div/form/div/fieldset/div[2]/input[2]").click()
        time.sleep(35)  #traceroute时间较长，此处等待时间不能改短
    except (NoSuchElementException,Exception) as e:
        print u"traceroute运行按钮定位失败,原因如下：%s" %str(e)

#描述:在nslookup输入框输入主机名
#输入:self,host   host为需要输入的主机地址或IP
#输出:输入框定位失败时输出错误信息
def set_nslookup(self,host):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_name("nslookup").clear()
        driver.find_element_by_name("nslookup").send_keys(host)
    except (NoSuchElementException,Exception) as e:
        print u"nslookup输入框定位失败,原因如下：%s" %str(e)

#描述:点击nslookup按钮并检查是否有结果显示的元素
#输入:self
#输出:检查页面中如果含有结果显示的元素则说明执行成功，否则为失败并打印详细错误提示
def nslookup_run(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_xpath("/html/body/div/form/div/fieldset/div[3]/input[2]").click()
        time.sleep(35)
    except (NoSuchElementException,Exception) as e:
        print u"nslookup运行按钮定位失败,原因如下：%s" %str(e)

 #描述:错误结果检查
#输入:self
#输出:检查网络诊断中执行结果是否含有bad address字符，如果有，则说明错误结果和提示正常
def bad_result(self):
    driver = self.driver
    driver.implicitly_wait(10)
    result = driver.find_element_by_id("diag-rc-output").text
    if "bad address" in result:     #多个条件放一起判断不太稳定，所以分开判断
        print u"ping/traceroute使用错误地址解析时，结果与期望一致"
    elif  "can't resolve" in result:
        print u"nslookup使用错误地址解析时，结果与期望一致"
    else:
        print result
        raise ValueError(u"使用错误地址解析时，结果与期望不一致")

 #描述:正确结果检查
#输入:self
#输出:检查网络诊断中执行结果是否含有bad address和can't resolve字符，如果有，则说明输出结果有误
def pass_result(self):
    driver = self.driver
    driver.implicitly_wait(10)
    result = driver.find_element_by_id("diag-rc-output").text
    if "bad address" in result:     #多个条件放一起判断不太稳定，所以分开判断
        raise ValueError(u"ping/traceroute命令执行结果与期望不一致")
    elif "can't resolve" in result:
        raise ValueError(u"nslookup命令执行结果与期望不一致")
    else:
        print u"网络诊断命令执行结果检查正常"

 #描述:输出内容位置定位检查
#输入:self
#输出:检查结果输出的元素是否存在，如果不存在则输出错误提示
def diag_output(self):
    driver = self.driver
    driver.implicitly_wait(10)
    output = driver.find_element_by_id("diag-rc-output").text
    if output:
        print u"命令执行成功，结果输出框定位成功"
    else:
        raise ValueError(u"命令执行失败，结果输出框定位失败")



__author__ = 'Administrator'
