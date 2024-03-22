import sys

from collector import Collector
from tqdm import tqdm

from numba import jit


@jit(nopython=True)
def calc_similarity(set1, set2):
    """
    计算两个集合的相似度
    :param set1:
    :param set2:
    :return:
    调用关系
    calc_similarity_all
    """

    union = len(set1.union(set2))
    inter = len(set1.intersection(set2))
    similarity = float(inter / union)
    return similarity


class Naive:
    """
    用于计算naive similarity
    :param __collect: 数据收集器
    :param __bound: 相似度的阈值
    调用关系
    main.py -> write_naive -> Naive
    """

    def __init__(self, __collect, __bound=0.9):
        collector = __collect
        self.map = collector.get_map()
        self.set_ids = collector.get_keys()
        self.all_values = collector.get_all_values()
        self.bound = __bound

    def calc_similarity_all(self):
        similarity_all = []
        for i in tqdm(range(len(self.set_ids)), file=sys.stdout, desc='Calculating naive similarity'):
            set1 = set(self.map[self.set_ids[i]])
            id1 = self.set_ids[i]
            for j in range(i + 1, len(self.set_ids)):
                set2 = set(self.map[self.set_ids[j]])
                id2 = self.set_ids[j]
                similarity = calc_similarity(set1, set2)
                if similarity >= self.bound:
                    similarity_all.append(f"{id1}\t{id2}")
        return similarity_all
