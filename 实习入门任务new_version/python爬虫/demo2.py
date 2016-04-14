#coding=utf-8

import urllib
import urllib2
import re
import string
import sys
import os

url = ['http://www.chinadaily.com.cn/china/2016-04/12/content_24471420.htm']
url.append('http://www.chinadaily.com.cn/china/2016-04/12/content_24470515.htm')
url.append('http://www.chinadaily.com.cn/business/2016-04/12/content_24457629.htm')
url.append('http://www.chinadaily.com.cn/business/2016-04/09/content_24397697.htm')
url.append('http://www.chinadaily.com.cn/business/2016-04/09/content_24397290.htm')
url.append('http://www.chinadaily.com.cn/business/chinadata/2016-03/16/content_23898438.htm')
url.append('http://www.chinadaily.com.cn/business/2016-04/12/content_24460897.htm')
url.append('http://www.chinadaily.com.cn/business/2016-04/12/content_24470803.htm')
url.append('http://www.chinadaily.com.cn/business/2016-04/12/content_24455437.htm')
url.append('http://www.chinadaily.com.cn/business/2016-04/12/content_24481250.htm')
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

        filename = str(i+1)+'.txt'
        print filename
        f = open(filename, 'w+')
        f.write(title_myitem[0])
        f.write('\n')

        pattern = re.compile('div.*?Content">.*?<table.*?</table>(.*?)<div.*?width',re.S)
        items = re.findall(pattern,content)
        mypat = re.compile(r'.*?<p>(.*?)</p>.*?')
        if(items.__len__()>0):
            myitem = re.findall(mypat,items[0])
        len = myitem.__len__()

        #a = []
        #for j in range(len):
            #a.append(re.split(r' |,|\(|\)|\.',str(myitem[j])))
        #print a

        for j in range(len):
            #print myitem[j]
            f.write(myitem[j])

except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason