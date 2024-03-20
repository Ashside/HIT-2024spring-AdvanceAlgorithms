from collector import Collector
from tqdm import tqdm


class Naive:
    """
    用于计算naive similarity
    :param __collect: 数据收集器
    :param __bound: 相似度的阈值
    """
    def __init__(self, __collect, __bound=0.9):
        collector = __collect
        self.map = collector.get_map()
        self.set_ids = collector.get_keys()
        self.all_values = collector.get_all_values()
        self.bound = __bound

    def calc_similarity(self, set1, set2):

        union = len(set1.union(set2))
        inter = len(set1.intersection(set2))
        similarity = float(inter / union)
        return similarity

    def calc_similarity_all(self):
        similarity_all = []
        for i in tqdm(range(len(self.set_ids) - 1), desc='Calculating naive similarity'):
            set1 = set(self.map[self.set_ids[i]])
            id1 = self.set_ids[i]
            for j in range(i + 1, len(self.set_ids)):
                set2 = set(self.map[self.set_ids[j]])
                id2 = self.set_ids[j]
                similarity = self.calc_similarity(set1, set2)
                if similarity >= self.bound:
                    similarity_all.append(f"{id1}\t{id2}")
        return similarity_all
