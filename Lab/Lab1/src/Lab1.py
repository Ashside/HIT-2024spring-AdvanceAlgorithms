class DataCollector:
    def __init__(self):
        self.data = []

    def collect(self, data):
        self.data.append(data)

    def get_data(self):
        return self.data


