import numpy as np

from collector import Collector
from minHash import MinHash
from naive import Naive
import time
import pandas as pd

# import matplotlib.pyplot as plt

def write_minHash(_collector, _n_samples, _bound=0.9, _iteration=10):
    # 获取数据
    minHash = MinHash(_collector, _iteration, _bound)
    # 将similarity的结果写入文件
    with open(f'../result/minhash/similarity{_collector.sel}.txt', 'w') as file:
        similarity = minHash.calc_similarity()
        for j in similarity:
            file.write(str(j) + '\n')
    print(f'MinHash Similarity{_collector.sel} has been written successfully')


def write_naive(_collector, _n_samples, _bound=0.9):
    # 获取数据
    naive = Naive(_collector, _bound)
    # 将similarity的结果写入文件
    with open(f'../result/naive/similarity{_collector.sel}.txt', 'w') as file:
        similarity = naive.calc_similarity_all()
        for j in similarity:
            file.write(str(j) + '\n')
    print(f'Naive similarity{_collector.sel} has been written successfully')


def compare_file(_sel, _n_samples):
    # 读取minHash的结果
    _minhash_collector = Collector(_sel, _n_samples, True, True)
    # 读取naive的结果
    _naive_collector = Collector(_sel, _n_samples, True, False)
    # 对比两者的结果
    _minhash_map = _minhash_collector.get_map()
    _naive_map = _naive_collector.get_map()
    _minhash_keys = _minhash_collector.get_keys()
    _naive_keys = _naive_collector.get_keys()

    # 统计minhash的value个数
    minhash_values = 0.0
    for _k in _minhash_keys:
        minhash_values += len(_minhash_map[_k])
    # 统计naive的value个数
    naive_values = 0.0
    for _k in _naive_keys:
        naive_values += len(_naive_map[_k])
    return min(minhash_values, naive_values) / max(minhash_values, naive_values)


if __name__ == '__main__':
    iteration = 10
    bound = 0.7
    text_sel = 0
    n_samples = 500
    acc = {}
    for text_sel in range(3):
        # 获取数据
        collector = Collector(text_sel, n_samples)
        for iteration in range(10, 110, 10):
            # 写入minHash的结果
            t_minhash_start = time.perf_counter()
            write_minHash(collector, n_samples, bound, iteration)
            t_minhash_end = time.perf_counter()
            period_minhash = t_minhash_end - t_minhash_start

            t_naive_start = time.perf_counter()
            # 写入naive的结果
            write_naive(collector, n_samples, bound)
            t_naive_end = time.perf_counter()
            period_naive = t_naive_end - t_naive_start
            # 对比两者的结果
            acc[(iteration, text_sel)] = (compare_file(text_sel, n_samples), period_minhash, period_naive)
    # 写入文件
    with open('../result/compare.csv', 'w') as file:
        for k, v in acc.items():
            file.write(f'{k[0]},{k[1]},{v[0]},{v[1]},{v[2]}\n')
    print('Compare file has been written successfully')
