// Package: main运行入口
package main

import (
	"fmt"
	"time"
)

func main() {
	n, err := getInputNumber()
	if err {
		return // 输入错误
	}

	// 生成均匀分布随机数组
	fmt.Println("Generating uniform random numbers...")
	uniformNums := genUniformNums(n)
	compTime(uniformNums, n)
	fmt.Println("-----------------------------")

	// 生成正态分布随机数组
	fmt.Println("Generating normal random numbers...")
	normalNums := genNormalNums(n)
	compTime(normalNums, n)
	fmt.Println("-----------------------------")

	// 不保证有限时间内结束
	if n <= 500 {
		// 生成Zipf分布随机数组
		fmt.Println("Generating Zipf random numbers...")
		zipfNums := genZipfNums(n)
		compTime(zipfNums, n)
		fmt.Println("-----------------------------")
	}

	//fmt.Println("After selKth:", uniformNums)
}

func compTime(nums []int, n int) {
	// 快速排序
	start1 := time.Now()
	q := quickSort{nums: nums}
	fmt.Println("Median:", q.getMedian())
	end1 := time.Now()
	fmt.Println("快速排序耗时：", end1.Sub(start1))

	// 线性时间选择
	start2 := time.Now()
	m := medianFinder{nums: nums}
	fmt.Println("Median:", m.getMedian())
	end2 := time.Now()
	fmt.Println("线性时间选择耗时：", end2.Sub(start2))

	// 随机选择
	epochCnt := 0
	start3 := time.Now()
	rs := randomSel{nums: nums, k: n / 2, epoch: epochCnt}
	fmt.Println("Median:", rs.getMedian())
	epochCnt = rs.epoch
	end3 := time.Now()
	fmt.Println("随机选择耗时：", end3.Sub(start3))
	fmt.Println("随机选择递归次数：", epochCnt)
}
