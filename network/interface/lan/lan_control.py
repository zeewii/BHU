#coding=utf-8
#描述：该模块为LAN设置页面中的模块控制层
#作者：曾祥卫

from publicControl import public_control

#编号：Func_lan_28
#描述：获取页面弹出的警告框
#输入：self
#输出：Alert(警告框)
def get_alert(self):
    try:
        driver = self.driver
        #获取页面上的警告信息
        alert=driver.switch_to_alert()
        #返回警告信息
        return alert
    #捕捉异常并打印异常信息
    except Exception,e:
        print u"获取页面弹出的警告框失败，原因如下：\n%s"%e

#编号：Func_lan_29
#描述：点击“保存&应用”提交表单
#输入：self
#输出：None
def apply(self):
    public_control.apply(self)

#编号：Func_lan_30
#描述：点击“复位”
#输入：self
#输出：None
def reset(self):
    public_control.reset(self)


__author__ = 'zeng'
