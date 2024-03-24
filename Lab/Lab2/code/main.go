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

	nums := genNums(n)

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

	// 随机选择

	if n >= 3 {
		epochCnt := 0
		start3 := time.Now()
		if n%2 == 0 {
			// 偶数个元素
			rs1 := randomSel{nums: nums, k: n / 2, epoch: 1}
			rs2 := randomSel{nums: nums, k: n/2 + 1, epoch: 1}
			fmt.Println("Median:", float64(rs1.sort()+rs2.sort())/2)
			epochCnt = rs1.epoch + rs2.epoch
		} else {
			// 奇数个元素
			rs := randomSel{nums: nums, k: (n + 1) / 2, epoch: 1}
			fmt.Println("Median:", float64(rs.sort()))
			epochCnt = rs.epoch
		}
		end3 := time.Now()
		fmt.Println("随机选择耗时：", end3.Sub(start3))
		fmt.Println("随机选择递归次数：", epochCnt)
	} else {
		fmt.Println("随机选择需要n>=3")
	}

	//fmt.Println("After sort:", nums)
}
