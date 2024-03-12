from collector import Collector
from minHash import MinHash
from naive import Naive


def write_minHash(sel: int = 3):
    # 获取数据
    minHash = MinHash(10, 0.9, sel)
    # 将similarity的结果写入文件
    with open(f'../result/minhash/similarity{sel}.txt', 'w') as file:
        similarity = minHash.calc_similarity()
        for j in similarity:
            file.write(str(j) + '\n')
    print(f'Similarity{sel} has been written successfully')


def write_naive(sel: int = 3):
    # 获取数据
    naive = Naive(0.9, sel)
    # 将similarity的结果写入文件
    with open(f'../result/naive/similarity{sel}.txt', 'w') as file:
        similarity = naive.calc_similarity_all()
        for j in similarity:
            file.write(str(j) + '\n')
    print(f'Similarity{sel} has been written successfully')


if __name__ == '__main__':
    # 获取数据
    write_naive(2)
    print('All similarity has been written successfully')
