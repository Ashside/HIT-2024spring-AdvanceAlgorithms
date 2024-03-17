import random


class Collector:
    def __init__(self, __text_sel=3, __n_samples=1000,__get_compares=False,__get_minhash=False):

        self.map = {}
        self.get_compares = __get_compares
        switcher_data = {
            0: '../data/E1_AOL-out.txt',
            1: '../data/E1_Booking-out.txt',
            2: '../data/E1_kosarak_100k.txt',
            3: '../data/test.txt',
        }
        switcher_minhash_compare = {
            0: '../result/minhash/similarity0.txt',
            1: '../result/minhash/similarity1.txt',
            2: '../result/minhash/similarity2.txt',
            3: '../result/minhash/similarity3.txt',
        }
        switcher_naive_compare = {
            0: '../result/naive/similarity0.txt',
            1: '../result/naive/similarity1.txt',
            2: '../result/naive/similarity2.txt',
            3: '../result/naive/similarity3.txt',
        }
        if __get_compares:
            if __get_minhash:
                self.path = switcher_minhash_compare.get(__text_sel, '../result/minhash/similarity0.txt')
            else:
                self.path = switcher_naive_compare.get(__text_sel, '../result/naive/similarity0.txt')
        else:
            self.path = switcher_data.get(__text_sel, '../data/E1_AOL-out.txt')
        self.sel = __text_sel

        self.data = self.read()
        self._make_data()
        self._select_n_samples(__n_samples)

    def read(self):
        try:
            with open(self.path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"{self.path} file not found")
            return None

    def _make_data(self):
        for line in self.data.split('\n'):
            # 跳过空行
            if len(line) == 0:
                continue
            # 如果不是以制表符分隔的两个数字，跳过
            if len(line.split('\t')) != 2:
                continue
            items = line.split('\t')
            # print(items)
            set_id = int(items[0])
            set_item = int(items[1])
            if set_id in self.map:
                if set_item not in self.map[set_id]:
                    # NOTE: 确实会有重复的数据
                    self.map[set_id].append(set_item)
            else:
                self.map[set_id] = [set_item]
        if not self.get_compares:
            print('Data has been read successfully')

    def _select_n_samples(self, n_samples):
        # 从map中随机选取n_samples个数据
        keys = list(self.map.keys())
        random.shuffle(keys)
        self.map = {key: self.map[key] for key in keys[:n_samples]}
        if not self.get_compares:
            print(f'{n_samples} samples have been selected successfully')

    def get_map(self):
        return self.map

    def get_keys(self) -> list:
        return list(self.map.keys())

    def get_all_values(self):
        # 获取所有的values
        all_values = []
        for values in self.map.values():
            all_values.extend(values)
        # 去重
        all_values = list(set(all_values))
        return all_values
