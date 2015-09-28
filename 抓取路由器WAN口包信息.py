#coding=utf-8
#描述：本模块实现通过tcpdump抓取路由器wan口包的信息
#作者：曾祥卫


import unittest
import time

from selenium import webdriver
from connect import scp,ssh
from network.wifidog import general_control
from login import login_control,login_business
from data import data
from network.interface import interface_business

class Testcapture_wan_packet(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        #将浏览器最大化
        self.driver.maximize_window()

    def test(self):
        print '1'
        ip ='192.168.11.1'
        user = 'root'
        password = 'BHU@100msh$%^'
        #上传tcpdump到路由器
        scp.scp_to_remote('/home/zeng/PycharmProjects/BHU/data/BHU_tcpdump/tcpdump',ip,user,password,'/usr/sbin/')
        print '2'
        scp.scp_to_remote('/home/zeng/PycharmProjects/BHU/data/BHU_tcpdump/libpcap.so.1.3',ip,user,password,'/usr/lib/')

        print '3'
        #默认IP登录路由web页面
        web_user_password = data.default_web_user_password()
        interface_business.open_router_web(self,web_user_password[0])
        #登录路由
        login_control.set_user(self,web_user_password[1],web_user_password[2])
        login_control.submit(self)
        time.sleep(3)
        #进入门户认证，修改网关ID
        general_control.wifidog_menu(self)
        print '4'
        #修改门户认证的检查间隔为60s
        general_control.set_checkInterval(self,'60')
        general_control.apply(self)
        time.sleep(60)
        print '5'
        #ssh登录路由输入tcpdump抓包
        ssh.tcpdump_command(user,ip,password,'tcpdump -i eth1 -s0 -w /tmp/wanlog')
        scp.scp_to_local(ip,user,password,'/tmp/wanlog','/home/zeng/')

        f = open('/home/zeng/wanlog')
        log = f.read()
        f.close()

        if 'GET /index/ping/?gw_id=' and \
                    'route_mac=84:82:F4:0D:22:1C&route_version=100MSHBHU2S_R_2.2.0&wlan_mac_0=84:82:F4:0D:22:1D' \
                    in log:
            print 'pass'
        else:
         print 'failed'


    #退出清理工作
    def tearDown(self):
        self.driver.quit()


if __name__=='__main__':
    unittest.main()



