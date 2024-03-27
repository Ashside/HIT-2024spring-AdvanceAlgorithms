package main

import (
	"fmt"
	"math"
	"math/rand"
	"time"
)

// genZipfNums 生成Zipf分布随机数组
func genZipfNums(n int) []int {
	rand.Seed(time.Now().Unix())
	zipf := rand.NewZipf(rand.New(rand.NewSource(time.Now().Unix())), 2, 1, math.MaxUint32)
	nums := make([]int, n)
	for i := range nums {
		nums[i] = int(zipf.Uint64())
	}
	fmt.Println("Generate successfully")
	//fmt.Println(nums)
	return nums
}

// genNormalNums 生成正态分布随机数组
func genNormalNums(n int) []int {
	// 生成随机种子
	rand.Seed(time.Now().Unix())
	// 生成随机数组
	nums := make([]int, n)
	for i := range nums {
		nums[i] = int(rand.NormFloat64() * float64(n) / 2)
	}
	fmt.Println("Generate successfully")
	return nums

}

// genUniformNums 生成随机数组
func genUniformNums(n int) []int {
	// 生成随机种子
	rand.Seed(time.Now().Unix())
	// 生成随机数组
	nums := make([]int, n)
	for i := range nums {
		nums[i] = rand.Intn(n * 10)
	}
	fmt.Println("Generate successfully")
	return nums
}

// getInputNumber 获取输入的数字
func getInputNumber() (int, bool) {
	var n int
	fmt.Println("Please input the number of elements:")
	_, err := fmt.Scan(&n)
	if err != nil {
		return 0, true
	}
	if n <= 0 {
		fmt.Println("input should be a positive integer.")
		return 0, true
	}
	return n, false
}
