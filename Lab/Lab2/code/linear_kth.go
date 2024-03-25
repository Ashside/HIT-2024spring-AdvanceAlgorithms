package main

import (
	"math/rand"
)

type medianFinder struct {
	nums []int
}

// getMedian 查找中位数
func (m *medianFinder) getMedian() float64 {
	length := len(m.nums)
	//rand.Seed(time.Now().Unix())
	if length%2 == 0 {
		return float64(m.findKth(0, length-1, length/2)+m.findKth(0, length-1, length/2+1)) / 2.0
	} else {
		return float64(m.findKth(0, length-1, (length+1)/2))
	}
}

// findKth 查找第k小的元素
func (m *medianFinder) findKth(left, right, k int) int {
	if left == right {
		return m.nums[left]
	}
	pivotIndex := m.partition(left, right)
	if k == pivotIndex+1 {
		return m.nums[pivotIndex]
	} else if k < pivotIndex+1 {
		return m.findKth(left, pivotIndex-1, k)
	} else {
		return m.findKth(pivotIndex+1, right, k)
	}
}

// partition 分区
func (m *medianFinder) partition(left, right int) int {
	pivotIndex := rand.Intn(right-left+1) + left
	pivot := m.nums[pivotIndex]
	m.nums[pivotIndex], m.nums[right] = m.nums[right], m.nums[pivotIndex]
	storeIndex := left
	for i := left; i < right; i++ {
		if m.nums[i] < pivot {
			m.nums[storeIndex], m.nums[i] = m.nums[i], m.nums[storeIndex]
			storeIndex++
		}
	}
	m.nums[right], m.nums[storeIndex] = m.nums[storeIndex], m.nums[right]
	return storeIndex
}
