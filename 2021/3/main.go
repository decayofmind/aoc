package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strconv"
	"strings"
)

func categorize(list []string, pos int) ([]string, []string) {
	var zeros, ones []string
	for _, l := range list {
		switch l[pos] {
		case '0':
			zeros = append(zeros, l)
		case '1':
			ones = append(ones, l)
		}
	}
	return zeros, ones
}

func filter(list []string, t string) string {
	chunk := list
	for p := 0; p < len(list[0]); p++ {
		if len(chunk) == 1 {
			break
		}
		zeros, ones := categorize(chunk, p)
		switch t {
		case "o2":
			if len(zeros) > len(ones) {
				chunk = zeros
			} else {
				chunk = ones
			}
		case "co2":
			if len(zeros) > len(ones) {
				chunk = ones
			} else {
				chunk = zeros
			}
		}
	}
	return chunk[0]
}

func main() {
	path, _ := os.Getwd()

	file, _ := os.ReadFile(filepath.Join(path, "input"))

	data := strings.Split(string(file), "\n")

	var gamma_bin, epsilon_bin string

	for p := 0; p < len(data[0]); p++ {
		zeros, ones := categorize(data[:len(data)-1], p)

		if len(zeros) > len(ones) {
			gamma_bin += "0"
			epsilon_bin += "1"
		} else {
			gamma_bin += "1"
			epsilon_bin += "0"
		}
	}

	gamma, _ := strconv.ParseInt(gamma_bin, 2, 64)
	epsilon, _ := strconv.ParseInt(epsilon_bin, 2, 64)
	o2, _ := strconv.ParseInt(filter(data[:len(data)-1], "o2"), 2, 64)
	co2, _ := strconv.ParseInt(filter(data[:len(data)-1], "co2"), 2, 64)

	fmt.Println("1: ", gamma*epsilon)
	fmt.Println("2: ", o2*co2)

}
