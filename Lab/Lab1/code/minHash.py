import random
from collector import Collector
import numpy as np
import tqdm


class MinHash:
    def __init__(self, __iteration=10, __bound=0.9, __text_sel=3):
        self.map = {}
        self.set_ids = []
        self.all_values = []
        self.iteration = __iteration
        self.bound = __bound
        self.text_sel = __text_sel
        self._pre_process()

    def _pre_process(self):
        # FIXME: 1. 从Collector中获取数据
        """texts = ['../data/E1_AOL-out.txt',
                 '../data/E1_Booking-out.txt',
                 '../data/E1_kosarak_100k.txt']
        text = '../data/test.txt'"""
        collector = Collector(self.text_sel)
        self.map = collector.get_data()
        self.set_ids = collector.get_keys()
        self.all_values = collector.get_all_values()

    @property
    def number_of_sets(self):
        return len(self.set_ids)

    def get_hash(self):
        # 返回一个打乱顺序的all_values
        return random.sample(self.all_values, len(self.all_values))

    def calc_minhash(self, set_id: int, hash_values: list):
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

    def calc_all_minhash(self, hash_values: list):
        min_hash_values = []
        for set_id in self.set_ids:
            min_hash = self.calc_minhash(set_id, hash_values)
            min_hash_values.append(min_hash)

        return min_hash_values

    def calc_hash_table(self) -> list:
        hash_table = []
        iteration = self.iteration
        for i in tqdm.tqdm(range(iteration), desc='Calculating hash table'):
            hash_values = self.get_hash()
            min_hash_values = self.calc_all_minhash(hash_values)
            # print(min_hash_values)
            hash_table.append(min_hash_values)
        return hash_table

    def calc_similarity(self):
        hash_table = self.calc_hash_table()
        similarity = []
        '''for i in range(len(hash_table)):
            for j in range(i + 1, len(hash_table)):
                count = 0
                for k in range(len(hash_table[i])):
                    if hash_table[i][k] == hash_table[j][k]:
                        count += 1
                similarity.append(count / len(hash_table[i]))'''
        row = len(hash_table)
        col = len(hash_table[0])
        for i in tqdm.tqdm(range(col-1), desc='Calculating similarity'):
            for j in range(i + 1, col):
                count = 0
                for k in range(row):
                    if hash_table[k][i] == hash_table[k][j]:
                        count += 1
                if float(count / row) >= self.bound:
                    # print(f'set {i} and set {j} are similar')
                    similarity.append((self.set_ids[i], self.set_ids[j], count / row))

        return similarity

    def __str__(self):
        return f'Number of sets: {self.number_of_sets}\n' \
               f'All values: {self.all_values}\n' \
               f'Set IDs: {self.set_ids}\n'
