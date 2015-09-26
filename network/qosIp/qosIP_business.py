#coding=utf-8

import time

from network.qosIp import qosIP_control


#作者：孔志兵

#描述：get_rule函数实现添加一条完整的规则
#输入：id1,id2,id3和id4分别是起始地址，结束地址，下载速度和上传速度的定位
def set_rule(self,startIP,endIP,dlSpeed,upSpeed,i):
    driver = self.driver
    driver.implicitly_wait(10)
    qosIP_control.add(self)
    qosIP_control.set_ip(self,startIP,endIP,i)
    qosIP_control.set_speed(self,dlSpeed,upSpeed,i)
    qosIP_control.submit(self)

#描述：get_alet_text获取警告框的信息
#输出：警告框上的信息
def get_alert_text(self):
    alert = qosIP_control.get_alert(self)
    test =  alert.text
    alert.accept()
    return test

def add_multi(self,numMax):
    driver = self.driver
    ip = ['192','168','11','100']
    dlSpeed = 1024
    upSpeed = 128
    for i in range(1,numMax):
        ip[3] = str(int(ip[3])+1)
        startIp = '.'.join(ip)
        endIp = '.'.join(ip)
        dl = dlSpeed+i*128
        up = upSpeed+i*128
        qosIP_control.add(self)
        qosIP_control.set_ip(self,startIp,endIp,i)
        qosIP_control.set_speed(self,dl,up,i)
    qosIP_control.submit(self)

#通过比较输入的下载速度的值和网页在线测速的值，误差范围在5%内就算用例测试通过
#dlSpeed----页面输入的下载速度
#point ----允许误差范围，如0.2
def dlSpeedCheck(self,dlSpeed,point):
    download = qosIP_control.get_dlSpeed_online(self)
    err = abs(download-dlSpeed)
    print err
    speed = dlSpeed*point
    print speed
    if err < speed :
        print '下载限速成功'
        return True
    else :
        print '下载限速失败'
        return False


#通过比较输入的上传速度的值和网页在线测速的值，误差范围在5%内就算用例测试通过
#upSpeed----页面输入的上传速度
#point -----允许的误差范围，如0.1
def upCheck(self,upSpeed,point):
    qosIP_control.get_dlSpeed_online(self)
    qosIP_control.get_dlSpeed_online(self)
    up = qosIP_control.get_upSpeed_online(self)
    err = abs(up-upSpeed)
    speed = upSpeed*point
    if err < speed :
        print '上传限速成功'
        return True
    else :
        print '上传限速失败'
        return False




__author__ = 'kzb'
