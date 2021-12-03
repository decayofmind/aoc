package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func sum(array []string) int {
	result := 0
	for _, v := range array {
		i, _ := strconv.Atoi(v)
		result += i
	}
	return result
}

func main() {
	file, err := os.Open("./data.txt")

	if err != nil {
		panic(err)
	}

	scanner := bufio.NewScanner(file)

	var lines []string

	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	file.Close()

	var answer1 int

	for nr, line := range lines {
		if nr == 0 {
			continue
		}

		cur, _ := strconv.Atoi(line)
		prev, _ := strconv.Atoi(lines[nr-1])

		if cur > prev {
			answer1++
		}
	}

	fmt.Println(answer1)

	var answer2 int

	var window_sums []int

	for i := 0; i < (len(lines) - 2); i++ {
		window := lines[i : i+3]

		window_sums = append(window_sums, sum(window))
	}

	for nr := range window_sums {
		if nr == 0 {
			continue
		}

		if window_sums[nr] > window_sums[nr-1] {
			answer2++
		}
	}

	fmt.Println(answer2)
}
