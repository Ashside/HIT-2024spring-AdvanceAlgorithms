package main

import (
	"fmt"
	"time"
)

func main() {
	iter := 50
	numList := []int{16, 32, 64, 128, 256, 512, 1024}
	//numList := []int{5}
	for _, n := range numList {
		// 重复计算iter次，取平均值
		exp := 0.0
		start := time.Now().UnixNano()
		for i := 0; i < iter; i++ {
			exp += Calculate(n)
		}
		end := time.Now().UnixNano()
		fmt.Printf("n=%d, E=%.2f, time=%v\n", n, exp/float64(iter), time.Duration(end-start))
	}
}

func Calculate(n int) float64 {

	g := NewGraph(n)
	//mst := g.MinSpanningTree()
	mst := g.KruskalMST()
	//mst.PrintGraph()
	exp := mst.CalExpectation()
	return exp

}
