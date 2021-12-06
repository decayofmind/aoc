package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strconv"
	"strings"
)

func countComparisons(records []int) int {
	var count int
	for i := 1; i < len(records); i++ {
		if records[i] > records[i-1] {
			count++
		}
	}
	return count
}

func sum(array []int) int {
	result := 0
	for _, v := range array {
		result += v
	}
	return result
}

func main() {
	path, _ := os.Getwd()
	file, _ := os.ReadFile(filepath.Join(path, "/input"))

	data := strings.Split(string(file), "\n")
	records := make([]int, 0)

	for _, l := range data {
		l_i, _ := strconv.Atoi(l)
		records = append(records, l_i)
	}

	var window_sums []int

	for i := 0; i < (len(records) - 2); i++ {
		window := records[i : i+3]
		window_sums = append(window_sums, sum(window))
	}

	fmt.Println("1: ", countComparisons(records))
	fmt.Println("1: ", countComparisons(window_sums))
}
