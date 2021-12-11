package main

import (
	"fmt"
	"os"
	"path/filepath"
	"sort"
	"strings"
)

func contains(a int, b *[]int) bool {
	for _, el := range *b {
		if a == el {
			return true
		}
	}
	return false
}

func main() {
	path, _ := os.Getwd()
	file, err := os.ReadFile(filepath.Join(path, "./2021/10/input"))

	if err != nil {
		panic(err)
	}

	data := strings.Split(string(file), "\n")

	var (
		ans1 int
		ans2 []int
	)

	closeToOpen := map[string]string{
		")": "(",
		"]": "[",
		"}": "{",
		">": "<",
	}

	openToClose := map[string]string{
		"(": ")",
		"[": "]",
		"{": "}",
		"<": ">",
	}

	errorScores := map[string]int{
		")": 3,
		"]": 57,
		"}": 1197,
		">": 25137,
	}

	complScores := map[string]int{
		")": 1,
		"]": 2,
		"}": 3,
		">": 4,
	}

	for _, l := range data[:len(data)-1] {
		splitted := strings.Split(l, "")
		matched := make([]int, 0)

		bad := false

		for i, c := range splitted {
			if closeToOpen[c] != "" {
				match := false
				for j := i - 1; j >= 0; j-- {
					if splitted[j] == closeToOpen[c] && !contains(j, &matched) {
						stat := make(map[string]int)
						s := splitted[j : i+1]
						for _, el := range s {
							stat[el] += 1
						}
						for op, cl := range closeToOpen {
							if stat[op] != stat[cl] {
								bad = true
								break
							}
						}
						match = true
						matched = append(matched, j, i)
						break
					}
				}
				if !match {
					bad = true
				}
				if bad {
					ans1 += errorScores[c]
					break
				}
			}
		}

		if !bad {
			var score int
			for i := len(l) - 1; i >= 0; i-- {
				if !contains(i, &matched) {
					score = score*5 + complScores[openToClose[splitted[i]]]
				}
			}
			ans2 = append(ans2, score)
		}

	}
	sort.Ints(ans2)

	fmt.Println("1: ", ans1)
	fmt.Println("2: ", ans2[len(ans2)/2])

}
