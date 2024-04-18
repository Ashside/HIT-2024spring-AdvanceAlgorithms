import random
import statistics
import numpy as np

import pandas as pd


class SampleUtils:
    def __init__(self, relations, weights, sample_num: int = 0):
        self.relations = relations
        self.weights = weights
        self.sample_num = sample_num

    def JOIN(self, relation1: pd.DataFrame, relation2: pd.DataFrame, weight1: np.array, weight2: np.array,
             join_key: str) -> pd.DataFrame | None:
        """
        按权重随机抽样relation1,根据join_key连接relation2,并返回连接后的结果
        :param self:
        :param relation1: 关系1，包含A,B两列
        :param relation2: 关系2，包含B,C两列
        :param weight1:  关系1中每个元组的权重
        :param weight2:  关系2中每个元组的权重
        :param join_key:  用于连接的属性
        :return:  连接后的结果
        """
        try:
            # 比较relation1和relation2的权重长度是否相等
            if len(weight1) != len(relation1):
                raise ValueError("The length of weight1 is not equal to the length of relation1")
            if len(weight2) != len(relation2):
                raise ValueError("The length of weight2 is not equal to the length of relation2")
            # 比较relation1和relation2的列名是否相等
            if join_key not in relation1.columns:
                raise ValueError("The join_key is not in relation1")
            if join_key not in relation2.columns:
                raise ValueError("The join_key is not in relation2")
        except ValueError as e:
            print(e)
            return None

        # 为relation1和relation2添加权重列
        relation1['weight'] = weight1
        relation2['weight'] = weight2

        # 为relation添加索引
        relation1 = relation1.set_index(join_key)
        relation2 = relation2.set_index(join_key)
        gruop_relation1 = relation1.groupby(join_key)
        gruop_relation2 = relation2.groupby(join_key)
        # 根据权重随机抽样relation1中的一个元组
        sample1 = relation1.sample(n=1, weights='weight')

        join_attr = sample1.index[0]

        # 根据权重随机抽样relation2中的一个元组
        if join_attr not in gruop_relation2.groups:
            return None
        group2 = gruop_relation2.get_group(join_attr)

        sample2 = group2.sample(n=1, weights='weight')
        # 计算拒绝概率
        reject_prob = 1 - group2['weight'].sum() / sample1['weight'].values[0]

        # 以拒绝概率拒绝或接受relation2中的元组
        if random.random() < reject_prob:
            return None
        else:
            # 删除权重列
            sample1 = sample1.drop(columns='weight')
            sample2 = sample2.drop(columns='weight')
            # 将两个元组连接
            result = pd.concat([sample1, sample2], axis=1)
            # 删除索引
            result = result.reset_index()
            return result

    def random_sample(self):
        # 选择一条随机游走路径
        samples = []
        for it in range(self.sample_num):

            # 调用JOIN函数连接relation1和relation2
            for i in range(len(self.relations) - 1):
                relation1 = self.relations[i]
                relation2 = self.relations[i + 1]
                weight1 = self.weights[i]
                weight2 = self.weights[i + 1]
                join_key = 'source'
                sample = self.JOIN(relation1, relation2, weight1, weight2, join_key)
                if sample is not None:
                    samples.append(sample)
                else:
                    break

        return samples
