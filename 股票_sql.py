import tushare as ts
import pandas as pd
from sqlalchemy import create_engine
#查询出该股票的所有信息
df = ts.get_hist_data('000875')
#连接数据库
engine = create_engine('mysql+mysqlconnector://root:1@localhost/test?charset=utf8')
#导入导数据库
df.to_sql('tick_data',engine,if_exists='append')


