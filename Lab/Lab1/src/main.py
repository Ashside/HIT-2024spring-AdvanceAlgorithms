from collector import Collector
from minHash import MinHash


def write(sel: int = 3):
    # 获取数据
    minHash = MinHash(10, 0.9, sel)
    # 将similarity的结果写入文件
    with open(f'../result/similarity{sel}.txt', 'w') as file:
        similarity = minHash.calc_similarity()
        for j in similarity:
            file.write(str(j) + '\n')
    print(f'Similarity{sel} has been written successfully')


if __name__ == '__main__':
    for i in range(4):
        write(i)
    print('All similarity has been written successfully')