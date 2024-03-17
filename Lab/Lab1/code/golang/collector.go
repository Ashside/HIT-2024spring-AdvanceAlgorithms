package main

import (
	"fmt"
	"log"
	"os"
	"strings"
)

type Collector struct {
	mapping map[int][]int // map[setID]setItem
	path    string
}

func NewCollector(textSel int) *Collector {
	switcher := map[int]string{
		0: "../data/E1_AOL-out.txt",
		1: "../data/E1_Booking-out.txt",
		2: "../data/E1_kosarak_100k.txt",
		3: "../data/test.txt",
	}
	path := switcher[textSel]
	return &Collector{
		mapping: make(map[int][]int),
		path:    path,
	}
}

func (c *Collector) Read() string {
	data, err := os.ReadFile(c.path)
	if err != nil {
		log.Fatal("File not found")
	}
	return string(data)
}

func (c *Collector) makeData() {
	data := c.Read()
	lines := strings.Split(data, "\n")
	for _, line := range lines {
		// 忽略空行
		if len(line) == 0 {
			continue
		}
		// 分割行
		items := strings.Split(line, "\t")
		if len(items) != 2 {
			continue
		}
		setID := parseInt(items[0])
		setItem := parseInt(items[1])
		// 如果setID已经存在，则检查setItem是否已经存在
		if _, ok := c.mapping[setID]; ok {
			found := false
			// 检查setItem是否已经存在
			for _, v := range c.mapping[setID] {
				if v == setItem {
					found = true
					break
				}
			}
			// 如果setItem不存在，则添加
			if !found {
				c.mapping[setID] = append(c.mapping[setID], setItem)
			}
		} else { //
			c.mapping[setID] = []int{setItem}
		}
	}
	fmt.Println("Data has been read successfully")
}

func (c *Collector) GetData() map[int][]int {
	return c.mapping
}

func (c *Collector) GetKeys() []int {
	keys := make([]int, 0, len(c.mapping))
	for k := range c.mapping {
		keys = append(keys, k)
	}
	return keys
}

func (c *Collector) GetAllValues() []int {
	allValues := make([]int, 0)
	for _, values := range c.mapping {
		for _, v := range values {
			allValues = append(allValues, v)
		}
	}
	allValues = removeDuplicates(allValues)
	return allValues
}

func parseInt(s string) int {
	var result int
	_, err := fmt.Sscanf(s, "%d", &result)
	if err != nil {
		log.Fatal(err)
	}
	return result
}

func removeDuplicates(intSlice []int) []int {
	keys := make(map[int]bool)
	var list []int
	for _, entry := range intSlice {
		if _, value := keys[entry]; !value {
			keys[entry] = true
			list = append(list, entry)
		}
	}
	return list
}

func main() {
	// 分别读取三个数据集
	c1 := NewCollector(0)
	c1.makeData()
	c2 := NewCollector(1)
	c2.makeData()
	c3 := NewCollector(2)
	c3.makeData()
	// 获取数据集的keys集长度
	fmt.Println("E1_AOL-out.txt keys length:", len(c1.GetKeys()))
	fmt.Println("E1_Booking-out.txt keys length:", len(c2.GetKeys()))
	fmt.Println("E1_kosarak_100k.txt keys length:", len(c3.GetKeys()))
}
