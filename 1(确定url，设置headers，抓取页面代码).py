#coding:utf-8

__author__ = 'greatbuger'

import urllib,urllib2

page = 1
url = 'http://www.qiushibaike.com/8hr/page/' + str(page)
user_agent = 'Mozilla/5.0(xll;Linux x86_64)'
headers = {'User-Agent' : user_agent}
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    print response.read()
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

