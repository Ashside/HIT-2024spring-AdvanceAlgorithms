import random
import sys

from collector import Collector
import numpy as np
import tqdm
import numba
from numba import jit


class MinHash:
    """
    用于计算minHash similarity
    :param __collect: 数据收集器
    :param __iteration: 迭代次数
    :param __bound: 相似度的阈值
    调用关系
    main.py -> write_minHash -> MinHash
    """

    def __init__(self, __collect, __iteration=10, __bound=0.9):
        self.iteration = __iteration
        self.bound = __bound

        collector = __collect
        self.map = collector.get_map()
        self.set_ids = collector.get_keys()
        self.all_values = collector.get_all_values()

    @property
    def number_of_sets(self):
        return len(self.set_ids)

    def get_hash_func(self):
        random.shuffle(self.all_values)

    def calc_minhash(self, set_id: int, hash_values: list):
        """
        计算一个集合的minHash值
        :param set_id:
        :param hash_values:
        :return:
        """
        # hash_values = self.get_hash()
        # NOTE: hash_values应该外部传入

        set_values = self.map[set_id]
        min_hash = float('inf')
        # print(hash_values)
        for i in range(len(hash_values)):
            if hash_values[i] in set_values:
                min_hash = i
                break
        return min_hash

    def calc_all_minhash(self):
        """
        计算所有集合的minHash值
        :return:
        """
        min_hash_values = []
        for set_id in self.set_ids:
            min_hash = self.calc_minhash(set_id, self.all_values)
            min_hash_values.append(min_hash)

        return min_hash_values

    def calc_hash_table(self) -> list:
        """
        计算hash table
        :return:
        """
        hash_table = []
        iteration = self.iteration
        for i in tqdm.tqdm(range(iteration), file=sys.stdout, desc='Calculating hash table'):
            # hash_values = self.get_hash_func()
            self.get_hash_func()  # 重新打乱
            min_hash_values = self.calc_all_minhash() # 计算minHash值 调用calc_all_minhash->calc_minhash
            # print(min_hash_values)
            hash_table.append(min_hash_values)
        return hash_table

    def calc_similarity(self):
        hash_table = self.calc_hash_table()
        similarity = []
        '''
        弃用
        for i in range(len(hash_table)):
            for j in range(i + 1, len(hash_table)):
                count = 0
                for k in range(len(hash_table[i])):
                    if hash_table[i][k] == hash_table[j][k]:
                        count += 1
                similarity.append(count / len(hash_table[i]))
        '''
        row = len(hash_table)
        col = len(hash_table[0])
        for i in tqdm.tqdm(range(col - 1), file=sys.stdout, desc='Calculating minHash similarity'):
            for j in range(i + 1, col):
                count = 0
                for k in range(row):
                    if hash_table[k][i] == hash_table[k][j]:
                        count += 1
                if float(count) / float(row) >= self.bound:
                    # print(f'set {i} and set {j} are similar')
                    similarity.append(f"{self.set_ids[i]}\t{self.set_ids[j]}") # 记录相似的集合

        return similarity

    def __str__(self):
        return f'Number of sets: {self.number_of_sets}\n' \
               f'All values: {self.all_values}\n' \
               f'Set IDs: {self.set_ids}\n'
