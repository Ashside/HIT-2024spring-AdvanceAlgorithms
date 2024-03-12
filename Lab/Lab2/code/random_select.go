package main

import (
	"math"
	"math/rand"
	"sort"
	"time"
)

func rank(x int, nums []int) int {
	rank := 0
	for _, num := range nums {
		if num < x {
			rank++
		}
	}
	return rank
}

type randomSel struct {
	nums  []int
	k     int // 第 k 小的元素
	epoch int // 递归次数
}

func (rs *randomSel) selectRandomElements(numElements int) []int {

	// 使用当前时间作为随机种子
	rand.Seed(time.Now().UnixNano())

	// 创建一个映射来跟踪已经选择的索引
	selectedIndices := make(map[int]bool)
	selectedElements := make([]int, numElements)

	// 从数组中选择指定数量的元素
	for i := 0; i < numElements; {
		// 生成随机索引
		randomIndex := rand.Intn(len(rs.nums))

		// 如果索引未被选择，则将其添加到已选择的索引列表中
		if !selectedIndices[randomIndex] {
			selectedIndices[randomIndex] = true
			selectedElements[i] = rs.nums[randomIndex]
			i++
		}
	}

	return selectedElements
}

func (rs *randomSel) sort() int {
	n := len(rs.nums)
	selNums := rs.selectRandomElements(int(math.Pow(float64(n), 0.75)))

	// 快速排序
	sort.Ints(selNums)

	// 理论上的kth数在排序后的数组中的索引
	x := float64(rs.k) * math.Pow(float64(n), -0.25)

	// 考察上下边界
	left := math.Max(math.Floor(x-math.Pow(float64(n), 0.5)), 0)
	right := math.Min(math.Floor(x+math.Pow(float64(n), 0.5)), float64(len(selNums)-1))

	// 在有序数组中找到第l,h小的元素
	L := selNums[int(left)]
	H := selNums[int(right)]

	// 计算rank
	Lp := rank(L, rs.nums)
	Hp := rank(H, rs.nums)

	// 收集原数组中介于L和H之间的元素
	var P []int
	for _, num := range rs.nums {
		if num >= L && num <= H {
			P = append(P, num)
		}

	}

	// 判断
	if Lp <= rs.k && rs.k <= Hp && float64(len(P)) <= 4*(math.Pow(float64(n), 0.75))+1 {
		sort.Ints(P)
		return P[rs.k-Lp-1] // 返回第k - Lp 小的元素，注意索引偏移
	} else {
		rs.epoch++
		return rs.sort()
	}

}
