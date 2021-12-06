package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Cell struct {
	value  int
	called bool
}

type Board struct {
	cells [][]Cell
}

func (c *Cell) mark() {
	c.called = true
}

func isInSlice(el int, list []int) bool {
	for _, a := range list {
		if el == a {
			return true

		}

	}
	return false
}

func mark(number int, board *[][]Cell) {
	for r, row := range *board {
		for c, col := range row {
			if col.value == number {
				(*board)[r][c].called = true
			}
		}
	}
}

func score(number int, board *[][]Cell) int {
	sum := 0
	for _, r := range *board {
		for _, c := range r {
			if !c.called {
				sum += c.value
			}
		}
	}
	return (number * sum)
}

func check(board *[][]Cell) bool {
	for _, row := range *board {
		accum := 0
		for _, c := range row {
			if c.called {
				accum++
			}
		}
		if accum == 5 {
			return true
		}
	}
	for i := 0; i < 5; i++ {
		accum := 0
		for _, row := range *board {
			if row[i].called {
				accum++
			}
		}
		if accum == 5 {
			return true
		}
	}
	return false
}

func main() {
	file, err := os.ReadFile("./input")

	if err != nil {
		panic(err)
	}

	data := strings.Split(string(file), "\n")

	sample := make([]int, 0)
	for _, n := range strings.Split(data[0], ",") {
		n_i, _ := strconv.Atoi(n)
		sample = append(sample, n_i)
	}

	var game [][][]Cell

	for i := 2; i < len(data[2:])+1; i += 6 {
		var board [][]Cell
		for _, r := range data[i : i+5] {
			parsed := strings.Fields(r)
			row := make([]Cell, 0)
			for _, v := range parsed {
				v_i, _ := strconv.Atoi(v)
				row = append(row, Cell{value: v_i})
			}
			board = append(board, row)
		}
		game = append(game, board)
	}

	var winners []int
	m := make(map[int][]int)

	for _, n := range sample {
		for b := range game {
			mark(n, &game[b])
			if check(&game[b]) {
				if !(isInSlice(b, winners)) {
					winners = append(winners, b)
					m[b] = append(m[b], score(n, &game[b]))
				}
			}
		}
	}

	fmt.Println("1: ", m[winners[0]][0])
	fmt.Println("2: ", m[winners[len(winners)-1]][0])
}
