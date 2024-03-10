class Collector:
    def __init__(self, __text_sel=3):

        self.map = {}
        switcher = {
            0: '../data/E1_AOL-out.txt',
            1: '../data/E1_Booking-out.txt',
            2: '../data/E1_kosarak_100k.txt',
            3: '../data/test.txt',
        }
        self.path = switcher.get(__text_sel, '../data/E1_AOL-out.txt')

        self.data = self.read()
        self._make_data()

    def read(self):
        try:
            with open(self.path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print("File not found")
            return None

    def _make_data(self):
        for line in self.data.split('\n'):
            # 跳过空行
            if len(line) == 0:
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
        print('Data has been read successfully')

    def get_data(self):
        return self.map

    def get_keys(self) -> list:
        return list(self.map.keys())

    def get_all_values(self):
        all_values = []
        for values in self.map.values():
            all_values.extend(values)
        # 去重
        all_values = list(set(all_values))
        return all_values
