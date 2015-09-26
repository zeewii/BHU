#coding:utf-8

#描述：门户认证-网络访问控制层，包括通过认证上网和不通过认证上网
#作者：尹霞
import random,sys,time,datetime
from selenium.common.exceptions import NoSuchElementException
from connect import ssh
from data import data
reload(sys)
sys.setdefaultencoding('utf-8') #将系统unicode的编码方式修改为utf-8格式,
#描述:不需要认证访问网页-访问某个特定网页，检查标题是否正确
#输入:self,url-需要访问的网站地址，title-网站的标题
#输出:True-正常访问成功，反之
def network(self,url,title):
    driver = self.driver
    try:
        driver.get(url)
        driver.implicitly_wait(30)
        if driver.title==u"Problem loading page":
            print u"页面首次访问失败:火狐浏览器原因，现进行一次刷新"
            driver.refresh()
            driver.implicitly_wait(30)
        return title in driver.title
    except (NoSuchElementException,Exception) as e:
        print u"访问网络失败,原因如下：%s" %e

#描述:从data中随机选择的一个网页，检包含url和title
#输入:self
#输出:url和title
def rand_get_network():
    return data.rand_get_network()

#描述:正常访问网页-访问从data中随机选择的网页，检查标题是否正确，注意ubuntu浏览器是unicode编码
#输入:self
#输出:True-正常访问成功，反之
def rand_network(self):
    driver = self.driver
    try:
        url,title = rand_get_network()
        driver.get(url)
        driver.implicitly_wait(30)
        if driver.title==u"Problem loading page":
            print u"页面首次访问失败:火狐浏览器原因，现进行一次刷新"
            driver.refresh()
            driver.implicitly_wait(30)
        return title in driver.title
    except (NoSuchElementException,IOError,Exception) as e:
        print u"浏览器驱动异常或者随机选择的weblist.csv错误,原因如下：%s"%e

#描述:访问指定的网页是否跳转到门户认证
#输入:self
#输出:None
def redirect(self,url):
    driver = self.driver
    try:
        driver.get(url)
        driver.implicitly_wait(30)
        if driver.title==u"Problem loading page":
            print u"页面首次访问失败:火狐浏览器原因，现进行一次刷新"
            driver.refresh()
            driver.implicitly_wait(30)
        try:
            tmp = driver.find_element_by_link_text(u"临时上网")
            tmp.click()
        except:
            network = driver.find_element_by_class_name('connectNetwork')
            network.click()
        driver.implicitly_wait(30)
        return (u"百米" in driver.title )or( "UC" in  driver.title)
    except (NoSuchElementException,Exception) as e:
        png = "error_redirect_%s.png"%str(datetime.datetime.now())
        print u"访问网络认证失败,见error文件夹中%s，原因如下：%s" %(png,e)
        driver.get_screenshot_as_file("./data/error/"+png)

#描述:访问网页是否跳转到门户认证
#输入:self
#输出:True-成功，False-失败
def rand_redirect(self):
    driver = self.driver
    try:
        url,title = rand_get_network()
        driver.get(url)
        driver.implicitly_wait(30)
        if driver.title==u"Problem loading page":
            print u"页面首次访问失败:火狐浏览器原因，现进行一次刷新"
            driver.refresh()
            driver.implicitly_wait(30)
        try:
            tmp = driver.find_element_by_link_text(u"临时上网")
            tmp.click()
        except:
            network = driver.find_element_by_class_name('connectNetwork')
            network.click()
            driver.implicitly_wait(30)
        return (u"百米" in driver.title )or( "UC" in  driver.title)
    except (NoSuchElementException,IOError,Exception) as e:
        png = "error_rand_redirect_%s.png"%str(datetime.datetime.now())
        print u"访问网络认证失败,见error文件夹中%s，原因如下：%s" %(png,e)

        driver.get_screenshot_as_file("./data/error/"+png)

#描述:访问网页是否跳转到门户认证-获取认证url
#输入:self
#输出:url
def rand_redirect_get_url(self):
    driver = self.driver
    try:
        url,title = rand_get_network()
        driver.get(url)
        driver.implicitly_wait(30)
        if driver.title==u"Problem loading page":
            print u"页面首次访问失败:火狐浏览器原因，现进行一次刷新"
            driver.refresh()
            driver.implicitly_wait(30)
        url = driver.current_url
        return url
    except (NoSuchElementException,IOError,Exception) as e:
        print u"访问网络认证失败,原因如下：%s" %e


#描述:ssh获取wifidog进程，并判断是否存在
#输入:None
#输出:True-存在，反之
def ssh_wifidog():
    try:
        i =0
        while(i<5):
            result = ssh.ssh_cmd2("ps")
            if "wifidog" in result:
                return True
            time.sleep(20)
            i+=1
        return False
    except Exception,e:
        print u"从ssh获取wifidog进程信息失败，原因如下：%s"%e

#描述:ssh获取iptables中outgoing表信息
#输入:None
#输出:outgoing链信息
def ssh_get_outgoing():
    try:
        outgoing = ssh.ssh_cmd2("iptables -t mangle -L WiFiDog_br-lan_Outgoing")
        return outgoing
    except Exception,e:
        print u"从ssh获取iptables表中WiFiDog_br-lan_Outgoing信息失败。原因如下：%s"%e