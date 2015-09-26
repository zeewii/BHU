#coding=utf-8

import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ErrorInResponseException,NoAlertPresentException
from publicControl import public_control

#作者：孔志兵
#描述：该模块实现Qos-ip模块上面的各个按钮，输入框的动作



#描述：menu函数用以进入网络-Qos-ip权页面
#输出：管理权页面的标题，方便后续判断页面是否正确跳转到系统-管理权页面
def menu(self):
    public_control.menu(self,u'网络',u'Qos-ip')
    '''
    driver = self.driver
    try :
        element = driver.find_element_by_link_text(u'网络')
        ActionChains(driver).move_to_element(element).perform()
        driver.find_element_by_link_text(u'Qos-ip').click()
        return driver.title
    except (NoSuchElementException,Exception) as e:
        print  u"点击导航中'网络-Qos-ip'页面跳转失败,失败原因如下：%s" %e
    '''

#描述：qos_button函数实现定位QOS-IP启用按钮
#输出：启用按钮状态，1-开，0-关，以便后续判断启用按钮默认状态
def get_button(self):
    driver = self.driver
    try:
        element = driver.find_element_by_id('cbid.qos-ip.lan.enabled')
        status = element.is_selected()
        return status
    except (NoSuchElementException,Exception) as e:
        print u'没有定位到启用按钮，具体原因如下：%s' %e

#描述:设置页面qos_ip开关的状态
#输入:self
#输出:None
def set_qos_ip_enable(self):
    driver = self.driver
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_id('cbid.qos-ip.lan.enabled').click()
    except (ErrorInResponseException,Exception) as e:
        print u"qos_ip开关设置失败,原因如下：%s" %str(e)


#描述：add函数实现点击添加动作
def add(self):
    driver = self.driver
    try:
        driver.find_element_by_class_name('cbi-button-add').click()
    except (NoSuchElementException,Exception) as e:
        print u'未找到添加按钮，具体原因如下：%s' %e
    except (ErrorInResponseException,Exception) as e:
        print u'点击添加按钮没有响应，具体原因如下：%s' %e


#描述：qos_ip函数实现输入起始地址和结束地址
#输入：
#startIP----起始地址
#endIP------结束IP
#i--------表示哪一条规则,从1开始
def set_ip(self,startIP,endIP,i) :
    driver = self.driver
    j = i+2
    xpath1 = '/html/body/div/form/div[2]/fieldset[2]/div[2]/table/tbody/tr[%d]/td[1]/div[1]/input' %j
    xpath2 = '/html/body/div/form/div[2]/fieldset[2]/div[2]/table/tbody/tr[%d]/td[2]/div[1]/input' %j
    #输入起始ip
    driver.find_element_by_xpath(xpath1).clear()
    driver.find_element_by_xpath(xpath1).send_keys(startIP)
    #输入结束IP
    driver.find_element_by_xpath(xpath2).clear()
    driver.find_element_by_xpath(xpath2).send_keys(endIP)


#qos_speed函数实现输入上传和下载速度
#输入：
#dlSpeed----下载速度
#upSpeed----上传速度
#i--------表示哪一条规则，从1开始
def set_speed(self,dlSpeed,upSpeed,i):
    driver = self.driver
    j = i+2
    xpath1 = '/html/body/div/form/div[2]/fieldset[2]/div[2]/table/tbody/tr[%d]/td[3]/div[1]/input' %j
    xpath2 = '/html/body/div/form/div[2]/fieldset[2]/div[2]/table/tbody/tr[%d]/td[4]/div[1]/input' %j
    #输入下载速度
    driver.find_element_by_xpath(xpath1).clear()
    driver.find_element_by_xpath(xpath1).send_keys(dlSpeed)
    #输入上传速度
    driver.find_element_by_xpath(xpath2).clear()
    driver.find_element_by_xpath(xpath2).send_keys(upSpeed)


#描述：qos_save函数实现保存配置
def submit(self):
    driver = self.driver
    try:
        driver.find_element_by_name("cbi.apply").click()
    except (NoSuchElementException,Exception) as e:
        print u'未找到保存按钮，具体原因如下：%s' %e
    except (ErrorInResponseException,Exception) as e:
        print u'点击保存按钮没有响应，具体原因如下：%s' %e


#描述：delete函数实现删除按钮操作
#i--------表示哪一条规则，从1开始
def delete(self,i):
    driver = self.driver
    i = i+2
    xpath = '/html/body/div/form/div[2]/fieldset[2]/div[2]/table/tbody/tr[%d]/td[5]/input' %i
    try:
        driver.find_element_by_xpath(xpath).click()
    except (NoSuchElementException,Exception) as e:
        print u'未找到删除按钮，具体原因如下：%s' %e
    except (ErrorInResponseException,Exception) as e:
        print u'点击删除按钮没有响应，具体原因如下：%s' %e


#描述：

def delete_multi(self):
    driver = self.driver
    elements = driver.find_elements_by_class_name('cbi-button-remove')
    length = len(elements)
    for i in range(0,length):
        elements = driver.find_elements_by_class_name('cbi-button-remove')
        elements[-1].click()
        #driver.execute('$(arguments[0]).click()',element)




#描述：ip_plit函数实现分割IP地址，获取IP地址的最后一位，以便后续做IP地址容错性判断
#输入：输入的IP地址
#输出：IP地址的最后一位
def get_ip(ip):
    IP = ip.split(".")
    return IP[3]


#描述：get_alert实现页面弹出的警告框
#输出：警告框
def get_alert(self):
    driver = self.driver
    try:
        alert = driver.switch_to_alert()
        return alert
    except (NoAlertPresentException,Exception) as e:
        print u'没弹出警告框，详情如下:%s' %e

#描述：实现获取页面弹出警告框中的信息
#输出：提示信息
def get_alet_info(alert):
    try:
        info = alert.text()
        return info
    except Exception as e:
        print u'获取提示信息失败，详情如下：%s' %e


#描述：onlineSpeed使用中国电信网络测速：http://netreport.sh.189.cn/speed/main.html
def onlineSpeed(self):
    driver = self.driver
    driver.get('http://netreport.sh.189.cn/speed/main.html')
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/table/tbody/tr[1]/td[2]/div/a/img').click()
    #使用有线客户端进行测试
    driver.find_element_by_xpath('html/body/div[4]/table/tbody/tr/td/div/div[3]').click()
    driver.find_element_by_xpath('html/body/div[4]/table/tbody/tr/td/div/div[1]').click()
    time.sleep(16)

#描述：get_dlSpeed_online函数实现获取在线测速功能测下载的速度
def get_dlSpeed_online(self):
    driver = self.driver
    onlineSpeed(self)
    #在线测速单位是KB
    #driver.switch_to_frame("iframePageDiv")
    driver.switch_to_frame("myWorkSpace")
    element  = driver.find_element_by_xpath(".//*[@id='avgSpeed']")
    driver.execute_script('$(arguments[0]).click()',element)
    #element.click()
    time.sleep(2)
    #dlSpeed = driver.execute_script('$(arguments[0]).text',element)
    dlSpeed = element.text
    if dlSpeed =='':
        get_dlSpeed_online(self)
    else :
        #将在线测速的单位换算成kb,与软件的单位一致，以便计算
        dlSpeed= int(dlSpeed)*8
        #print dlSpeed
        return dlSpeed




#用在线测速功能测上传速度
def get_upSpeed_online(self):
    driver = self.driver
    onlineSpeed(self)
    #driver.switch_to_frame("iframePageDiv")
    driver.switch_to_frame("myWorkSpace")

    #点击测试上传速率
    bb=driver.find_element_by_xpath(".//*[@id='testUpload']")
    driver.execute_script('$(arguments[0]).click()',bb)

    #重新测试速率，获取上传速率
    bb = driver.find_element_by_xpath(".//*[@id='btn-again-id']")
    driver.execute_script('$(arguments[0]).click()',bb)
    time.sleep(2)
    #智能等待测速完毕
    time.sleep(20)

    #在线测速单位是KB
    element = driver.find_element_by_xpath(".//*[@id='upavgSpeed']")
    driver.execute_script('$(arguments[0]).click()',element)
    upSpeed = element.text
    if upSpeed =='':
        get_upSpeed_online(self)
    else :
        #将在线测速的单位换算成kb,与软件的单位一致，以便计算
        upSpeed= int(upSpeed)*8
        #print upSpeed
        return upSpeed



__author__ = 'kzb'






