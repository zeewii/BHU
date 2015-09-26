#coding=utf-8

import unittest
from selenium import webdriver
from system.admin import admin_control,admin_business
from login import login_business,login_control
from data import data
from system.flashops import flashops_control
import time


#########################################################
bakconfig = '/home/svn/BHUv1.0/data/bakconfig/BHU/backup-100msh.com-2015-09-14.tar.gz'
firmware = '/home/svn/BHUv1.0/data/firmware/100MSHBHU2S_R_2.2.0_2015_07_07_16_56'
bakconf = '/home/svn/BHUv1.0/data/firmware/bakconfig/'

#调戏时使用，与setup中的 admin_login对应
'''
url = "http://192.168.11.1"
user = 'root'
passwd = 'bm100@rut!%v2'
'''
#########################################################


class AdminTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        #login_business.admin_login(self,url,user,passwd)
        login_business.default_login(self)
        flashops_control.flashops_menu(self)
        print '备份升级页面已打开'

    #固件升级
    def test_upgrade(self):
        flashops_control.set_savconf_disable(self)
        flashops_control.flash_upload(self,firmware)
        #点击刷写固件按钮
        flashops_control.flash_upgrade(self)
        flashops_control.flash_submit(self)
        time.sleep(3)
        #获取固件刷写进度条
        flashops_control.get_Progress(self)
        time.sleep(40)


    #恢复备份
    def test_rebakconf(self):
        flashops_control.set_bakconf(self,bakconfig)
        flashops_control.bakconf_upload(self)
        time.sleep(5)
        flashops_control.get_Progress(self)
        time.sleep(60)






    #退出
    def tearDown(self):
         self.driver.quit()

if __name__=='__main__':
    unittest.main()
    #nose.main()



__author__ = 'super'
