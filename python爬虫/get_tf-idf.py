#coding=utf-8

import math
import json

t=0
Dict_idf ={}
Dict_tf = {}

DicList =[]

for j in range(10):
  f_name = str(j+1)+'.txt'
  f = open(f_name)
  mystr = f.read()
  f.close()
  #print mystr.__len__()
  len = mystr.__len__()

  #print len
  str_p = ""

  myarticle = []
  for i in range(len):
    if mystr[i]=='.' or mystr[i]==',':
      if i<len-1 and mystr[i+1]>='0' and mystr[i+1]<='9':
        str_p = str_p.__add__(mystr[i])
      elif str_p=="":
        continue
      else:
        #print str_p
        myarticle.append(str_p)
        str_p=""
    elif mystr[i]=='(' or mystr[i]==')' or mystr[i]==' ' or mystr[i]=='"':
      if str_p == "":
        continue
      else:
        #print str_p
        myarticle.append(str_p)
        str_p = ""
    else:
      str_p = str_p.__add__(mystr[i])

  #print myarticle.__len__()
  Dict_tf = {}
  for i in range(myarticle.__len__()):
    if not Dict_tf.has_key(myarticle[i]):
      Dict_tf[myarticle[i]] =1.0
      if not Dict_idf.has_key(myarticle[i]):
        Dict_idf[myarticle[i]] =1.0
      else:
        Dict_idf[myarticle[i]] +=1.0
    else:
      Dict_tf[myarticle[i]] +=1.0
    #print myarticle[i],Dict_tf[myarticle[i]]
  #print Dict_tf.__len__()
  DicList.append(Dict_tf)
  for k,v in Dict_tf.items():
    Dict_tf[k] = Dict_tf[k]/myarticle.__len__()
  #for k, v in Dict_tf.items():
    #print k,v
for k,v in Dict_idf.items():
  Dict_idf[k] = math.log(10.0/Dict_idf[k])
#for k,v in Dict_idf.items():
  #print k,v

res = ""
res = res.__add__("{")
res = res.__add__("\n")
res = res.__add__("\t[\n")

for j in range(10):
  Dictf_idf = DicList[j]
  for k,v in Dictf_idf.items():
    Dictf_idf[k] = Dictf_idf[k]*Dict_idf[k]

  Dictf_idf = sorted(Dictf_idf.iteritems(), key=lambda d: d[1], reverse=True)

  f_name = str(j+1)+'.txt'
  f = open(f_name)
  mystr = f.read()
  f.close()

  mytitle=""


  data= {}



  for i in range(mystr.__len__()):
    if mystr[i]=='\n':
      #print mytitle
      res = res.__add__("\t\tarticle_titile:\"")
      res = res.__add__(mytitle)
      res = res.__add__("\"\n")
      res = res.__add__("\t\t[\n")

      for tt in range(10):
        res = res.__add__("\t\t\t{\n")
        res = res.__add__("\t\t\t\tword:\"")
        res = res.__add__(Dictf_idf[tt][0])
        res = res.__add__("\"\n")
        res = res.__add__("\t\t\t\tvalue:")
        res = res.__add__(str(Dictf_idf[tt][1]))
        res = res.__add__("\n")
        res = res.__add__("\t\t\t}\n")
      res = res.__add__("\t\t]\n")

    else:
      mytitle = mytitle.__add__(mystr[i])

res = res.__add__("\t]\n")
res = res.__add__("}")
#print res

changeflie = 'tf-idf.txt'
fp = open(changeflie,'w+')
fp.write(res)
fp.close()

fp = open(changeflie)
myres = fp.read()
fp.close()


file = 'my.json'
fp = open(file,'w+')
fp.write(json.dumps(res))
fp.close()
