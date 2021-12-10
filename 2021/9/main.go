package main

import (
	"fmt"
	"os"
	"path/filepath"
	"sort"
	"strconv"
	"strings"
)

type Dot struct {
	x, y, z int
}

func getMinNeighbour(array []Dot) Dot {
	min := array[0]

	for _, el := range array {
		if el.z < min.z {
			min = el
		}
	}
	return min
}

func contains(d Dot, m *[]Dot) bool {
	for _, el := range *m {
		if d.x == el.x && d.y == el.y {
			return true
		}
	}
	return false
}

func getNeighbours(d Dot, m *[][]Dot) (ns []Dot) {
	x := d.x
	y := d.y

	coords := [4][2]int{{1, 0}, {-1, 0}, {0, -1}, {0, 1}}

	for _, c := range coords {
		t := [2]int{y + c[0], x + c[1]}
		if t[0] >= 0 && t[0] < len((*m)) && t[1] >= 0 && t[1] < len((*m)[0]) {
			ns = append(ns, (*m)[t[0]][t[1]])
		}
	}
	return ns
}

func isLowest(d Dot, nbs []Dot) bool {
	min := getMinNeighbour(nbs)
	return d.z < min.z
}

func scan(d Dot, m *[][]Dot, a *[]Dot) {
	nbs := getNeighbours(d, m)
	(*a) = append((*a), d)
	for _, n := range nbs {
		c := contains(n, a)
		if n.z < 9 && !c {
			scan(n, m, a)
		}
	}
}

func main() {
	path, _ := os.Getwd()
	file, err := os.ReadFile(filepath.Join(path, "./2021/9/input"))

	if err != nil {
		panic(err)
	}

	data := strings.Split(string(file), "\n")

	var (
		ans1 int
		ans2 = 1
	)

	heightmap := make([][]Dot, 0)

	lowest := make([]Dot, 0)

	for y, l := range data[:len(data)-1] {
		r := make([]Dot, 0)
		for x, c := range strings.Split(l, "") {
			i, _ := strconv.Atoi(c)
			r = append(r, Dot{x: x, y: y, z: i})
		}
		heightmap = append(heightmap, r)
	}

	for _, l := range heightmap {
		for _, d := range l {
			nbs := getNeighbours(d, &heightmap)
			if isLowest(d, nbs) {
				lowest = append(lowest, d)
				ans1 += d.z + 1
			}
		}
	}

	sizes := []int{}

	for _, d := range lowest {
		area := []Dot{}
		scan(d, &heightmap, &area)
		sizes = append(sizes, len(area))
	}

	sort.Ints(sizes)
	for _, i := range sizes[len(sizes)-3:] {
		ans2 *= i
	}

	fmt.Println("1: ", ans1)
	fmt.Println("2: ", ans2)
}
