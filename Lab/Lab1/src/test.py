from collector import Collector
from minHash import MinHash

if __name__ == '__main__':
    minHash = MinHash(10, 0.99, 2)
    # 将similarity的结果写入文件
    with open('../data/similarity.txt', 'w') as file:
        for set_id in minHash.set_ids:
            similarity = minHash.calc_similarity(set_id)
            file.write(f'{set_id} {similarity}\n')
