# -*- coding: utf-8 -*-
import cookielib
import re

import requests
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

reload(sys)




# 构造 Request headers
agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
headers = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent': agent
}


class Zhihu_login():
    def __init__(self):
        self.r = requests.session()
        self.r.cookies =cookielib.LWPCookieJar(filename='cookies')

    def get_xsrf(self):
        '''_xsrf 是一个动态变化的参数'''
        index_url = 'https://www.zhihu.com'
        # 获取登录时需要用到的_xsrf
        index_page = self.r.get(index_url, headers=headers)
        html = index_page.text
        print html
        pattern = r'name="_xsrf" value="(.*?)"'
        # 这里的_xsrf 返回的是一个list
        _xsrf = re.findall(pattern, html)
        print _xsrf[0]
        return _xsrf[0]

    def zhihu_login(self):
        login_data={
            "_xsrf": self.get_xsrf(),
            "password":"123456",
            "captcha_type":"cn",
            "phone_num":"18905818037"
        }
        login_url = "https://www.zhihu.com/login/phone_num"
        result = self.r.post(login_url,data=login_data)
        print result
zhihu_login = Zhihu_login()
zhihu_login.zhihu_login()


