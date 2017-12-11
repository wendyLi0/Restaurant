# coding=UTF-8

# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String


# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'restaurant2'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    restaurant_name = Column(String(100))
    restaurant_address = Column(String(300))


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:wdbuyer@10.1.101.161:3306/wenwenTest')
Base.metadata.create_all(engine)

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(restaurant_name='name3',restaurant_address="address3")
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()