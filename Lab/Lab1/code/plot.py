import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Plot:
    def __init__(self):
        self.switcher = {
            0: 'AOL',
            1: 'Booking',
            2: 'Kosarak',
        }
    # 读取数据
    def read_data(self):
        _data = pd.read_csv('../result/compare.csv', header=None)
        return _data





    def plot_acc(self):
        data = self.read_data()
        groups = data.groupby(data.iloc[:, 1])
        plt.figure(figsize=(10, 6))
        # 对每个组绘制折线图
        for name, group in groups:
            plt.plot(group.iloc[:, 0], group.iloc[:, 2], label=f'{self.switcher[name]}')
        plt.ylabel('accuracy')  # 设置y轴标签
        plt.xlabel('hash numbers')  # 设置x轴标签
        plt.legend()
        plt.show()


    def plot_time(self):
        data = self.read_data()
        groups = data.groupby(data.iloc[:, 1])
        plt.figure(figsize=(10, 6))
        # 对每个组绘制折线图
        for name, group in groups:
            plt.plot(group.iloc[:, 0], group.iloc[:, 3] - group.iloc[:, 4], label=f'{self.switcher[name]}')
        plt.ylabel('time difference')  # 设置y轴标签
        plt.xlabel('hash numbers')  # 设置x轴标签
        plt.legend()
        plt.show()


    def plot_both(self):
        data = self.read_data()
        groups = data.groupby(data.iloc[:, 1])

        fig, ax1 = plt.subplots(figsize=(10, 6))

        # 对每个组绘制折线图
        for name, group in groups:
            ax1.plot(group.iloc[:, 0], group.iloc[:, 2], label=f'{self.switcher[name]} accuracy')

        ax1.set_ylabel('accuracy')  # 设置y轴标签
        ax1.set_xlabel('hash numbers')  # 设置x轴标签
        ax1.legend(loc='upper left')

        ax2 = ax1.twinx()  # 创建第二个y轴

        # 对每个组绘制折线图
        for name, group in groups:
            ax2.plot(group.iloc[:, 0], group.iloc[:, 3] - group.iloc[:, 4], label=f'{self.switcher[name]} time difference',
                     linestyle='--')

        ax2.set_ylabel('time difference')  # 设置第二个y轴标签
        ax2.legend(loc='upper right')

        plt.show()


if __name__ == '__main__':
    Plot().plot_both()
