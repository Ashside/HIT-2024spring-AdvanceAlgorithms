import sqlite3
import os
import time

import pandas as pd
from SampleUtils import SampleUtils
from WeightUtils import WeightCalculator
import numpy as np

np.seterr(divide='ignore', invalid='ignore')
methods = ['RS', 'EW', 'EO', 'OE']
if __name__ == '__main__':
    # 创建数据库连接
    conn = sqlite3.connect('../data/data.db')
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
    sample_num = [1, 10, 50, 100, 500]
    relations = [Twitter_user, userLike]
    for i in range(4):
        cur_method = methods[i]
        # 计算权重
        __start = time.time()
        weight_calculator = WeightCalculator(cur_method, relations)
        ws = weight_calculator.calc_weights()
        print(f"Method: {cur_method}, Weight Time: {time.time() - __start}")
        for num in sample_num:
            # 采样
            __start_sample = time.time()
            sample_utils = SampleUtils(relations, ws, num)
            sample_res = sample_utils.random_sample()
            print(f"Method: {cur_method}, Sample Num: {num}, Time: {time.time() - __start_sample}")
        print(f"Method: {cur_method}, Total Time: {time.time() - __start}")

    conn.close()
