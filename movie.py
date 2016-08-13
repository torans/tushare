#coding:utf-8

import tushare as ts
from sqlalchemy import create_engine,insert

df = ts.realtime_boxoffice()    #获取实时电影票房数据，30分钟更新一次票房数据
engine = create_engine('mysql://root:root@127.0.0.1/tushare?charset=utf8')
df.to_sql('movie_data',engine)
print df