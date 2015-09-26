#coding=utf-8
#描述：该模块为测试wan模块
#作者：曾祥卫

import unittest
from selenium import webdriver
from network.interface.wan import wan_business

class TestWan(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        #将浏览器最大化
        self.driver.maximize_window()
        #使用默认ip登录wan页面
        wan_business.goin_default_wan(self)
        self.driver.implicitly_wait(10)

    def test_069_staticip(self):
        u"""WAN设置为静态IP地址"""
        result = wan_business.step_100msh0069(self)
        print result
        #如果2个都为True则通过，否则不通过
        assert result ==[True,True],u"测试WAN为静态IP地址fail"
        print u"测试WAN为静态IP地址pass"

    def test_070_staticip_broadcast(self):
        u"""wan广播地址配置有效性测试"""
        result = wan_business.step_100msh0070(self)
        print result
        #如果2次都为1则通过，否则不通过
        assert result == [1,1],u"测试wan广播地址配置有效性fail"
        print u"测试wan广播地址配置有效性pass"

    def test_071_staticip_dns(self):
        u"""自定义DNS的有效性测试"""
        result = wan_business.step_100msh0071(self)
        print result
        #如果2次都为True则通过，否则不通过
        assert result == [True,True],u"测试自定义DNS的有效性fail"
        print u"测试自定义DNS的有效性pass"

    def test_072_staticip_mac_clone(self):
        u"""wan为静态ip时MAC地址克隆"""
        result = wan_business.step_100msh0072(self)
        print result
        #如果结果为1则通过，否则不通过
        assert result == 1,u"测试wan为静态ip时MAC地址克隆fail"
        print u"测试wan为静态ip时MAC地址克隆pass"

    def test_073_staticip_mtu(self):
        u"""wan为静态ip时MTU设置检查"""
        result1 = wan_business.step_100msh0073_1(self)
        result2 = wan_business.step_100msh0073_2(self)
        print result1,result2
        #如果结果为1则通过，否则不通过
        assert result1 == [1,1,1] and result2 == [1,1],u"测试wan为静态ip时MTU设置检查fail"
        print u"测试wan为静态ip时MTU设置检查pass"

    def test_074_dhcp(self):
        u"""WAN口DHCP获取上网IP"""
        result = wan_business.step_100msh0074(self)
        print result
        #如果2个都为True则通过，否则不通过
        assert result ==[True,True],u"测试WAN为dhcpfail"
        print u"测试WAN为dchppass"

    def test_075_dhcp_reboot(self):
        u"""重启/重新上电后上网测试"""
        result = wan_business.step_100msh0075(self)
        print result
        #如果结果为0则通过，否则不通过
        assert result == 0,u"测试WAN为dhcp后重启/重新上电后上网fail"
        print u"测试WAN为dchp后重启/重新上电后上网pass"

    def test_076_wan_disconnect_connect(self):
        u"""WAN口反复关闭后重新获取IP测试"""
        result = wan_business.step_100msh0076(self)
        print result
        #如果结果为0则通过，否则不通过
        assert result == 0,u"测试WAN口反复关闭后上网fail"
        print u"测试WAN口反复关闭后上网pass"

    def test_078_dhcp_dns(self):
        u"""主副DNS有效性测试"""
        result = wan_business.step_100msh0078(self)
        print result
        assert ('192.168.1.1') in result,u"测试主副DNS有效性fail"
        print u"测试主副DNS有效性pass"

    def test_080_dhcp_hostname(self):
        u"""发送主机名功能检查测试"""
        result = wan_business.step_100msh0080(self)
        print result
        assert '100msh.com' in result,u"发送主机名功能检查测试fail"
        print u"发送主机名功能检查测试pass"

    def test_081_dhcp_mac_clone(self):
        u"""wan为dhcp时MAC地址克隆"""
        result = wan_business.step_100msh0072(self)
        print result
        #如果结果为1则通过，否则不通过
        assert result == 1,u"测试wan为dhcp时MAC地址克隆fail"
        print u"测试wan为dchp时MAC地址克隆pass"

    def test_082_dhcp_mtu(self):
        u"""wan为dhcp时MTU设置检查"""
        result1 = wan_business.step_100msh0073_1(self)
        result2 = wan_business.step_100msh0073_2(self)
        print result1,result2
        #如果结果为1则通过，否则不通过
        assert result1 == [1,1,1] and result2 == [1,1],u"测试wan为dhcp时MTU设置检查fail"
        print u"测试wan为dhcp时MTU设置检查pass"

    def test_083_pppoe(self):
        u"""PPPOE拨号功能测试"""
        result = wan_business.step_100msh0083(self)
        print result
        #如果2个都为True则通过，否则不通过
        assert result ==[True,True],u"测试WAN为pppoe fail"
        print u"测试WAN为pppoe pass"

    def test_084_pppoe_reboot(self):
        u"""重启/重新上电后上网测试"""
        result = wan_business.step_100msh0075(self)
        print result
        #如果结果为0则通过，否则不通过
        assert result == 0,u"测试WAN为pppoe后重启/重新上电后上网fail"
        print u"测试WAN为pppoe后重启/重新上电后上网pass"

    def test_085_wan_disconnect_connect(self):
        u"""WAN口反复关闭后重新连接"""
        result = wan_business.step_100msh0076(self)
        print result
        #如果结果为0则通过，否则不通过
        assert result == 0,u"测试WAN口反复关闭后重新连接上网fail"
        print u"测试WAN口反复关闭后重新连接上网pass"

    def test_089_pppoe_dns(self):
        u"""主副DNS有效性测试"""
        result = wan_business.step_100msh0078(self)
        print result
        assert '202.96.134.133' in result,u"测试主副DNS有效性fail"
        print u"测试主副DNS有效性pass"
        #测试完成后把上网方式改回默认的dhcp
        wan_business.change_dhcp(self)



    #退出清理工作
    def tearDown(self):
        self.driver.quit()


if __name__=='__main__':
    unittest.main()

__author__ = 'zeng'

