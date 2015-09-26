#coding=utf-8

#描述:修改密码用例模块
#作者：孔志兵

import unittest
#import nose
from selenium import webdriver
from system.admin import admin_control,admin_business
from login import login_control
from data import data

login_data=data.get_login_data()
ip=login_data.get("ip") #路由器管理IP
user=login_data.get("user") #路由器登录用户名
pwd=login_data.get("pwd")     #路由器登录密码
url='http://%s' %ip  #路由器管理URL

class AdminTest(unittest.TestCase):
     def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        login_control.set_user(self,user,pwd)
        login_control.submit(self)
        admin_control.menu(self)

     #测试管理权，即修改登录密码---100msh0033
     def test_managePurview(self):
         u'''修改登录密码 '''
         result = admin_business.updatePassword(self,u'kongzhibing',u'kongzhibing')
         assert result == True,u'页面上修改成功后，使用修改后的密码登陆不进去'
         print u'修改登录密码验证成功'

     #测试管理权，修改登录密码为纯数字---100msh0033
     def test_managePurview_0033(self):
         u''' 修改登录密码为纯数字---100msh0033'''
         result = admin_business.updatePassword(self,'123456','123456')
         assert result == True,u'页面上修改成功后，使用修改后的密码登陆不进去'
         print u'修改登录密码为纯数字-验证成功'


     #测试管理权，修改登录密码为纯字母---100msh0034
     def test_managePurview_0034(self):
         u'''修改登录密码为纯字母 ---100msh0034'''
         result = admin_business.updatePassword(self,u'qwertyui',u'qwertyui')
         assert result == True,u'页面上修改成功后，使用修改后的密码登陆不进去'
         print u'修改登录密码为纯字母-验证成功'

     '''
     #测试管理权，修改登录密码为中文--100msh0035
     def test_managePurview_0035(self):
         result = admin_business.updatePassword(self,u'中国',u'中国')
         assert result == True,u'页面上修改成功后，使用修改后的密码登陆不进去'
         print u'修改登录密码为中文-验证成功'
     '''

     #测试管理权，修改登录密码为特殊字符--100msh0036
     def test_managePurview_0036(self):
         u''' 修改登录密码为特殊字符--100msh0036'''
         result = admin_business.updatePassword(self,u'!@#$%^^',u'!@#$%^^')
         assert result == True,u'页面上修改成功后，使用修改后的密码登陆不进去'
         print u'修改登录密码为特殊字符验证成功-验证成功'

     #测试管理权，修改登录密码,密码与确认密码不一致--100msh0037
     def test_managePurview_0037(self):
         u'''修改登录密码,密码与确认密码不一致--100msh0037 '''
         admin_control.set_pwd(self,'123456','543216')
         admin_control.submit(self)
         error = admin_control.get_errorbox(self)
         assert error,u'密码与确认密码不一致时，没有错误提示信息'
         info = admin_control.get_errof_info(error)
         assert u'由于密码验证不匹配，密码没有更改！' in info,u'密码与确认密码不一致时,提示信息不正确'


     #测试管理权，修改密码为空--100msh0039
     def test_managePurview_0039(self):
         u'''修改密码为空--100msh0039 '''
         admin_control.set_pwd(self,'','')
         admin_control.submit(self)
         login_control.logout(self)
         login_control.set_user(self,'root','bm100@rut!%v2')
         login_control.submit(self)
         title = self.driver.title
         assert u'总览' in title,u'页面上修改密码为空后，使用原来的密码登陆不进去'
         print u'修改密码为空--验证成功'

     #测试管理权，修改密码为最小长度-1-100msh0040
     def test_managePurview_0040(self):
         u''' 修改密码为最小长度-1-100msh0040'''
         admin_control.set_pwd(self,'123qw','123qw')
         admin_control.submit(self)
         alert = admin_control.get_alert(self)
         assert alert,u'修改密码为最小长度-1时，没有提示信息'
         alertinfo = admin_control.get_aler_info(alert)
         assert alertinfo == u'一些项目的值无效，无法保存！',u'提示信息内容不符合'
         print u'修改密码为最小长度-1验证成功'

     #测试管理权，修改密码为最大长度-100msh0042
     def test_managePurview_0042(self):
         u'''修改密码为最大长度-100msh0042 '''
         result = admin_business.updatePassword(self,'12345678901234567890','12345678901234567890')
         assert result == True,u'页面上修改成功后，使用修改后的密码登陆不进去'
         print u'修改密码为最大长度-验证成功'

     #测试管理权，修改密码为最大+1长度-100msh0043
     def test_managePurview_0043(self):
         u''' 修改密码为最大+1长度-100msh0043'''
         admin_control.set_pwd(self,'123456789012345678901','123456789012345678901')
         admin_control.submit(self)
         alert = admin_control.get_alert(self)
         assert alert,u'修改密码为最大长度+1时，没有提示信息'
         alertinfo = admin_control.get_aler_info(alert)
         assert alertinfo == u'一些项目的值无效，无法保存！',u'提示信息内容不符合'
         print u'修改密码为最大长度+1验证成功'

     #退出
     def tearDown(self):
         #每次密码都要改回原来的，防止前面的错误导致后面的用例运行错误
         admin_control.menu(self)
         admin_control.set_pwd(self,'bm100@rut!%v2','bm100@rut!%v2')
         admin_control.submit(self)
         self.driver.quit()


if __name__=='__main__':
    unittest.main()
    #nose.main()

__author__ = 'kzb'

