#coding=utf-8
#描述：本模块实现通过scp拷贝文件到另一个主机(这里是路由器)上
#作者：曾祥卫

import pexpect
#描述：本函数实现通过scp拷贝文件到另一个主机(这里是路由器)上
#输入：filename-本地文件名(也可以是文件的路径)，user-登录名,ip-登录ip,
    # password-登录密码,dir-remote主机的文件路径(也可以远程主机的文件名)
#输出：无
def scp_to_remote(filename,ip,user,password,dir):
    try:
        scp_newkey = 'Are you sure you want to continue connecting (yes/no)?'
        # 为scp命令生成一个spawn类的子程序对象
        child = pexpect.spawn('scp %s %s@%s:%s'%(filename,user,ip,dir))
        #列出期望出现的字符串，超时，'password',scp_newkey
        i = child.expect([pexpect.TIMEOUT,scp_newkey,'password: '])

        #如果匹配到了超时
        if i == 0:
            print "scp登录时出现超时:"
            #打印出错信息
            print child.before, child.after
            return None

        #如果出现的字符串为ssh_newkey，即第一次登录，没有public key
        if i == 1:
           #输入'yes'
            child.sendline('yes')
            #列出期望出现的字符串，超时或'password:'
            i = child.expect([pexpect.TIMEOUT, 'password: '])
            #如果出现的字符串为pexpect.TIMEOUT超时
            if i == 0:
                print 'scp登录时出现超时:'
                #打印出错信息
                print child.before, child.after
                return None

        #如果匹配到了密码字符
        child.sendline(password)

        #列出输入密码后期望出现的字符串，'password',EOF，超时'
        i = child.expect(["(?i)password",pexpect.EOF,pexpect.TIMEOUT])
        #匹配到pexpect.EOF，
        if i == 0:
            print '密码输入错误！'
        elif i == 1:
            print '恭喜,scp上传文件成功！'
        else:
            print '传输文件超时！'

    except pexpect.ExceptionPexpect, e:
        print "scp连接失败",str(e)
        pexpect.run("rm -rf ~/.ssh")


#描述：本函数实现通过scp从remote主机(这里是路由器)上拷贝文件到本机上
#输入：filename-远程文件名，user-登录名,ip-登录ip,
    # password-登录密码,dir-本机的文件路径(也可以远程主机的文件名)
#输出：无
def scp_to_local(ip,user,password,filename,dir):
    try:
        scp_newkey = 'Are you sure you want to continue connecting (yes/no)?'
        # 为scp命令生成一个spawn类的子程序对象
        child = pexpect.spawn('scp %s@%s:%s %s'%(user,ip,filename,dir))
        #列出期望出现的字符串，超时，'password',scp_newkey
        i = child.expect([pexpect.TIMEOUT,scp_newkey,'password: '])

        #如果匹配到了超时
        if i == 0:
            print "scp登录时出现超时:"
            #打印出错信息
            print child.before, child.after
            return None

        #如果出现的字符串为ssh_newkey，即第一次登录，没有public key
        if i == 1:
           #输入'yes'
            child.sendline('yes')
            #列出期望出现的字符串，超时或'password:'
            i = child.expect([pexpect.TIMEOUT, 'password: '])
            #如果出现的字符串为pexpect.TIMEOUT超时
            if i == 0:
                print 'scp登录时出现超时:'
                #打印出错信息
                print child.before, child.after
                return None

        #如果匹配到了密码字符
        child.sendline(password)

        #列出输入密码后期望出现的字符串，'password',EOF，超时'
        i = child.expect(["(?i)password",pexpect.EOF,pexpect.TIMEOUT])
        #匹配到pexpect.EOF，
        if i == 0:
            print '密码输入错误！'
        elif i == 1:
            print '恭喜,scp下载文件成功！'
        else:
            print '传输文件超时！'

    except pexpect.ExceptionPexpect, e:
        print "scp连接失败",str(e)
        pexpect.run("rm -rf ~/.ssh")



__author__ = 'zeng'
