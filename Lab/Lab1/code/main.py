from collector import Collector
from minHash import MinHash
from naive import Naive


def write_minHash(_collector, _n_samples, _bound=0.9, _iteration=10):
    # 获取数据
    minHash = MinHash(_collector, _iteration, _bound)
    # 将similarity的结果写入文件
    with open(f'../result/minhash/similarity{_collector.sel}.txt', 'w') as file:
        similarity = minHash.calc_similarity()
        for j in similarity:
            file.write(str(j) + '\n')
    print(f'MinHash Similarity{_collector.sel} has been written successfully')


def write_naive(_collector, _n_samples, _bound=0.9):
    # 获取数据
    naive = Naive(_collector, _bound)
    # 将similarity的结果写入文件
    with open(f'../result/naive/similarity{_collector.sel}.txt', 'w') as file:
        similarity = naive.calc_similarity_all()
        for j in similarity:
            file.write(str(j) + '\n')
    print(f'Naive similarity{_collector.sel} has been written successfully')


def compare_file(_sel, _n_samples):
    # 读取minHash的结果
    _minhash_collector = Collector(_sel, _n_samples, True, True)
    # 读取naive的结果
    _naive_collector = Collector(_sel, _n_samples, True, False)
    # 对比两者的结果
    _minhash_map = _minhash_collector.get_map()
    _naive_map = _naive_collector.get_map()
    _minhash_keys = _minhash_collector.get_keys()
    _naive_keys = _naive_collector.get_keys()

    _cnt = 0
    # 对比两者的结果
    for i in range(max(len(_minhash_keys), len(_naive_keys))):
        if i < len(_minhash_keys) and i < len(_naive_keys):
            if _minhash_map[_minhash_keys[i]] != _naive_map[_naive_keys[i]]:
                _cnt += 1
        elif i < len(_minhash_keys):
            _cnt += 1
        elif i < len(_naive_keys):
            _cnt += 1

    if _cnt > 0:
        print(f'{float(_cnt) / len(_minhash_keys) * 100}% data are different')
    else:
        print('All data are the same')


if __name__ == '__main__':
    iteration = 100
    bound = 0.99
    text_sel = 0
    n_samples = 1000
    for text_sel in range(3):
        # 获取数据
        collector = Collector(text_sel, n_samples)
        # 写入minHash的结果
        write_minHash(collector, n_samples, bound, iteration)
        # 写入naive的结果
        write_naive(collector, n_samples, bound)

        # 对比两者的结果
        compare_file(text_sel, n_samples)
