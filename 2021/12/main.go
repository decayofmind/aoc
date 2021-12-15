package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strings"
	"unicode"
)

func contains(n string, a *[]string) bool {
	for _, el := range *a {
		if n == el {
			return true
		}
	}
	return false
}

func IsSmall(n string) bool {
	for _, r := range n {
		if !unicode.IsLower(r) && unicode.IsLetter(r) {
			return false
		}
	}
	return true
}

func walk(n string, p []string, paths *[][]string, caves *map[string][]string, p2, used bool) {
	if IsSmall(n) && contains(n, &p) {
		if p2 {
			if used {
				return
			}
			used = true
			walk(n, p, paths, caves, p2, used)
		} else {
			return
		}
	}

	p = append(p, n)

	if n == "end" {
		*paths = append(*paths, p)
		return
	}

	for _, el := range (*caves)[n] {
		if el != "start" {
			walk(el, p, paths, caves, p2, used)
		}
	}

}

func main() {
	path, _ := os.Getwd()
	file, err := os.ReadFile(filepath.Join(path, "./2021/12/input"))

	if err != nil {
		panic(err)
	}

	data := strings.Split(strings.TrimSuffix(string(file), "\n"), "\n")

	caves := make(map[string][]string)

	var (
		paths1, paths2 [][]string
		pInit          []string
	)

	for _, l := range data {
		splitted := strings.Split(l, "-")
		caves[splitted[0]] = append(caves[splitted[0]], splitted[1])
		caves[splitted[1]] = append(caves[splitted[1]], splitted[0])
	}

	walk("start", pInit, &paths1, &caves, false, false)
	walk("start", pInit, &paths2, &caves, true, false)

	fmt.Println("1: ", len(paths1))
	fmt.Println("2: ", len(paths2))
}
