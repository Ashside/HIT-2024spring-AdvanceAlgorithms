package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	var n int
	fmt.Println("Please input the number of elements:")
	_, err := fmt.Scan(&n)
	if err != nil {
		return
	}
	// 生成随机种子
	rand.Seed(time.Now().Unix())
	// 生成随机数组
	nums := make([]int, n)
	for i := range nums {
		nums[i] = rand.Intn(n * 10)
	}
	//fmt.Println("Before sort:", nums)

	// 快速排序
	start1 := time.Now()
	q := quickSort{nums: nums}
	fmt.Println("Median:", q.getMid())
	end1 := time.Now()
	fmt.Println("快速排序耗时：", end1.Sub(start1))

	// 线性时间选择
	start2 := time.Now()
	m := medianFinder{nums: nums}
	fmt.Println("Median:", m.findMedian())
	end2 := time.Now()
	fmt.Println("线性时间选择耗时：", end2.Sub(start2))

	//fmt.Println("After sort:", nums)
}
