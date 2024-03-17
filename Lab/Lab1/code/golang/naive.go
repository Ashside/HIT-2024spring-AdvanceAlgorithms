package main

import (
	"fmt"
)

type Naive struct {
	mapping     map[int][]int
	setIDs      []int
	allValues   []int
	bound       float64
}

func NewNaive(bound float64, textSel int) *Naive {
	collector := NewCollector(textSel)
	mapping := collector.GetData()
	setIDs := collector.GetKeys()
	allValues := collector.GetAllValues()
	return &Naive{
		mapping:   mapping,
		setIDs:    setIDs,
		allValues: allValues,
		bound:     bound,
	}
}

func (n *Naive) calcSimilarity(set1, set2 map[int]bool) float64 {
	intersection := 0
	for key := range set1 {
		if set2[key] {
			intersection++
		}
	}
	union := len(set1) + len(set2) - intersection
	similarity := float64(intersection) / float64(union)
	return similarity
}

func (n *Naive) calcSimilarityAll() [][]interface{} {
	var similarityAll [][]interface{}
	for i := 0; i < len(n.setIDs)-1; i++ {
		set1 := make(map[int]bool)
		for _, item := range n.mapping[n.setIDs[i]] {
			set1[item] = true
		}
		id1 := n.setIDs[i]
		for j := i + 1; j < len(n.setIDs); j++ {
			set2 := make(map[int]bool)
			for _, item := range n.mapping[n.setIDs[j]] {
				set2[item] = true
			}
			id2 := n.setIDs[j]
			similarity := n.calcSimilarity(set1, set2)
			if similarity >= n.bound {
				similarityAll = append(similarityAll, []interface{}{id1, id2, similarity})
			}
		}
	}
	return similarityAll
}

func main() {
	naive := NewNaive(0.9, 3)
	similarityAll := naive.calcSimilarityAll()
	fmt.Println("Similarity:", similarityAll)
}
