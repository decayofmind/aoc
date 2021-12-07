package main

import (
	"fmt"
	"math"
	"os"
	"path/filepath"
	"strconv"
	"strings"
)

func arrayMin(array []int) int {
	min := array[0]

	for _, el := range array {
		if el < min {
			min = el
		}
	}
	return min
}

func arrayMax(array []int) int {
	max := array[0]

	for _, el := range array {
		if el > max {
			max = el
		}
	}
	return max
}

func getFuel(p1, p2 int, ans2 bool) int {
	distance := int(math.Abs(float64(p2 - p1)))
	if ans2 {
		var fuel int
		for i := 0; i <= distance; i++ {
			fuel += i
		}
		return fuel
	}
	return distance
}

func main() {
	path, _ := os.Getwd()

	file, _ := os.ReadFile(filepath.Join(path, "/input"))

	initial := make([]int, 0)

	data := strings.Split(string(file), "\n")

	for _, c := range strings.Split(data[0], ",") {
		c_i, _ := strconv.Atoi(c)
		initial = append(initial, c_i)
	}

	total1 := make([]int, 0)
	total2 := make([]int, 0)

	for t := 0; t <= arrayMax(initial); t++ {
		var (
			cons1, cons2 int
		)
		for _, c := range initial {
			cons1 += getFuel(c, t, false)
			cons2 += getFuel(c, t, true)
		}

		total1 = append(total1, cons1)
		total2 = append(total2, cons2)
	}

	fmt.Println("1: ", arrayMin(total1))
	fmt.Println("1: ", arrayMin(total2))

}
