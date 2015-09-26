#coding=utf-8

#描述:使用ssh链接路由器的后台
#作者：尹霞
import pexpect
import datetime,os,time
from data import data

#描述:首先使用 ssh -l user host cmd登录ssh,在确定是否是首次登录，在输出结果
#输入:host-远程登录主机名，username-登录用户名，password-密码,cmd-命令
#输出:命令返回的结果，同时将结果存放在同目录的log.txt文件中
def ssh_cmd(host,user,pwd,cmd):
    try:
        ssh_newkey = "Are you sure you want to continue connecting(yes/no)?"
        # 为 ssh 命令生成一个 spawn 类的子程序对象.
        child = pexpect.spawn('ssh -l %s %s %s'%(user, host, cmd))
        i = child.expect([pexpect.TIMEOUT, ssh_newkey, 'password: '])
        # 如果登录超时，打印出错信息，并退出.
        if i == 0:
            print u"错误，SSH 登录超时:"
            print child.before, child.after
            return None
        # 如果 ssh 没有 public key，接受它.
        if i == 1: # SSH does not have the public key. Just accept it.
            child.sendline ('yes')
            i = child.expect([pexpect.TIMEOUT, 'password: '])
            if i == 0:
                print u"错误，SSH 登录超时:"
                print child.before, child.after
                return None
        # 输入密码.
        child.sendline(pwd)
        child.expect(pexpect.EOF)

        #将执行命令的时间和结果以追加的形式保存到log.txt文件中备份文件
        f = open('log.txt','a')
        str1 = str(datetime.datetime.now())+' command'+cmd
        f.writelines(str1+child.before)
        f.close()

        result = child.before
        return result
    except pexpect.ExceptionPexpect, e:
        print u"ssh连接失败，正在重启进程"
        result2 = os.system("rm -rf ~/.ssh")
        print result2

        time.sleep(10)
        print "delete ssh"
        print e

#描述:从data文件中ssh_login.txt中获取ssh登录所需的数据，再调用ssh_cmd
#输入：cmd-命令
#输出：result-命令结果
def ssh_cmd2(cmd):
    login=[]
    try:
        login = data.ssh_user()
        result = ssh_cmd(login[0],login[1],login[2],cmd)
        return result
    except IOError,e:
        print "文件信息错误,具体信息："
        print e
