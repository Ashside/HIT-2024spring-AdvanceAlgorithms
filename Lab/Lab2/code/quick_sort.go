package main

type quickSort struct {
	nums []int
}

// medianThree 三数取中值
func (q *quickSort) medianThree(left, mid, right int) int {
	// 此处使用异或运算来简化代码（!= 在这里起到异或的作用）
	if (q.nums[left] < q.nums[mid]) != (q.nums[left] < q.nums[right]) {
		return left
	} else if (q.nums[mid] < q.nums[left]) != (q.nums[mid] < q.nums[right]) {
		return mid
	}
	return right
}

// partition 分区
func (q *quickSort) partition(left, right int) int {
	// 以 nums[left] 为基准数
	med := q.medianThree(left, (left+right)/2, right)
	// 将中位数交换至数组最左端
	q.nums[left], q.nums[med] = q.nums[med], q.nums[left]
	// 以 nums[left] 为基准数
	i, j := left, right
	for i < j {
		for i < j && q.nums[j] >= q.nums[left] {
			j-- //从右向左找首个小于基准数的元素
		}
		for i < j && q.nums[i] <= q.nums[left] {
			i++ //从左向右找首个大于基准数的元素
		}
		//元素交换
		q.nums[i], q.nums[j] = q.nums[j], q.nums[i]
	}
	//将基准数交换至两子数组的分界线
	q.nums[left], q.nums[i] = q.nums[i], q.nums[left]
	return i //返回基准数的索引
}

// QSort 快速排序
func (q *quickSort) QSort(left, right int) {
	// 子数组长度为 1 时终止
	for left < right {
		// 哨兵划分操作
		pivot := q.partition(left, right)
		// 对两个子数组中较短的那个执行快速排序
		if pivot-left < right-pivot {
			q.QSort(left, pivot-1) // 递归排序左子数组
			left = pivot + 1       // 剩余未排序区间为 [pivot + 1, right]
		} else {
			q.QSort(pivot+1, right) // 递归排序右子数组
			right = pivot - 1       // 剩余未排序区间为 [left, pivot - 1]
		}
	}
}

// getMid 获取中位数
func (q *quickSort) getMid() float64 {
	q.QSort(0, len(q.nums)-1)
	if len(q.nums)%2 == 0 {
		return float64(q.nums[len(q.nums)/2-1]+q.nums[len(q.nums)/2]) / 2.0
	}
	return float64(q.nums[len(q.nums)/2])
}
