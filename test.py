#coding:utf-8
from sqlalchemy import create_engine
import tushare as ts

df = ts.get_tick_data('600848', date='2014-12-22')
engine = create_engine('mysql://root:root@127.0.0.1/tushare?charset=utf8')

#存入数据库
df.to_sql('tick_data',engine)

#追加数据到现有表
#df.to_sql('tick_data',engine,if_exists='append')