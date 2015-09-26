#coding=utf-8
#描述：该模块为测试dhcpdns模块
#作者：曾祥卫

import unittest
from selenium import webdriver
from network.dhcpDns import dhcpdns_business


class TestDhcpdns(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        #将浏览器最大化
        self.driver.maximize_window()
        #使用默认ip登录DHCP/DNS页面
        dhcpdns_business.goin_default_dhcpdns(self)


    def test_160_valid_domain(self):
        u"""有效域名绑定测试"""
        result = dhcpdns_business.step_100msh0160(self)
        print result
        assert result ==1,u"测试有效域名绑定fail"
        print u"测试有效域名绑定pass"

    def test_161_invalid_domain(self):
        u"""无效域名绑定测试"""
        result = dhcpdns_business.step_100msh0161(self)
        print result
        assert result ==1,u"测试无效域名绑定fail"
        print u"测试无效域名绑定pass"

    def test_163_reboot(self):
        u"""域名绑定后重启测试"""
        result = dhcpdns_business.step_100msh0163(self)
        print result
        assert result ==1,u"域名绑定后重启测试fail"
        print u"域名绑定后重启测试pass"

    def test_164_max_list(self):
        u"""域名绑定最大限制测试"""
        result = dhcpdns_business.step_100msh0164(self)
        print result
        assert result ==1,u"域名绑定最大限制测试fail"
        print u"域名绑定最大限制测试pass"

    def test_165_samedomain_differentip(self):
        u"""域名相同IP不同时绑定测试"""
        result = dhcpdns_business.step_100msh0165(self)
        print result
        assert result ==1,u"域名相同IP不同时绑定测试fail"
        print u"域名相同IP不同时绑定测试pass"

    def test_166_differentdomain_sameip(self):
        u"""IP相同域名不同时绑定测试"""
        result = dhcpdns_business.step_100msh0166(self)
        print result
        assert result ==1,u"IP相同域名不同时绑定测试fail"
        print u"IP相同域名不同时绑定测试pass"

    def test_167_none_www(self):
        u"""域名绑定时不绑定网络名"""
        result = dhcpdns_business.step_100msh0167(self)
        print result
        assert result ==[1,1],u"域名绑定时不绑定网络名测试fail"
        print u"域名绑定时不绑定网络名测试pass"

    def test_168_only_host(self):
        u"""域名绑定时只绑定主机名"""
        result = dhcpdns_business.step_100msh0168(self)
        print result
        assert result == 1,u"域名绑定时只绑定主机名测试fail"
        print u"域名绑定时只绑定主机名测试pass"

    def test_169_add_static_leases(self):
        u"""DHCP静态地址分配"""
        result = dhcpdns_business.step_100msh0169(self)
        print result
        assert result == 1,u"DHCP静态地址分配测试fail"
        print u"DHCP静态地址分配测试pass"


    #退出清理工作
    def tearDown(self):
        self.driver.quit()


if __name__=='__main__':
    unittest.main()

__author__ = 'zeng'

