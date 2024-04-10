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
	rand.Seed(42)
	for i := 0; i < g.Vertices; i++ {
		for j := i + 1; j < g.Vertices; j++ {
			weight := rand.Float64()
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

func (g *Graph) MinSpanningTree() *Graph {
	mst := &Graph{
		Vertices: g.Vertices,
		Edges:    make([][]float64, g.Vertices),
	}
	for i := range mst.Edges {
		mst.Edges[i] = make([]float64, g.Vertices)
	}
	// Prim's algorithm
	visited := make([]bool, g.Vertices)
	visited[0] = true
	for i := 1; i < g.Vertices; i++ {
		minWeight := 2.0
		minFrom := 0
		minTo := 0
		for j := 0; j < g.Vertices; j++ {
			if visited[j] {
				for k := 0; k < g.Vertices; k++ {
					if !visited[k] && g.Edges[j][k] < minWeight {
						minWeight = g.Edges[j][k]
						minFrom = j
						minTo = k
					}
				}
			}
		}
		mst.Edges[minFrom][minTo] = minWeight
		mst.Edges[minTo][minFrom] = minWeight
		visited[minTo] = true

	}
	return mst

}

func (g *Graph) CalExpectation() float64 {
	// 计算期望
	sum := 0.0
	for i := 0; i < g.Vertices; i++ {
		for j := i + 1; j < g.Vertices; j++ {
			sum += g.Edges[i][j]
		}
	}
	return sum
}
