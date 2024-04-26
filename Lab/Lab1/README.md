# Lab1: 用minHash实现集合的相似性连接

## code-代码

* `/golang`使用Go语言实现了一部分代码，如果对性能有要求，可以参考该文件夹下的代码
* `collector.py`实现了Collector类，用于从三个文件中读取数据，详细的使用方法可以参考代码中的注释
* `minhash.py`实现了MinHash类，用于计算集合的MinHash值，实现思路基于课件中的介绍。对minHash的思路不熟悉的可以参考`Review/课程复习.md`中的介绍
* `naive.py`使用naive方法计算集合的相似性，用于对比minHash的效果。所谓的naive方法其实就是计算两个集合的交集和并集的比值。
* `plot.py`使用matplotlib绘制了准确率的分布图，可以直观的看到minHash的效果
* `main.py`是主程序，用于调用上述的类和方法，计算集合的相似性

> 值得注意的地方：Collector的实现逻辑比较奇怪，是为了实现“通用读取数据方法”这一目标，实际使用时可以根据自己的需求修改。本质上讲，能读数据就好了。如果不要求做优化，实验一没有什么很复杂的地方。

## data-数据

* [E1_AOL-out.txt](data/E1_AOL-out.txt)
* [E1_Booking-out.txt](data/E1_Booking-out.txt)
* [E1_kosarak_100k.txt](data/E1_kosarak_100k.txt)
* [测试样例](data/test.txt)

## report-报告

* 暂不提供，有需要可以联系笔者

## result-结果

存放代码运行的结果

* `minHash/`
* `naive/`
* `compare.csv`

## README

本文件
