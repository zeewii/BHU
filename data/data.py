#coding=utf-8
#描述:本模块用来调用数据，方便测试用例来调用
#作者：曾祥卫

import csv,random
import xlrd

XLSFILE = xlrd.open_workbook('./data/data.xlsx')

#作者：孔志兵
#描述：该函数用以从文件中获取登录IP，用户名，密码，后台密码，软件版本号信息
def get_login_data():
    xlsFile = xlrd.open_workbook('./data/userPassword.xls')
    sh=xlsFile.sheet_by_index(0)#文件中的地一个表
    login_data = {}
    login_data['ip'] =  sh.cell_value(1,0)
    login_data['user'] =  sh.cell_value(1,1)
    login_data['pwd']=  sh.cell_value(1,2)
    login_data['pwd_ssh'] =  sh.cell_value(1,3)
    login_data['version']=  sh.cell_value(1,4)
    return login_data


#描述：调用web页面的默认登录ip，用户名和密码，然后返回给函数
#输入：目录下/data/data.xlsx-basic_conf
#输出：以列表形式输出默认登录ip，用户名和密码
def default_web_user_password():
    try:
        #定义一个列表
        user_password = []
        #打开默认登录web页面的用户名和密码的文件
        xlsFile = xlrd.open_workbook("./data/data.xlsx")
        #获取文件中的对应的表
        sh=xlsFile.sheet_by_name('basic_conf')
        #取ip
        user_password.append(sh.cell_value(3,1))
        #取用户名
        user_password.append(sh.cell_value(5,1))
        #取密码
        user_password.append(sh.cell_value(6,1))
        #将值返回给函数
        return user_password
    except IOError,e:
        print u"文件信息错误,具体信息：\n%s"%e


#作者：尹霞
#描述：调用ssh的默认登录ip，用户名和密码，然后返回给函数
#输入：目录下/data/data.xlsx中的basic_conf
#输出：以列表形式输出默认登录ip，用户名和密码
def ssh_user():
    try:
        #定义一个列表
        user = []
        #获取对应的表-basic_conf
        table = XLSFILE.sheet_by_name('basic_conf')
        #获取表中ip.username\ssh密码的位置并取的值
        ip = table.cell_value(3,1)
        username = table.cell_value(5,1)
        pwd = table.cell_value(10,1)
        user.append(ip)
        user.append(username)
        user.append(pwd)
        return user
    except IOError,e:
        print u"文件信息错误,具体信息：\n%s"%e

#作者：曾祥卫
#描述：取出client运行需要root权限的命令时所需要输入的client的密码，然后返回给函数
#输入：目录下/data/data.xlsx中的basic_conf
#输出：以字符串形式返回密码给函数
def client_password():
    try:
        #打开data.xlsx取测试所需数据
        xlsFile = xlrd.open_workbook("./data/data.xlsx")
        #获取文件中的对应的表
        sh=xlsFile.sheet_by_name('basic_conf')
        #取测试所需密码
        pw = sh.cell_value(16,1)
        #密码返回给函数
        return pw
    except IOError,e:
        print u"文件信息错误,具体信息：\n%s"%e


###########################################
#以下是测试lan时所需测试数据函数
###########################################

#描述：测试用例100msh0054，100msh0055时所需的ip和对应的子网掩码
#输入：目录下/data/data.xlsx-lan_conf
#输出：以列表形式输出所要修改的ip和对应的子网掩码
def ip_netmask():
    try:
        #打开data.xlsx取测试所需数据
        xlsFile = xlrd.open_workbook("./data/data.xlsx")
        #获取文件中的对应的表
        sh=xlsFile.sheet_by_name('lan_conf')
        #取测试所需ip
        ip = sh.col_values(1)[2:6]
        #去测试所需子网掩码
        netmask = sh.col_values(2)[2:6]
        #返回给函数
        return ip,netmask
    except IOError,e:
        print u"文件信息错误,具体信息：\n%s"%e

#描述：测试用例100msh0056(自定义子网掩码设置)所需的ip和子网掩码
#输入：目录下/data/data.xlsx-lan_conf
#输出：以列表形式输出默认登录ip，用户名和密码
def custom_ip_netmask():
    try:
        #打开data.xlsx取测试所需数据
        xlsFile = xlrd.open_workbook("./data/data.xlsx")
        #获取文件中的对应的表
        sh=xlsFile.sheet_by_name('lan_conf')
        #取测试所需ip
        ip = sh.col_values(1)[2:6]
        #去测试所需子网掩码
        netmask = sh.col_values(3)[2:6]
        #返回给函数
        return ip,netmask
    except IOError,e:
        print u"文件信息错误,具体信息：\n%s"%e

#描述：测试用例100msh0057(广播地址)所需的广播地址
#输入：目录下/data/data.xlsx-lan_conf
#输出：以列表形式输出所需测试的广播地址
def lan_broadcast():
    try:
        #打开data.xlsx取测试所需数据
        xlsFile = xlrd.open_workbook("./data/data.xlsx")
        #获取文件中的对应的表
        sh=xlsFile.sheet_by_name('lan_conf')
        #取测试所需广播地址
        broadcast = sh.col_values(1)[9:11]
        #将值返回给函数
        return broadcast
    except IOError,e:
        print u"文件信息错误,具体信息：\n%s"%e

#描述：测试用例100msh0067,68(IP地址和网关输入非法字符)所需要的字符
#输入：目录下/data/data.xlsx-lan_conf
#输出：以列表形式输出所需要的字符
def lan_illegal_character():
    try:
        #打开data.xlsx取测试所需数据
        xlsFile = xlrd.open_workbook("./data/data.xlsx")
        #获取文件中的对应的表
        sh=xlsFile.sheet_by_name('lan_conf')
        #取测试所需字符
        illegal_character = sh.col_values(1)[14:18]
        #将值返回给函数
        return illegal_character
    except IOError,e:
        print u"文件信息错误,具体信息：\n%s"%e

###########################################
#以下是测试wan时所需测试数据函数
###########################################

#描述：测试用例100msh0069(WAN设置为静态IP地址)所需要的字符
#输入：目录下/data/data.xlsx-wan_conf
#输出：以列表形式输出所需要的字符
def wan_staticip_data():
    try:
        #打开data.xlsx取测试所需数据
        xlsFile = xlrd.open_workbook("./data/data.xlsx")
        #获取文件中的对应的表
        sh=xlsFile.sheet_by_name('wan_conf')
        #取测试所需广播地址
        wan_staticip_data = sh.col_values(1)[2:5]
        #将值返回给函数
        return wan_staticip_data
    except IOError,e:
        print u"文件信息错误,具体信息：\n%s"%e

#描述：测试用例100msh0070(广播地址)所需的广播地址
#输入：目录下/data/data.xlsx-wan_conf
#输出：以列表形式输出所需测试的广播地址
def wan_broadcast():
    try:
        #打开data.xlsx取测试所需数据
        xlsFile = xlrd.open_workbook("./data/data.xlsx")
        #获取文件中的对应的表
        sh=xlsFile.sheet_by_name('wan_conf')
        #取测试所需广播地址
        broadcast = sh.col_values(1)[8:10]
        #将值返回给函数
        return broadcast
    except IOError,e:
        print u"文件信息错误,具体信息：\n%s"%e

#描述：测试用例100msh0071(自定义DNS)所需的dns地址
#输入：目录下/data/data.xlsx-wan_conf
#输出：以列表形式输出所需的dns地址
def wan_dns():
    try:
        #打开data.xlsx取测试所需数据
        xlsFile = xlrd.open_workbook("./data/data.xlsx")
        #获取文件中的对应的表
        sh=xlsFile.sheet_by_name('wan_conf')
        #取测试所需的DNS
        dns= sh.col_values(1)[13:15]
        #将值返回给函数
        return dns
    except IOError,e:
        print u"文件信息错误,具体信息：\n%s"%e

#描述：测试用例100msh0073(MTU值有效性)所需的无效的mtu值
#输入：目录下/data/data.xlsx-wan_conf
#输出：以列表形式输出所需的无效的mtu值
def wan_illegal_mtu():
    try:
        #打开data.xlsx取测试所需数据
        xlsFile = xlrd.open_workbook("./data/data.xlsx")
        #获取文件中的对应的表
        sh=xlsFile.sheet_by_name('wan_conf')
        #取测试所需的无效的mtu值
        mtu= sh.col_values(1)[18:20]
        #将值返回给函数
        return mtu
    except IOError,e:
        print u"文件信息错误,具体信息：\n%s"%e

#描述：测试用例100msh0073(MTU值有效性)所需的有效的mtu值
#输入：目录下/data/data.xlsx-wan_conf
#输出：以列表形式输出所需的有效的mtu值
def wan_mtu():
    try:
        #打开data.xlsx取测试所需数据
        xlsFile = xlrd.open_workbook("./data/data.xlsx")
        #获取文件中的对应的表
        sh=xlsFile.sheet_by_name('wan_conf')
        #取测试所需的mtu值
        mtu= sh.col_values(1)[23:25]
        mtu_low = sh.col_values(2)[23:25]
        mtu_up = sh.col_values(3)[23:25]
        return mtu,mtu_low,mtu_up
    except IOError,e:
        print u"文件信息错误,具体信息：\n%s"%e

#描述：测试用例100msh0083(PPPOE拨号功能)所需的用户名和密码
#输入：目录下/data/data.xlsx-wan_conf
#输出：以列表形式输出所需的用户名和密码
def pppoe_id_passwd():
    try:
        #打开data.xlsx取测试所需数据
        xlsFile = xlrd.open_workbook("./data/data.xlsx")
        #获取文件中的对应的表
        sh=xlsFile.sheet_by_name('wan_conf')
        #取测试所需的用户名和密码
        pppoe= sh.col_values(1)[28:30]
        #将值返回给函数
        return pppoe
    except IOError,e:
        print u"文件信息错误,具体信息：\n%s"%e

#描述：测试用例100msh0088(PPPOE拨号功能)所需的错误的用户名和密码
#输入：目录下/data/data.xlsx-wan_conf
#输出：以列表形式输出所需的错误的用户名和密码
def pppoe_err_id_passwd():
    try:
        #打开data.xlsx取测试所需数据
        xlsFile = xlrd.open_workbook("./data/data.xlsx")
        #获取文件中的对应的表
        sh=xlsFile.sheet_by_name('wan_conf')
        #取测试所需的用户名和密码
        pppoe= sh.col_values(1)[33:35]
        #将值返回给函数
        return pppoe
    except IOError,e:
        print u"文件信息错误,具体信息：\n%s"%e



#描述：测试用例100msh0160域名绑定所需的有效域名和无效域名
#输入：目录下/data/data.xlsx-dhspdns_conf
#输出：以列表形式输出域名和ip列表
def domain_hijacking_1():
    try:
        #打开data.xlsx取测试所需数据
        xlsFile = xlrd.open_workbook("./data/data.xlsx")
        #获取文件中的对应的表
        sh=xlsFile.sheet_by_name('dhspdns_conf')
        #取测试所需的域名和IP
        domain= sh.col_values(1)[2:4]
        ip = sh.col_values(2)[2:4]
        #返回给函数
        return domain,ip
    except IOError,e:
        print u"文件信息错误,具体信息：\n%s"%e


#描述：测试用例100msh0164域名绑定所需的28个域名
#输入：目录下/data/data.xlsx-dhspdns_conf
#输出：以列表形式输出域名和ip列表
def domain_hijacking_all():
    try:
        #打开data.xlsx取测试所需数据
        xlsFile = xlrd.open_workbook("./data/data.xlsx")
        #获取文件中的对应的表
        sh=xlsFile.sheet_by_name('dhspdns_conf')
        #取测试所需的域名和IP
        domain= sh.col_values(1)[7:35]
        ip = sh.col_values(2)[7:35]
        #返回给函数
        return domain,ip
    except IOError,e:
        print u"文件信息错误,具体信息：\n%s"%e

#描述：测试用例100msh0165域名绑定所需的10个域名
#输入：目录下/data/data.xlsx-dhspdns_conf
#输出：以列表形式输出域名和ip列表
def domain_hijacking_2():
    try:
        #打开data.xlsx取测试所需数据
        xlsFile = xlrd.open_workbook("./data/data.xlsx")
        #获取文件中的对应的表
        sh=xlsFile.sheet_by_name('dhspdns_conf')
        #取测试所需的域名和IP
        domain= sh.col_values(1)[38:48]
        ip = sh.col_values(2)[38:48]
        #返回给函数
        return domain,ip
    except IOError,e:
        print u"文件信息错误,具体信息：\n%s"%e

#描述：测试用例100msh0166域名绑定所需的10个域名
#输入：目录下/data/data.xlsx-dhspdns_conf
#输出：以列表形式输出域名和ip列表
def domain_hijacking_3():
    try:
        #打开data.xlsx取测试所需数据
        xlsFile = xlrd.open_workbook("./data/data.xlsx")
        #获取文件中的对应的表
        sh=xlsFile.sheet_by_name('dhspdns_conf')
        #取测试所需的域名和IP
        domain= sh.col_values(1)[51:61]
        ip = sh.col_values(2)[51:61]
        #返回给函数
        return domain,ip
    except IOError,e:
        print u"文件信息错误,具体信息：\n%s"%e

#描述：测试用例100msh0167域名绑定所需的2个域名
#输入：目录下/data/data.xlsx-dhspdns_conf
#输出：以列表形式输出域名和ip列表
def domain_hijacking_4():
    try:
        #打开data.xlsx取测试所需数据
        xlsFile = xlrd.open_workbook("./data/data.xlsx")
        #获取文件中的对应的表
        sh=xlsFile.sheet_by_name('dhspdns_conf')
        #取测试所需的域名和IP
        domain= sh.col_values(1)[64:66]
        ip = sh.col_values(2)[64:66]
        #返回给函数
        return domain,ip
    except IOError,e:
        print u"文件信息错误,具体信息：\n%s"%e

#描述：测试用例100msh0168域名绑定所需的域名
#输入：目录下/data/domain_hijacking_5.csv
#输出：以列表形式输出域名和ip列表
def domain_hijacking_5():
    try:
        #打开data.xlsx取测试所需数据
        xlsFile = xlrd.open_workbook("./data/data.xlsx")
        #获取文件中的对应的表
        sh=xlsFile.sheet_by_name('dhspdns_conf')
        #取测试所需的域名和IP
        domain= sh.col_values(1)[66:67]
        ip = sh.col_values(2)[66:67]
        #返回给函数
        return domain,ip
    except IOError,e:
        print u"文件信息错误,具体信息：\n%s"%e


#描述：随机提取weblist.csv中的网站和标题
#输入：None
#输出：url,title
def rand_get_network():
     try:
        '''path = './data/weblist.csv'
        datas = csv.reader(file(path,'rb'))
        data = random.sample(list(datas)[1:],1)
        for i in data:
            url =  i[0].decode('gbk').encode('utf8')
            title =  i[1].decode('gbk').encode('utf8')
            return url,title'''
        table = XLSFILE.sheet_by_name('wifidog_conf')
        nrows = table.nrows
        ncols = table.ncols
        count = random.randint(19,26)
        print count
        colnames = table.row_values(count)

        return colnames[0],colnames[1]

     except IOError,e:
         print u"文件信息错误,具体信息：\n%s"%e

#描述：提取密码表格中的密码，其中第0列为第一次输入的密码，第1列为确认密码
#输入：None
#输出：nrow,ncol   nrow为行，现有数据共13行，    ncol为列，现有数据共3列，其中第3列为备注
#
def xls_pwd(nrow,ncol):
    xlspath = './data/admin_pwd.xls'
    xlsfile = xlrd.open_workbook(xlspath)
    xlsrange = range(xlsfile.nsheets)
    try:
        sh = xlsfile.sheet_by_name('admin_pwd')
        nrows = sh.nrows
        ncols = sh.ncols
        #print '行数为 %d,列数为 %d' %(nrows,ncols)
        pwd = sh.cell_value(nrow,ncol)
        return pwd
    except:
        print 'no sheet in %s name admin_pwd' %xlspath


#描述：提取公共数据表格中的参数
#输入：sheet,nrow,ncol
#      sheet为工作表名；nrow为表格中行数；ncol为表格中列数
#输出：提取的参数的值，如工作表不存在则打印异常信息
def xls_data(sheet,nrow,ncol):
    xlspath = './data/data.xlsx'
    xlsfile = xlrd.open_workbook(xlspath)
    xlsrange = range(xlsfile.nsheets)
    try:
        sh = xlsfile.sheet_by_name(sheet)
        pwd = sh.cell_value(nrow,ncol)
        return pwd
    except:
        print 'no sheet in %s name %s' %(xlspath,sheet)


__author__ = 'zeng'

if __name__ == '__main__':
    ssh_user()