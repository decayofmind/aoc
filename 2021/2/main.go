package main

import (
	"fmt"
	"os"
	"strings"
)

type Move struct {
	direction string
	value     int
}

func makeMovements(moves *[]Move, aim bool) (int, int) {
	var (
		x, y, aim_pos int
	)

	for _, m := range *moves {
		switch m.direction {
		case "forward":
			if aim {
				x += m.value
				y += (aim_pos * m.value)
			} else {
				x += m.value
			}
		case "up":
			if aim {
				aim_pos += m.value
			} else {
				y += m.value
			}
		case "down":
			if aim {
				aim_pos -= m.value
			} else {
				y -= m.value
			}
		}
	}
	return x, y
}

func main() {
	var (
		ans1, ans2 int
	)

	file, _ := os.ReadFile("./input")

	var moves []Move

	for _, l := range strings.Split(string(file), "\n") {
		var (
			direction string
			value     int
		)
		fmt.Sscanf(l, "%s %d", &direction, &value)
		moves = append(moves, Move{direction: direction, value: value})
	}

	x, y := makeMovements(&moves, false)
	ans1 = x * y * -1

	x, y = makeMovements(&moves, true)
	ans2 = x * y * -1

	fmt.Println("1: ", ans1)
	fmt.Println("2: ", ans2)
}
