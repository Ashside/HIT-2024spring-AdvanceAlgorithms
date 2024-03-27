package main

import (
	"fmt"
	"math/rand"
)

type Graph struct {
	Vertices int
	Edges    [][]float64
}

func NewGraph(n int) *Graph {
	g := &Graph{
		Vertices: n,
		Edges:    make([][]float64, n),
	}

	for i := range g.Edges {
		g.Edges[i] = make([]float64, n)
	}
	g.generateRandomGraph()
	return g
}

func (g *Graph) generateRandomGraph() {
	rand.Seed(42) // 设置随机种子，确保每次运行结果一致

	for i := 0; i < g.Vertices; i++ {
		for j := i + 1; j < g.Vertices; j++ {
			weight := rand.Float64() // 生成 [0,1] 之间的随机权重
			g.Edges[i][j] = weight
			g.Edges[j][i] = weight // 无向图，权重对称
		}
	}
}

func (g *Graph) PrintGraph() {
	for i := 0; i < g.Vertices; i++ {
		for j := 0; j < g.Vertices; j++ {
			fmt.Printf("%.2f\t", g.Edges[i][j])
		}
		fmt.Println()
	}
}

func main() {
	n := 5 // 顶点数
	g := NewGraph(n)
	g.generateRandomGraph()
	g.PrintGraph()
}
