import numpy as np
from numba import cuda

# 定义一个CUDA核函数
@cuda.jit
def add_kernel(x, y, result):
    idx = cuda.grid(1)
    if idx < x.size:
        result[idx] = x[idx] + y[idx]

def main():
    # 定义输入数据
    N = 10000
    x = np.arange(N).astype(np.float32)
    y = np.arange(N).astype(np.float32)
    result = np.zeros_like(x)

    # 将数据移动到GPU
    x_gpu = cuda.to_device(x)
    y_gpu = cuda.to_device(y)
    result_gpu = cuda.to_device(result)

    # 定义CUDA网格和线程块的大小
    threads_per_block = 256
    blocks_per_grid = (N + threads_per_block - 1) // threads_per_block

    # 调用CUDA核函数
    add_kernel[blocks_per_grid, threads_per_block](x_gpu, y_gpu, result_gpu)

    # 将结果从GPU移回CPU
    result_gpu.copy_to_host(result)

    # 打印结果的前10个元素
    print(result[:10])

if __name__ == '__main__':
    main()
