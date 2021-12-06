package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strconv"
	"strings"
)

func simulate(state map[int]int, days int) map[int]int {
	now := state
	for day := 1; day <= days; day++ {

		tomorrow := make(map[int]int)

		for age, count := range now {
			tomorrow[age] = count
		}

		for i := 1; i < 9; i++ {
			tomorrow[i-1] = now[i]
		}

		fresh := now[0]

		tomorrow[6] += fresh
		tomorrow[8] = fresh

		now = tomorrow
	}
	return now
}

func main() {
	path, err := os.Getwd()
	if err != nil {
		fmt.Println(err)
	}

	file, err := os.ReadFile(filepath.Join(path, "/input"))

	if err != nil {
		panic(err)
	}

	initial := make(map[int]int)

	data := strings.Split(string(file), "\n")

	for _, c := range strings.Split(data[0], ",") {
		c_i, _ := strconv.Atoi(c)
		initial[c_i]++
	}

	var (
		ans1, ans2 int
	)

	for _, v := range simulate(initial, 80) {
		ans1 += v
	}

	for _, v := range simulate(initial, 256) {
		ans2 += v
	}

	fmt.Println("1: ", ans1)
	fmt.Println("1: ", ans2)
}
