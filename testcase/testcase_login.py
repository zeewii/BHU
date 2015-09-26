#coding=utf-8

import unittest
from selenium import webdriver
from system.admin import admin_control,admin_business
from login import login_business,login_control
from data import data
import time


#########################################################
sheet = 'basic_conf'
url = data.xls_data(sheet,3,1)              #路由器登录IP
general_usr = data.xls_data(sheet,5,1)      #普通用户用户名
general_pwd = data.xls_data(sheet,6,1)      #普通用户密码
adv_usr = data.xls_data(sheet,7,1)          #高级用户用户名
adv_pwd = data.xls_data(sheet,8,1)          #高级用户密码
digit_pwd = '12345678'                    #纯数字密码
letter_pwd = 'abcdefgh'                   #纯英文密码
mini_pwd = '100msh'                       #6字节密码（最小有效值）
mini_pwd1 = '100ms'                       #5字节密码（低于最小值）
max_pwd = 'https.www.100msh.com'       #20字节密码（最大有效值）
max_pwd1 = 'https.www.100msh.com1'     #21字节密码（大于最大值）
china_pwd = u'百米生活'                   #中文密码
special_pwd = '100msh!@#$'               #含特殊字符密码

#########################################################


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        print u'登录页面已打开'

    #用户名和密码均为空时
    def test_nulllogin(self):
        login_control.set_user(self,'','')
        login_control.submit(self)
        login_control.get_error(self)
        print u'登陆用户名、密码都为空时--验证成功'
        login_business.default_login(self)

    #用户名为空时
    def test_unllusr(self):
        login_control.set_user(self,'',general_pwd)
        login_control.submit(self)
        login_control.get_error(self)
        print u'登陆用户名为空--验证成功'
        login_business.default_login(self)

    #密码为空时
    def test_unllpwd(self):
        login_control.set_user(self,general_usr,'')
        login_control.submit(self)
        login_control.get_error(self)
        print u'登陆密码为空--验证成功'
        login_business.default_login(self)


    #密码为1字节时
    def test_1bytepwd(self):
        login_control.set_user(self,general_usr,'1')
        login_control.submit(self)
        login_control.get_error(self)
        print u'登陆密码为1字节时--验证成功'
        login_business.default_login(self)

    #密码为5字节时
    def test_5bytepwd(self):
        login_control.set_user(self,general_usr,mini_pwd1)
        login_control.submit(self)
        login_control.get_error(self)
        print u'登陆密码长度小于最小有效值时--验证成功'
        login_business.default_login(self)


    #密码为6字节时
    def test_6bytepwd(self):
        login_business.default_login(self)
        admin_control.menu(self)
        result = admin_business.updatePassword(self,mini_pwd,mini_pwd)
        assert result == True,u'密码修改成功后，使用修改后的密码登陆不进去'
        print u'登录密码长度为最小有效值时--验证成功'

    #密码为20字节时
    def test_20bytepwd(self):
        login_business.default_login(self)
        admin_control.menu(self)
        result = admin_business.updatePassword(self,max_pwd,max_pwd)
        assert result == True,u'密码修改成功后，使用修改后的密码登陆不进去'
        print u'登录密码长度等于最大有效值时--验证成功'


    #密码为21字节时
    def test_21bytepwd(self):
        login_control.set_user(self,web_usr,max_pwd1)
        login_control.submit(self)
        login_control.get_error(self)
        print u'登陆密码长度大于最大有效值时--验证成功'
        login_business.default_login(self)

    #密码为纯数字时
    def test_digital(self):
        login_business.default_login(self)
        admin_control.menu(self)
        result = admin_business.updatePassword(self,digit_pwd,digit_pwd)
        assert result == True,u'密码修改成功后，使用修改后的密码登陆不进去'
        print u'登录密码为21字节时-验证成功'


    #密码为纯字母时
    def test_letter(self):
        login_business.default_login(self)
        admin_control.menu(self)
        result = admin_business.updatePassword(self,letter_pwd,letter_pwd)
        assert result == True,u'密码修改成功后，使用修改后的密码登陆不进去'
        print u'登录密码为纯字母时-验证成功'

    #密码为含特殊字符时
    def test_special(self):
        login_business.default_login(self)
        admin_control.menu(self)
        result = admin_business.updatePassword(self,special_pwd,special_pwd)
        assert result == True,u'密码修改成功后，使用修改后的密码登陆不进去'
        print u'登录密码含特殊字符时-验证成功'

    #高级用户默认密码登录
    def test_advdefault(self):
        login_control.set_user(self,adv_usr,adv_pwd)
        login_control.submit(self)
        login_control.get_error(self)
        print u'高级用户默认密码登录--验证成功'

    #高级用户非默认密码登录
    def test_advpwd(self):
        login_control.set_user(self,adv_usr,adv_pwd)
        login_control.submit(self)
        admin_control.menu(self)
        result = admin_business.updatePassword(self,letter_pwd,letter_pwd)
        assert result == True,u'密码修改成功后，使用修改后的密码登陆不进去'
        print u'高级用户非默认密码登录--验证成功'



    #退出
    def tearDown(self):
        #每次密码都要改回原来的，防止前面的错误导致后面的用例运行错误
        admin_control.menu(self)
        admin_control.set_pwd(self,general_pwd,general_pwd)
        admin_control.submit(self)
        time.sleep(5)
        self.driver.quit()

if __name__=='__main__':
    unittest.main()









__author__ = 'super'



