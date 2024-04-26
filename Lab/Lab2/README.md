# Lab2: 比较三种中位数选取算法的效率

## code-代码

* [generator.go](code/generator.go) 随机数生成器，根据输入规模n，提供三种分布的随机数
* [linear_kth.go](code/linear_kth.go) 线性时间选择第k小元素，基于快速排序的思想
* [quick_sort.go](code/quick_sort.go) 快速排序算法
* [random_select.go](code/random_select.go) 参照课件实现随机选择算法。如果对该算法的实现有疑问，请重新查看课件中的介绍。
* [main.go](code/main.go) 主程序，调用上述方法，比较三种算法的效率
* [go.mod](code/go.mod) go module文件，用于管理依赖

> 注意，如果没有必要，不要尝试使用随机选择算法跑zipf分布的数据。在笔者的机器上，数据规模超过五百基本上栈就会爆掉。
> 除此之外，随机选择算法的效率和参数的选择有关，如果参数选择不当，可能会导致算法效率极低。如果实验要求改变参数，可以自行修改代码。

## report-报告

* 暂不提供，有需要可以联系笔者

## README

本文件
