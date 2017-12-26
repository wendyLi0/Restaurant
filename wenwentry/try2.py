# coding=UTF-8

# 导入:
import json

from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#构造字典
python2json = {}
#构造list
listData = [(u'11', u'22'), (u'testname111', u'testaddress111')]
for item in listData:
    python2json[item[0]] = item[1]


#转换成json字符串
json_str = json.dumps(python2json)
print json_str
print type(json_str)



obj = []
for t in listData:
    _obj = {}
    _obj["name"]=t[0]
    _obj["address"]=t[1]
    obj.append(_obj)
print