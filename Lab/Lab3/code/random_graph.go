package main

import (
	"fmt"
	"math/rand"
	"sort"
)

type Edge struct {
	From, To int
	Weight   float64
}

type UnionFind struct {
	parent, rank []int
}

func NewUnionFind(n int) *UnionFind {
	parent := make([]int, n)
	rank := make([]int, n)
	for i := range parent {
		parent[i] = i
	}
	return &UnionFind{parent: parent, rank: rank}
}

func (uf *UnionFind) Find(i int) int {
	if uf.parent[i] != i {
		uf.parent[i] = uf.Find(uf.parent[i])
	}
	return uf.parent[i]
}

func (uf *UnionFind) Union(x, y int) {
	rootX, rootY := uf.Find(x), uf.Find(y)
	if rootX == rootY {
		return
	}
	if uf.rank[rootX] < uf.rank[rootY] {
		uf.parent[rootX] = rootY
	} else if uf.rank[rootX] > uf.rank[rootY] {
		uf.parent[rootY] = rootX
	} else {
		uf.parent[rootY] = rootX
		uf.rank[rootX]++
	}
}

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
	// Prim算法
	visited := make([]bool, g.Vertices)
	// 从第一个节点开始
	visited[0] = true
	// 重复n-1次
	for i := 1; i < g.Vertices; i++ {
		// 找到最小权重的边
		minWeight := 2.0
		minFrom := 0
		minTo := 0
		// 遍历已访问的节点
		for j := 0; j < g.Vertices; j++ {
			if visited[j] {
				// 遍历未访问的节点
				for k := 0; k < g.Vertices; k++ {
					// 未访问的节点 && 权重小于当前最小权重
					if !visited[k] && g.Edges[j][k] < minWeight {
						minWeight = g.Edges[j][k]
						minFrom = j
						minTo = k
					}
				}
			}
		}
		// 添加边
		mst.Edges[minFrom][minTo] = minWeight
		mst.Edges[minTo][minFrom] = minWeight
		// 标记已访问
		visited[minTo] = true

	}
	return mst

}

func (g *Graph) KruskalMST() *Graph {
	edges := make([]Edge, 0, g.Vertices*(g.Vertices-1)/2)
	for i := 0; i < g.Vertices; i++ {
		for j := i + 1; j < g.Vertices; j++ {
			edges = append(edges, Edge{From: i, To: j, Weight: g.Edges[i][j]})
		}
	}
	sort.Slice(edges, func(i, j int) bool {
		return edges[i].Weight < edges[j].Weight
	})

	mst := &Graph{
		Vertices: g.Vertices,
		Edges:    make([][]float64, g.Vertices),
	}
	for i := range mst.Edges {
		mst.Edges[i] = make([]float64, g.Vertices)
	}

	uf := NewUnionFind(g.Vertices)
	for _, edge := range edges {
		if uf.Find(edge.From) != uf.Find(edge.To) {
			uf.Union(edge.From, edge.To)
			mst.Edges[edge.From][edge.To] = edge.Weight
			mst.Edges[edge.To][edge.From] = edge.Weight
		}
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
