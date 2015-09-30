#coding=utf-8
#描述：本模块为使用tcpdump抓包的业务层模块
#作者：曾祥卫

import tcpdump_control
from connect import ssh
from publicControl import public_control
import subprocess,time
from selenium import webdriver
from login import login_business
from network.wifidog import general_control
from data import data

#描述：本函数实现通过路由的ssh的默认ip，用户名，密码登录路由后修改路由文件内容
#输入：filename-路由器上需要修改的文件名，dir-路由器的文件路径，content-需要修改的内容
#输出：无
def modify_remote_file(dir,filename,content):
    #调用ssh的默认登录ip，用户名和密码
    d = data.ssh_user()
    #登录remote主机下载需要修改的文件
    tcpdump_control.scp_to_local(d[0],d[1],d[2],dir+filename,'./data/')
    #登录remote主机并备份文件
    ssh.ssh_cmd3(d[1],d[0],d[2],'mv %s%s %s%s_backup'\
                            %(dir,filename,dir,filename))
    print '备份remote主机的文件%s%s成功'%(dir,filename)
    #在本地打开下载的文件，清空原内容并写入需要新内容
    public_control.modify_file('./data/%s'%filename,content)
    #通过scp再传输给remote主机
    tcpdump_control.scp_to_remote('./data/%s'%filename,d[0],d[1],d[2],dir)
    print '修改remote主机文件%s%s成功'%(dir,filename)
    #删除本地到文件
    subprocess.call('rm -rf ./data/%s'%filename,shell=True)

#描述：本函数实现通过路由的ssh的默认ip，用户名，密码登录后tcpdump抓取路由器WAN口的包
#输入：wan-wan接口的接口名
#输出：封包保持的文件名：/tmp/wanlog
def capture_wan_packet():
    #调用ssh的默认登录ip，用户名和密码
    d = data.ssh_user()
    tcpdump_control.tcpdump_command(d[1],d[0],d[2],'tcpdump -i eth1 -s0 -w /tmp/wanlog')
    return '/tmp/wanlog'

#描述：本函数实现通过路由的ssh的默认ip，用户名，密码登录后tcpdump抓取路由器WAN口的包
#输入：wlan-wlan接口的接口名
#输出：封包保持的文件名：/tmp/wlanlog
def capture_wlan_packet():
    #调用ssh的默认登录ip，用户名和密码
    d = data.ssh_user()
    tcpdump_control.tcpdump_command(d[1],d[0],d[2],'tcpdump -i wlan0 -s0 -w /tmp/wlanlog')
    return '/tmp/wlanlog'


###############################################
#以下是所需要抓包的测试用例的测试步骤
###############################################

#描述：#描述：测试用例100msh0287测试步骤----ping报文内容字段检查
def step_100msh0287(self):

    #修改门户认证的检查间隔为60s
    general_control.set_checkInterval(self,'60')
    general_control.apply(self)
    time.sleep(60)

    #上传tcpdump到路由器
    #调用ssh的默认登录ip，用户名和密码
    d = data.ssh_user()
    tcpdump_control.scp_to_remote('./data/BHU_tcpdump/tcpdump',d[0],d[1],d[2],'/usr/sbin/')
    tcpdump_control.scp_to_remote('./data/BHU_tcpdump/libpcap.so.1.3',d[0],d[1],d[2],'/usr/lib/')

    #ssh登录路由输入tcpdump抓包
    wanlog = capture_wan_packet()
    #将抓到的封包传输回本地pc
    tcpdump_control.scp_to_local(d[0],d[1],d[2],wanlog,'./data/')

    #打开本地下载的文件，读取文件内容
    f = open('./data/wanlog')
    log = f.read()
    f.close()

    '''#获取路由网关ID
    gw = general_control.get_gatewayId(self)
    #路由mac
    r_mac = ssh.ssh_cmd2("ifconfig eth0 | grep HWaddr | awk '{print$5}'")
    R_MAC = r_mac.upper()
    #路由版本
    r_version = ssh.ssh_cmd2('cat /etc/version/version')
    R_VERSION = r_version.upper()
    #路由无线mac
    wlan_mac = ssh.ssh_cmd2("ifconfig wlan0 | grep HWaddr | awk '{print$5}'")
    WLAN_MAC = wlan_mac.upper()'''

    #正确的心跳ping信息字符如下
    ping_str1 = 'GET /index/ping/?gw_id='
    #ping_str2 = 'route_mac=%s&route_version=%s&wlan_mac_0=%s'%(R_MAC,R_VERSION,WLAN_MAC)

    if ping_str1 in log:
        #ping信息在log信息中，说明有心跳信息，结果赋值1
        result = 1
    else:
        #ping信息不在log信息中，说明没有心跳信息，结果赋值0
        result = 0
    #结果返回给函数
    return result


#描述：#描述：测试用例100msh0286测试步骤----分区域管理路由器功能检查
def step_100msh0286(self):

    #修改请求管理接口的时间间隔为1分钟
    content = ['0 2 * * * /bin/rand_upgrade_msh\n',
                '0 4 * * * /sbin/rand_reboot\n',
                '0 6 * * * /etc/init.d/sysntpd restart\n',
                '*/1 * * * * /sbin/get_manage\n',
                '0 1 * * * /sbin/cwifi_pwd\n']
    modify_remote_file('/etc/crontabs/','root',content)
    #重启路由定时机制
    ssh.ssh_cmd2('/etc/init.d/cron restart')
    time.sleep(10)

    #上传tcpdump到路由器
    #上个用例已经上传了，这里就不再上传了
    d = data.ssh_user()
    #tcpdump_control.scp_to_remote('./data/BHU_tcpdump/tcpdump',d[0],d[1],d[2],'/usr/sbin/')
    #tcpdump_control.scp_to_remote('./data/BHU_tcpdump/libpcap.so.1.3',d[0],d[1],d[2],'/usr/lib/')

    #ssh登录路由输入tcpdump抓包
    wanlog = capture_wan_packet()
    #将抓到的封包传输回本地pc
    tcpdump_control.scp_to_local(d[0],d[1],d[2],wanlog,'./data/')

    #打开本地下载的文件，读取文件内容
    f = open('./data/wanlog')
    log = f.read()
    f.close()

    '''#获取路由网关ID
    gw = general_control.get_gatewayId(self)
    #路由mac
    r_mac = ssh.ssh_cmd2("ifconfig eth0 | grep HWaddr | awk '{print$5}'")
    R_MAC = r_mac.upper()
    #路由版本
    r_version = ssh.ssh_cmd2('cat /etc/version/version')
    R_VERSION = r_version.upper()
    #路由无线mac
    wlan_mac = ssh.ssh_cmd2("ifconfig wlan0 | grep HWaddr | awk '{print$5}'")
    WLAN_MAC = wlan_mac.upper()'''

    #正确的patch信息字符如下
    patch_str1 = 'GET /manage/patch?gw_id='
    #patch_str2 = '%s&route_mac=%s&route_version=%s&patch_md5='%(gw,R_MAC,R_VERSION)
    #正确的manage信息字符如下
    manage_str1 = 'GET /manage/manage?gw_id='
    #manage_str2 = '%s&route_mac=%s&route_version=%s&manage_md5='%(gw,R_MAC,R_VERSION)

    if (patch_str1 and manage_str1) in log:
        #patch和manage信息在log信息中，说明有管理接口请求，结果赋值1
        result = 1
    else:
        #patch和manage信息不在log信息中，说明没有管理接口请求，结果赋值0
        result = 0
    #结果返回给函数
    return result




