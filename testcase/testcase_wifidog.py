#coding:utf-8

#描述:门户认证测试用例模块
#作者：尹霞

import unittest
from selenium import webdriver
import time
from login import login_business
from network.wifidog import general_control,terlist_control,weblist_control,network_control,wifidog_business

class TestWifidog(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        login_business.default_login(self)
        time.sleep(3)
        general_control.wifidog_menu(self)

    def test_166_switch(self):
        u"""默认启用认证"""
        status = general_control.get_wifidog_enable(self)
        assert status==1,u"门户认证默认状态不是打开状态"

    def test_167_switch(self):
        u"""开启认证功能的有效性"""
        result = network_control.rand_redirect(self)
        assert result,u"开启认证功能的有效性失败"

    def test_168_switch(self):
        u"""关闭认证功能的有效性"""
        result = wifidog_business.edit_wifidog(self,0)
        assert result==0,"关闭认证功能的有效性失败，wifidog进程仍存在"
        print u"关闭认证功能成功-两分钟内没有wifidog进程"

    def test_169_switch(self):
        u"""再次开启认证功能的有效性"""
        result1 = wifidog_business.edit_wifidog(self,1)
        assert result1,u"wifidog进程没起来，无法进行下一步"
        result2 = network_control.rand_redirect(self)
        assert result2,u"再次开启认证功能的有效性失败"

    def test_182_datewayid(self):
        u"""默认网关id上报功能验证"""
        default_gwid = "44060430603381"
        gwid = general_control.get_gatewayId(self)
        general_control.apply(self)
        time.sleep(40)
        data = wifidog_business.redirest_network(self)
        assert (default_gwid in data)and(default_gwid in gwid),u"默认网关ID上报功能验证失败"

    def test_183_datewayid(self):
        u"""修改后网关ID上报功能验证"""
        gwid = "100msh2323"
        wifidog_business.edit_gatewayid(self,gwid)
        data = wifidog_business.redirest_network(self)
        assert gwid in data,u"修改后网关ID:%s上报功能验证失败"%gwid

    def test_184_datewayid(self):
        u"""网关ID不存在或被删除"""
        gwid = "as12121ds32"
        wifidog_business.edit_gatewayid(self,gwid)
        data = wifidog_business.redirest_network(self)
        assert gwid in data,u"修改后不存在的网关ID上报功能验证失败"

    def test_189_hostname(self):
        u"""默认服务器地址"""
        default_hostname = "wifi.100msh.com"
        data = general_control.get_wifidog_hostname(self)
        general_control.apply(self)
        time.sleep(30)
        url = network_control.rand_redirect_get_url(self)
        assert default_hostname in (data and  url),u"默认认证服务器不是%s"%default_hostname

    def test_190_hostname(self):
        u"""修改为其它正确的地址有效性"""
        hostname = "test102.100msh.com"
        wifidog_business.edit_hostname(self,hostname)
        url = network_control.rand_redirect_get_url(self)
        data = wifidog_business.redirest_network(self)
        assert hostname in url,u"修改为其它正确的地址：%s，有效性认证失败"%hostname

    def test_191_hostname(self):
        u"""修改为错误的地址后用户上网功能检查"""
        hostname = "sbnejh.kwieh.com"
        wifidog_business.edit_hostname(self,hostname)
        #time.sleep(300)
        result = network_control.rand_network(self)
        assert result,u"修改为错误的地址后：%s，用户上网功能检查失败"%hostname

    def test_192_hostname(self):
        u"""修改为空的地址有效性"""
        hostname = None
        default_hostname = "wifi.100msh.com"
        wifidog_business.edit_hostname(self,hostname)
        url = network_control.rand_redirect_get_url(self)
        wifidog_business.redirest_network(self)
        assert default_hostname in url,u"修改为空地址有效性认证失败，主机名不是默认的"%hostname

    def test_192_xx_default_general(self):
        u"""还原一般设置的有效性"""
        wifidog_business.default_general(self)
        print u"一般设置恢复默认值"

    def test_196_terlist(self):
        u"""添加单个mac有效检查"""
        result= wifidog_business.edit_one_terlist(self)
        assert result,u"添加单个mac有效检查失败"

    def test_197_terlist(self):
        u"""添加多个mac有效检查"""
        maclist = ["12:34:56:78:54:23","12:34:56:78:54:24","12:34:56:78:54:25"]
        data = wifidog_business.edit_terlist(self,maclist,3)
        for i in maclist:
            assert i.upper() in data,u"添加多个地址时没有加入iptables里"

    def test_198_terlist(self):
        u"""MAC格式填写容错性"""
        maclist=["12-34-56-78-54-23","12:34:56:78:54:23:","12:34:56:78:54:2@",u"你好"]
        for i in maclist:
            data = wifidog_business.edit_errorlist(self,i)
            assert data=="一些项目的值无效，无法保存！",u"输入mac地址为：%s,弹出框信息错误"%i

    def test_200_terlist(self):
        u"""重启设备有效性"""
        result= wifidog_business.edit_one_terlist(self)
        wifidog_business.reboot(self)
        result2 = network_control.rand_network(self)
        assert result2,u"添加单个mac（本机mac）后重启设备有效检查失败"
        terlist_control.remove_button(self,0)
        terlist_control.apply(self)
        time.sleep(30)

    def test_200_xx_default_terlist(self):
        wifidog_business.remove_terlist(self)
        print u"终端192白名单恢复默认值"

    def test_201_weblist(self):
        u"""默认设置下有效性性检查"""
        weblist_control.tabmenu_weblist(self)
        weblist = weblist_control.get_weblist(self)
        for i in weblist[1:]:
            self.driver.get(i)
            time.sleep(5)
            assert (u"百米" in self.driver.title)or("404" in self.driver.title)or('nginx'in self.driver.title),\
                u"默认设置下的%s有效性性检查失败,得到的标题为%s"%(i,self.driver.title)

    def test_202_weblist(self):
        u"""添加单个IP或域名有效性检查"""
        webdics={}#存放字典，将url\title放入字典对应
        url,title = network_control.data.rand_get_network()
        webdics.setdefault(url,title)
        wifidog_business.add_weblist(self,webdics.keys())
        result = network_control.network(self,url,title)
        assert result,u"添加单个IP或域名有效性检查失败"

    def test_203_weblist(self):
        webdics={}#存放字典，将url\title放入字典对应
        u"""添加多个IP或域名有效性检查"""
        for i in range(3):
            url,title = network_control.data.rand_get_network()
            webdics.setdefault(url,title)
        wifidog_business.add_weblist(self,webdics.keys())
        for (i,j) in webdics.items():
            result = network_control.network(self,i,j)
            assert result,u"添加多个IP或域名有效性检查失败,失败网站是：%s:%s"%(i,j)

    def test_204_weblist(self):
        u"""网站白名单为空"""
        result = wifidog_business.remove_web(self)
        assert result,u"网站白名单为空有效性检查失败"

    def test_204_xx_default_weblist(self):
        u"""恢复默认的网站白名单"""
        wifidog_business.default_weblist(self)

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()

