import sqlite3
import os
import pandas as pd
from SampleUtils import SampleUtils
from WeightUtils import WeightCalculator
from SqlUtils import *

methods = ['RS', 'EW', 'EO', 'OE']
if __name__ == '__main__':
    # 创建数据库连接
    conn = sqlite3.connect('../data/small_data.db')
    # 创建游标
    cursor = conn.cursor()
    # 读取Twitter_user表
    cursor.execute("SELECT * FROM Twitter_user")
    Twitter_user = cursor.fetchall()
    # 读取userLike表
    cursor.execute("SELECT * FROM userLike")
    userLike = cursor.fetchall()

    # 将Twitter_user和userLike转换为DataFrame
    Twitter_user = pd.DataFrame(Twitter_user, columns=['source', 'destination'])
    userLike = pd.DataFrame(userLike, columns=['source', 'like1', 'like2', 'like3', 'like4', 'like5'])

    # 连接Twitter_user和userLike
    join_key = 'source'

    cur_method = methods[2]
    # 计算权重
    weight_calculator = WeightCalculator(cur_method, [Twitter_user, Twitter_user, Twitter_user])
    ws = weight_calculator.calc_weights()
    print(ws)

    # 连接Twitter_user和userLike
    # result = JOIN(Twitter_user, userLike, weight_Twitter_user, weight_userLike, join_key)
