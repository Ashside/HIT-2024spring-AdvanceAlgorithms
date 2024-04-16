import numpy as np
import pandas as pd


class WeightCalculator:
    """
    根据指定的方法和关系计算权重。
    ...

    属性
    ----------
    method : str
        一个字符串，表示用于计算权重的方法
    relations : list
        一个列表，包含需要计算权重的关系，每个关系都是一个DataFrame
    weights : list
        一个列表，用于存储计算出的权重，每个权重都是一个numpy数组

    方法
    -------
    RS():
        所有元组的权重都是1。
    EW():
        一个特定的权重计算方法的占位符。
    EO():
        一个特定的权重计算方法的占位符。
    OE():
        一个特定的权重计算方法的占位符。
    calc_weights():
        根据'method'属性调用适当的权重计算方法。
    """

    def __init__(self, method: str, relations: list[pd.DataFrame]):
        """
        构造WeightCalculator对象所需的所有必要属性。

        参数
        ----------
            method : str
                一个字符串，表示用于计算权重的方法
            relations : list
                一个列表，包含需要计算权重的关系
        """
        self.method = method
        self.relations = relations
        self.weights = []
        self.join_key = None

        self.get_join_key()
        self.add_weight_column()

    def get_join_key(self):
        """
        从关系中获取连接键。
        硬编码方法，只支持两个关系建立在一个连接键上。
        """
        if self.join_key is None:
            # 获取关系中的列名
            columns1 = self.relations[0].columns
            # 获取第二个关系中的列名
            columns2 = self.relations[1].columns
            # 返回两个关系中的列名的交集，检查是否有相同的列名
            try:
                self.join_key = list(set(columns1) & set(columns2))[0]
            except IndexError:
                print("No common column found")
                return None

        return self.join_key

    def add_weight_column(self):
        """
        为每个关系添加一个权重列。
        """
        for relation in self.relations:
            relation['weight'] = np.ones(len(relation))  # 初始化权重为1
        return self.relations

    def RS(self):
        """
        所有元组的权重都是1。
        """
        for relation in self.relations:
            relation['weight'] = np.ones(len(relation))

        __weights = [relation['weight'].values for relation in self.relations]
        self.weights = __weights
        return self.weights

    def EW(self):
        """
        一个特定的权重计算方法的占位符。
        """
        __weights = [self.relations[-1]['weight'].values]
        # 倒序向前计算权重
        for i in range(len(self.relations) - 2, -1, -1):
            __relation1 = self.relations[i]
            __relation2 = self.relations[i + 1]

            __relation2_group = __relation2.groupby(self.join_key)

            __relation1['weight'] = __relation1[self.join_key].apply(
                lambda x: __relation2_group.get_group(x)['weight'].sum() if x in __relation2_group.groups else 0)

            self.relations[i] = __relation1
            __weights.insert(0, __relation1['weight'].values)
        return __weights

    def EO(self):
        """
        表中度最大的元组的权重就是这个表中所有元组的权重
        """
        __weights = [self.relations[-1]['weight'].values]
        for i in range(len(self.relations) - 2, -1, -1):
            __relation1 = self.relations[i]
            __relation2 = self.relations[i + 1]

            __relation2_group = __relation2.groupby(self.join_key)

            # 获取每个组的元组数
            __relation2_group_count = __relation2_group.size()
            # 获取最大的组
            __max_group = __relation2_group_count.idxmax()
            # 获取最大组的权重
            __max_weight = __relation2_group.get_group(__max_group)['weight'].sum()

            __relation1['weight'] = __relation1[self.join_key].apply(
                lambda x: __max_weight)

            self.relations[i] = __relation1
            __weights.insert(0, __relation1['weight'].values)
        return __weights

    def OE(self):
        """
        一个特定的权重计算方法的占位符。
        """
        return self.weights

    def calc_weights(self):
        """
        根据'method'属性调用适当的权重计算方法。

        如果找不到方法，它会打印"Method not found"。
        """
        if self.method == "RS":
            print("RS")
            return self.RS()
        elif self.method == "EW":
            print("EW")
            return self.EW()
        elif self.method == "EO":
            print("EO")
            return self.EO()
        elif self.method == "OE":
            print("OE")
            return self.OE()
        else:
            print("Method not found")
