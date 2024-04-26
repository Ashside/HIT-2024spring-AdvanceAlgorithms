# Lab4-大数据抽样

## code-代码

* [SampleUtils.py](code/SampleUtils.py) 实现了对于基于权重对相邻两个关系进行抽样并连接的算法。更详细的说明可以查看代码中的注释。
* [WeightUtils.py](code/WeightUtils.py) 基于论文中的算法实现了对于权重的计算。其中EW,EO方法基本正确；RS方法对数据集的要求较高，如果该方法不适用，或者与期望结果不符合，可以尝试调整数据集；OE方法对于游走的次数有一定的要求，笔者这里不是很理解论文中的算法，所以实现的效果可能不是很好。
* [PlotUtils.py](code/PlotUtils.py) 可视化结果，效果不是很明显，可以尝试调整参数，比如增加抽样的步数。笔者这里的数据需要手动给出，可以自行修改代码读入数据。
* [main.py](code/main.py) 主程序，调用上述方法，计算权重并可视化结果。

## data-数据

* [data.db](data/data.db) 来自[【论文精读】《Random Sampling over Joins Revisited》](https://zhuanlan.zhihu.com/p/537521956)

## refer-参考文献

* [【论文精读】《Random Sampling over Joins Revisited》](https://zhuanlan.zhihu.com/p/537521956)
* [原论文](<refer/reading ch7 Random Sampling over joins Revisited SIGMOD 2018.pdf>)

## report-报告

* 暂不提供，有需要可以联系笔者

## README

本文件
