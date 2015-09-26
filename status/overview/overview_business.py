#coding=utf-8
from status.overview.overview_control import *
from login import login_control

#作者：孔志兵
#描述：version_compare用以判断版本号是否正确

def version_compare(self,version):
    menu(self)
    version1 = get_web_version(self)
    version2 = get_houtai_version(self)
    if version == version1 :
        if version1 == version2 :
            return True
    elif version != version1 :
        print u'需求版本号与页面版本号显示的不一致'
        return False
    elif version1 != version2 :
        print u'页面版本号和后台版本号显示的不一致'
        return False


__author__ = 'kzb'
