#coding=utf-8

import urllib
import urllib2
import re

url = ['http://www.chinadaily.com.cn/china/2016-04/12/content_24471420.htm']
url.append('http://www.chinadaily.com.cn/china/2016-04/12/content_24470515.htm')
url.append('http://www.chinadaily.com.cn/china/2016-04/12/content_24465583.htm')
url.append('http://www.chinadaily.com.cn/business/2016-04/12/content_24457629.htm')
url.append('http://www.chinadaily.com.cn/business/2016-04/11/content_24422886.htm')
url.append('http://www.chinadaily.com.cn/business/2016-04/09/content_24397697.htm')
url.append('http://www.chinadaily.com.cn/business/2016-04/09/content_24397290.htm')
url.append('http://www.chinadaily.com.cn/business/chinadata/2016-03/16/content_23898438.htm')
url.append('http://www.chinadaily.com.cn/business/2016-04/12/content_24460897.htm')
url.append('http://www.chinadaily.com.cn/business/2016-04/12/content_24470803.htm')
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent' : user_agent}

try:
    for i in range(10):
        request = urllib2.Request(url[i],headers=headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')

        title_pattern = re.compile('div.*?Title_e">(.*?)</div>',re.S)
        title_items = re.findall(title_pattern,content)
        title_mypat = re.compile(r'<h1.*?>(.*?)</h1>')
        title_myitem = re.findall(title_mypat,title_items[0])
        print title_myitem[0]

        pattern = re.compile('div.*?Content">.*?<table.*?</table>(.*?)<div.*?width',re.S)
        items = re.findall(pattern,content)
        mypat = re.compile(r'.*?<p>(.*?)</p>.*?')
        if(items.__len__()>0):
            myitem = re.findall(mypat,items[0])
        len = myitem.__len__()


        for j in range(len):
            print myitem[j],
        print '\n'
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason