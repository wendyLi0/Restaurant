# coding=UTF-8

# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class Restaurant(Base):
    # 表的名字:
    __tablename__ = 'restaurant'

    # 表的结构:
    id=Column(String(20),primary_key=True)
    restaurant_name = Column(String(100))
    restaurant_address = Column(String(300))


#解析请求的json
# cantingName=requestjson['cantingName'],
# cantingAddress=requestjson['cantingAddress']
# print cantingName,cantingAddress

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:wdbuyer@10.1.101.161:3306/wenwenTest')

# 创建对应column
Base.metadata.create_all(engine)

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# 创建对应column
Base.metadata.create_all(engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_Restaurant = Restaurant(id='5',restaurant_name='11', restaurant_address='22')
# 添加到session:
session.add(new_Restaurant)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()