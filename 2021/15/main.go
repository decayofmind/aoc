package main

import (
	"container/heap"
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

type Node struct {
	x, y int
}

type Edge struct {
	node   Node
	weight int
}

type Graph struct {
	nodes map[Node][]Edge
}

type Path struct {
	node Node
	dist int
}

type PriorityQueue []*Path

func (pq PriorityQueue) Len() int {
	return len(pq)
}

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].dist < pq[j].dist
}

func (pq *PriorityQueue) Push(x interface{}) {
	*pq = append(*pq, x.(*Path))
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	*pq = old[0 : n-1]
	return item
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
}

func getSurround(x, y int, d *[][]int) (s [][2]int) {
	coords := [4][2]int{{1, 0}, {-1, 0}, {0, -1}, {0, 1}}

	for _, c := range coords {
		t := [2]int{y + c[0], x + c[1]}

		if t[0] >= 0 && t[0] < len((*d)) && t[1] >= 0 && t[1] < len((*d)[0]) {
			s = append(s, t)
		}
	}
	return s
}

func (g *Graph) findShortestPath(start, end *Node) int {
	visited := make(map[Node]bool)

	pq := new(PriorityQueue)

	heap.Init(pq)

	init := Path{node: *start, dist: 0}

	heap.Push(pq, &init)

	for pq.Len() > 0 {
		p := heap.Pop(pq).(*Path)

		if visited[p.node] {
			continue
		}

		if p.node == *end {
			return p.dist
		}

		for _, e := range g.nodes[p.node] {
			if !visited[e.node] {
				heap.Push(pq, &Path{dist: p.dist + e.weight, node: e.node})
			}
		}

		visited[p.node] = true

	}

	return 0
}

func Expand(old [][]int) (new [][]int) {
	for _, r := range old {
		nl := make([]int, 0)
		for _, c := range r {
			if c == 9 {
				nl = append(nl, 1)
			} else {
				nl = append(nl, c+1)
			}
		}
		new = append(new, nl)
	}
	return new
}

func main() {
	path, _ := os.Getwd()
	file, err := os.ReadFile(filepath.Join(path, "./2021/15/input_test"))

	if err != nil {
		panic(err)
	}

	data := strings.Split(strings.TrimSuffix(string(file), "\n"), "\n")

	part := make([][]int, 0)

	for _, r := range data {
		l := make([]int, 0)
		for _, c := range r {
			l = append(l, int(c-'0'))
		}
		part = append(part, l)
	}

	cave := make([][]int, 0)
	cave = append(cave, part...)

	inc := Expand(part)
	for len(cave[0]) != len(part[0])*5 {
		for y, l := range inc {
			cave[y] = append(cave[y], l...)
		}
		inc = Expand(inc)
	}

	inc = Expand(cave)
	for len(cave) != len(part)*5 {
		cave = append(cave, inc...)
		inc = Expand(inc)
	}

	graph := Graph{nodes: make(map[Node][]Edge)}

	for y, l := range part {
		for x := range l {
			n := Node{y: y, x: x}
			for _, pos := range getSurround(x, y, &part) {
				graph.nodes[n] = append(graph.nodes[n], Edge{node: Node{x: pos[1], y: pos[0]}, weight: part[pos[1]][pos[0]]})
			}
		}
	}

	fmt.Println("1: ", graph.findShortestPath(&Node{x: 0, y: 0}, &Node{x: len(part[0]) - 1, y: len(part) - 1}))

	graph = Graph{nodes: make(map[Node][]Edge)}

	for y, l := range cave {
		for x := range l {
			n := Node{y: y, x: x}
			for _, pos := range getSurround(x, y, &cave) {
				graph.nodes[n] = append(graph.nodes[n], Edge{node: Node{x: pos[1], y: pos[0]}, weight: cave[pos[1]][pos[0]]})
			}
		}
	}
	fmt.Println("2: ", graph.findShortestPath(&Node{x: 0, y: 0}, &Node{x: len(cave[0]) - 1, y: len(cave) - 1}))
}
