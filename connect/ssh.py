#coding=utf-8

#描述:使用ssh链接路由器的后台
#作者：尹霞，曾祥卫
import pexpect,pxssh,subprocess
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

        #列出输入密码后期望出现的字符串，'password',EOF，超时
        i = child.expect(['password: ',pexpect.EOF,pexpect.TIMEOUT])
        #匹配到字符'password: '，打印密码错误
        if i == 0:
            print u'密码输入错误！'
        #匹配到了EOF，打印ssh登录成功，并输入命令后成功退出
        elif i == 1:
            print u'恭喜,ssh登录输入命令成功！'
        #匹配到了超时，打印超时
        else:
            print u'输入命令后等待超时！'

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

#输入：user-登录名,ip-登录ip,password-登录密码,command-输入命令
#输出：输入命令返回的结果
def ssh_cmd3(user,ip,password,command):
    try:
        #为ssh命令生成一个pxssh类的对象
        child = pxssh.pxssh()
        #利用 pxssh 类的 login 方法进行 ssh 登录，\
        # 原始 prompt 为'$' , '#',这里加入'>'
        child.login(ip,user,password,original_prompt='[#$>]')
        #发送命令
        child.sendline(command)
        #匹配 prompt,即匹配最后出现的字符串有'#$>'
        child.prompt()
        result = child.before

        #将执行命令的时间和结果以追加的形式保存到log.txt文件中备份文件
        f = open('log.txt','a')
        str1 = str(datetime.datetime.now())+' '
        f.writelines(str1+result)
        f.close()

        # 退出 ssh session
        child.logout()
        # 将 prompt 前所有内容返回给函数,即命令的执行结果
        return result

    #异常打印原因并删除public key
    except pxssh.ExceptionPxssh,e:
        print "ssh连接失败，正在重启进程",str(e)
        subprocess.call("rm -rf ~/.ssh",shell=True)

