#coding=utf-8
#描述:本模块测试所有测试用例
#描述：本模块还包括测试结束后自动发送邮件给测试人员目前发送方仅限foxmail
#作者：曾祥卫，尹霞

import unittest
import HTMLTestRunner
import smtplib,time,os
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from  email.utils import  parseaddr,formataddr
from email.mime.multipart import MIMEMultipart


#制定testcase文件夹路径
list = './testcase'
#构造测试集
def creatsuite1():
    testunit = unittest.TestSuite()
    #discover方法定义
    discover = unittest.defaultTestLoader.discover(list,
                    pattern ='testcase_*.py',
                    top_level_dir=None)
    #discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for testcase in test_suite:
            testunit.addTest(testcase)
            print testunit
    return testunit

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((
        Header(name,'utf-8').encode(),
               addr.encode('utf-8')
               if isinstance(addr,unicode) else addr))

#描述：已附件的格式群发邮件，只限foxmail邮箱
#输入：fp-测试报告地址，sender-发送者邮箱仅限foxmail
def send(fp,sender):
    #接收邮箱
    #receiver = {'曾祥卫':'zengxiangwei@100msh.com','尹霞':'yinxia@100msh.com','孔志兵':'kongzhibing@100msh.com','张均':'zhangjun@100msh.com'}
    receiver = ['zengxiangwei@100msh.com','yinxia@100msh.com','kongzhibing@100msh.com','zhangjun@100msh.com']
    #发送主题
    subject = 'BHU自动化测试报告'
    #发送邮箱服务器
    smtpserver = "smtp.qiye.163.com"

    #发件邮箱用户和密码
    username = "yinxia@100msh.com"
    password = "yinxia100"
    #获取测试报告
    f = open(fp,'rb')
    mail_body = f.read()
    f.close()
    #中文需参数'utf-8'，单字节字符不需要
    header = MIMEText('hi ! BHU自动化测试完毕，我们已经在第一时间发出邮件通知，请尽快处理！','plain','utf-8')#中文需参数‘utf-8'，单字节字符不需要
    #  msg['Subject'] = Header(subject, 'utf-8')

    #附件传送
    msgroot = MIMEMultipart('related')
    #添加发件人
    msgroot['From'] = _format_addr(u'本轮测试员<%s>'%sender)
    #添加收件人,首先将收件人生生成邮件格式即：XXX<xx@100msh.com>
    to =[]
    for i in receiver:
       to.append(_format_addr(i))
    #群发收件人使用逗号链接
    strto = ','.join(to)

    msgroot['To'] = strto
    #添加主题
    msgroot['Subject'] = subject

    #构造附件
    att = MIMEText(mail_body,'base64','utf-8')
    att["content-type"] = 'application/octet-stream'
    att["content-Disposition"] = 'attachment;filename=%s'%fp

    msgroot.attach(header)
    msgroot.attach(att)

    #html格式
    #msg = MIMEText(mail_body,'html','utf-8')

    #msg['Subject'] = subject
    #开启smtp链接，发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username,password)
    smtp.sendmail(sender,receiver,msgroot.as_string())
    smtp.quit()
    print 'email has send out!'


if __name__ == '__main__':
    os.system('rm -rf ~/.ssh')
    alltestnames = creatsuite1()
    now = time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))
    #filename = './report/'+now+'result.html'
    filename = now+'result.html'
    fp = file(filename, 'wb')

    runner =HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'BHU测试报告',
        description=u'用例执行情况：')

    #执行测试用例
    runner.run(alltestnames)

    #关闭文件
    fp.close()

    #发送测试报告
    send(filename,'yinxia@100msh.com')

__author__ = 'zeng'










