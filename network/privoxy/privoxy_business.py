#coding:utf-8
#描述：如影随行-业务逻辑层代码
#作者：尹霞
import privoxy_control
from network.wifidog import network_control
from connect import ssh
import time

#描述：1.修改如影随行->2.点击保存->3.控制等待时间30秒，保证wifedog起来
#输入：self
#输出：None
def edit_privoxy(self,status,url):
    nowstatus = privoxy_control.get_redirect_enable(self)
    print u"当前如影随行开关状态是%s(True表示开，False表示关)，现要反置"%nowstatus
    privoxy_control.set_redirect_enable(self,status)
    privoxy_control.set_redirect_Hostname(self,url)
    privoxy_control.apply(self)
    time.sleep(30)

#描述：1.认证访问任意网页->3.访问任意网页-》4.获取并返回网页源码
#输入：self
#输出：data-网页后1000个字符的代码
def redirect_get_js(self):
    url1 = "http://www.qq.com"
    result = network_control.redirect(self,url1)
    assert result==True,u"通过访问%s网页认证不成功，无法进行下一步"%url1
    result2 = network_control.network(self,"http://www.sina.com.cn","新浪")
    assert result2==True,u"认证后网页访问失败，无法进行下一步"
    time.sleep(10)
    data = privoxy_control.get_js(self)
    return data

#描述：1.认证访问任意网页->3.访问任意网页-》4.获取并返回网页后800个字符的代码
#输入：self
#输出：data-网页后1000个字符的代码
def get_js(self):
    network_control.network(self,"http://www.sina.com.cn","新浪")
    data = privoxy_control.get_js(self)
    return data



#描述:ssh-重启路由器
#输入:None
#输出:None
def reboot():
    ssh.ssh_cmd2("reboot")
    time.sleep(60)