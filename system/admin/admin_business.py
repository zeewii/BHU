#coding=utf-8
from login import login_control


import admin_control

#作者：孔志兵
#描述：修改登录密码，并用新的登录密码重新登录，获取登录后的title，用以判断密码是否修改成功
def updatePassword(self,pwd1,pwd2):
         driver = self.driver
         admin_control.set_pwd(self,pwd1,pwd2)
         admin_control.submit(self)
         login_control.logout(self)
         login_control.set_user(self,'root',pwd1)
         login_control.submit(self)
         title = driver.title
         return u'总览' in title

__author__ = 'kzb'