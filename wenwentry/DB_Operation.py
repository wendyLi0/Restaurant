# coding=UTF-8

# 导入:
import json
import random

import sys
from flask import jsonify
from sqlalchemy import Column, String, create_engine
from sqlalchemy import Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import DeclarativeMeta

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class Restaurant(Base):
    # 表的名字:
    __tablename__ = 'restaurant'

    # 表的结构:
    id = id = Column(Integer, primary_key=True)
    restaurant_name = Column(String(100))
    restaurant_address = Column(String(300))

def add_restaurant(requestjson):
    # 解析请求的json
    cantingName = requestjson['cantingName']
    cantingAddress = requestjson['cantingAddress']

    # 初始化数据库连接:
    engine = create_engine('mysql+mysqlconnector://root:wdbuyer@10.1.101.161:3306/wenwenTest')

    # 创建对应column
    # Base.metadata.create_all(engine)

    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)

    # 创建session对象:
    session = DBSession()
    # 创建新表对象:
    new_user = Restaurant(restaurant_name=cantingName, restaurant_address=cantingAddress)
    # 添加到session:
    session.add(new_user)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()

def get_restaurant(encode):
    engine = create_engine("mysql+mysqlconnector://root:wdbuyer@10.1.101.161:3306/wenwenTest")
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    result = session.query(Restaurant.restaurant_name, Restaurant.restaurant_address).all()
    session.close()
    if(encode == 'true'):
        obj = []
        for item in result:
            _obj = {}
            _obj["cantingName"] = item[0]
            _obj["cantingAddress"] = item[1]
            obj.append(_obj)
        return obj
    elif(encode=='false'):
        obj = []
        i = random.randint(0, len(result)-1)
        _obj = {}
        _obj["cantingName"] = result[i][0]
        _obj["cantingAddress"] = result[i][1]
        obj.append(_obj)
        return obj

print sys.path[0]
#
# aa=get_restaurant('false')
# print aa
# for i in aa.all():
#     print i

