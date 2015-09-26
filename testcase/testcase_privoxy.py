#coding:utf-8
#描述：如影随行-用例代码
#作者：尹霞
import unittest
from selenium import webdriver
from network.privoxy import privoxy_control,privoxy_business
from login import login_business

DEFAULT = "http://chdadd.100msh.com/ad.js"

class TestPrivoxy(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        login_business.default_login(self)
        privoxy_control.privoxy_menu(self)

    def test_205_switch(self):
        u"""广告默认开启"""
        str = u"如影随行默认开关不是打开状态"
        status = privoxy_control.get_redirect_enable(self)
        assert status==1,str
        print u"广告默认开启-pass"

    def test_206_switch(self):
        u"""验证开启广告功能的有效性"""
        data = privoxy_business.redirect_get_js(self)
        assert ("gw_id" and "smac" and "rmac") in data,\
        u"广告JS代码错误，具体见JS代码：%s"%data
        print u"验证开启广告功能的有效性-成功"

    def test_207_switch(self):
        u"""验证关闭广告功能的有效性"""
        privoxy_business.edit_privoxy(self,0,DEFAULT)
        data = privoxy_business.redirect_get_js(self)
        assert ("gw_id" and "smac" and "rmac") not in data,\
        u"广告仍存在JS代码，具体见JS代码：%s"%data
        print u"验证关闭广告功能的有效性-成功"


    def test_208_switch(self):
        u"""验证再次开启广告功能的有效性"""
        privoxy_business.edit_privoxy(self,1,DEFAULT)
        data = privoxy_business.redirect_get_js(self)
        assert ("gw_id" and "smac" and "rmac") in data,\
        u"广告JS代码错误，具体见JS代码：%s"%data
        print u"验证再次开启广告功能的有效性-成功"


    def test_209_switch(self):
        u"""验证重启设备广告功能的有效性"""
        hostname = privoxy_control.get_redirect_Hostname(self)
        privoxy_business.reboot()
        data = privoxy_business.redirect_get_js(self)
        assert ("gw_id" and "smac" and "rmac" and hostname) in data,\
        u"广告JS代码错误，具体见JS代码：%s"%data
        print u"验证广告功能的有效性-成功"

    def test_210_js(self):
        u"""默认路径有效性"""
        default_url = ""
        privoxy_control.apply(self)
        time.sleep(60)
        data = privoxy_business.get_js(self)
        assert ("gw_id" and "smac" and "rmac") in data,\
        u"广告JS代码错误，具体见JS代码：%s"%data
        print u"验证广告功能的有效性-成功"

    def test_211_js(self):
        u"""修改为其他正确的广告服务器路径有效性"""
        url = "http://a755.100msh.com/ad.js"
        privoxy_business.edit_privoxy(self,1,url)
        data = privoxy_business.redirect_get_js(self)
        assert url in data,u"修改为其他正确的广告服务器路径失败，js代码如下：%s"%data
        print u"修改为其他正确的广告服务器路径有效性-成功"

    def test_212_js(self):
        u"""修改为错误的广告服务器路径有效性"""
        url = "http://queuuureiuruiruij/ad.js"
        privoxy_business.edit_privoxy(self,1,url)
        data = privoxy_business.redirect_get_js(self)
        assert url in data,u"修改为其他错误的广告服务器路径失败，js代码如下：%s"%data
        print u"修改为错误的广告服务器路径有效性-成功"

    def test_213_js(self):
        u"""修改为空的广告服务器路径有效性"""
        url = None
        default_js = privoxy_control.get_redirect_Hostname(self)
        privoxy_business.edit_privoxy(self,1,url)
        data = privoxy_business.get_js(self)
        assert default_js in data,u"修改为空的广告服务器是默认的广告服务器失败，js代码如下：%s"%data
        print u"修改为空的广告服务器路径有效性-成功"

    def test_214_default_js(self):
        u"""修改为默认配置"""
        privoxy_business.edit_privoxy(self,1,DEFAULT)

    def tearDown(self):
        self.driver.quit()