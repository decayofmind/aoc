package main

import (
	"fmt"
	"os"
	"path/filepath"
	"regexp"
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

func main() {
	path, _ := os.Getwd()
	file, err := os.ReadFile(filepath.Join(path, "./2021/14/input_test"))

	if err != nil {
		panic(err)
	}

	data := strings.Split(strings.TrimSuffix(string(file), "\n"), "\n")

	rules := make(map[string]string)

	re := regexp.MustCompile("([A-Z]){1}([A-Z]){1} -> ([A-Z]){1}")

	for _, r := range data[2:] {
		parsed := re.FindStringSubmatch(r)
		rules[parsed[1]+parsed[2]] = parsed[len(parsed)-1]
	}

	maxSteps := 40

	pairs := make(map[string]int)

	for i := 0; i < len(data[0])-1; i++ {
		pairs[string(data[0][i])+string(data[0][i+1])]++
	}

	for step := 0; step < maxSteps; step++ {
		updated := make(map[string]int)
		for k, v := range pairs {
			updated[string(k[0])+rules[k]] += v
			updated[rules[k]+string(k[1])] += v
		}
		pairs = updated
	}

	counts := make(map[string]int)
	for k, v := range pairs {
		counts[string(k[0])] += v
		counts[string(k[1])] += v
	}

	c := make([]int, 0)

	for _, v := range counts {
		c = append(c, v)
	}

	fmt.Println((arrayMax(c) - arrayMin(c) - 1) / 2)

}
