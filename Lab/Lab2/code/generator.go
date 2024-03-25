package main

import (
	"fmt"
	"math/rand"
	"time"
)

// genNums 生成随机数组
func genNums(n int) []int {
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
