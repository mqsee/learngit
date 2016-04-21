#coding=utf-8

import requests
import bs4
import sys
import math
import json
reload(sys)
sys.setdefaultencoding('utf-8')

url_list = ['http://www.chinadaily.com.cn/china/2016-04/20/content_24701635.htm',
            'http://www.chinadaily.com.cn/china/2016-04/20/content_24700746.htm',
            'http://www.chinadaily.com.cn/china/2016-04/20/content_24681482.htm',
            'http://www.chinadaily.com.cn/china/2016-04/19/content_24675530.htm',
            'http://www.chinadaily.com.cn/china/2016-04/19/content_24675455.htm',
            'http://www.chinadaily.com.cn/china/2016-04/19/content_24674074.htm',
            'http://www.chinadaily.com.cn/china/2016-04/19/content_24655536.htm',
            'http://www.chinadaily.com.cn/china/2016-04/18/content_24643685.htm',
            'http://www.chinadaily.com.cn/china/2016-04/18/content_24636917.htm',
            'http://www.chinadaily.com.cn/china/2016-04/15/content_24562198.htm'
            ]

articles_title = []
articles_content = []

for pos,url in enumerate(url_list):
    r = requests.get(url)
    soup1 = bs4.BeautifulSoup(r.text)
    soup2 = bs4.BeautifulSoup(str(soup1.find_all(id="Title_e")))
    articles_title.append(soup2.h1.string)
    mystr = ""
    soup3 = bs4.BeautifulSoup(str(soup1.find_all(id="Content")))
    for x in soup3.find_all("p"):
        mystr = mystr + x.string

    str_p = ""
    contents = []
    for pos,x in enumerate(mystr):
        if x == '.' or x == ',':
            if pos < (len(mystr) - 1) and mystr[pos+1] >= '0' and mystr[pos+1] <= '9':
                str_p = str_p + x
            elif str_p == "":
                continue
            else:
                contents.append(str_p)
                str_p = ""
        elif x == '(' or x == ')' or x == ' ' or x == '"' or x == '[' or x == ']' or x == '-':
            if str_p == "":
                continue
            else:
                contents.append(str_p)
                str_p = ""
        else:
            str_p = str_p + x

    articles_content.append(contents)

Dict_idf = {}
DictList = []

for content in articles_content:
    Dict_tf = {}
    for x in content:
        if not Dict_tf.has_key(x):
            Dict_tf[x] = 1.0
            if not Dict_idf.has_key(x):
                Dict_idf[x] = 1.0
            else:
                Dict_idf[x] += 1.0
        else:
            Dict_tf[x] += 1.0

    for k, v in Dict_tf.items():
        Dict_tf[k] = v / len(content)

    DictList.append(Dict_tf)

for k, v in Dict_idf.items():
    Dict_idf[k] = math.log(float(len(url_list)) / v)

for pos,x in enumerate(DictList):
    for k,v in x.items():
        DictList[pos][k] = v*Dict_idf[k]
    DictList[pos] = sorted(x.iteritems(), key=lambda d: d[1], reverse=True)

"""
[
    [
	    article_titile:"XXXX"
	    [
		    {
		    	word:"hello"
		    	value:3.5
		    }
            {
                word:"hello"
                value:3.5
            }
            {
                word:"hello"
                value:3.5
            }
            ...
        ]
	]
]
"""

data = []
for pos in range(10):
    data2=[]
    data2.append("article_titile:")
    data2.append(articles_title[pos])
    data2.append([{"word": k,"value":round(v,4)} for k,v in DictList[pos][:10]])
    data.append(data2)

# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f)