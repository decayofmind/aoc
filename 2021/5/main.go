package main

import (
	"fmt"
	"math"
	"os"
	"strings"
)

type Point struct {
	x, y int
}

type Line struct {
	start, end Point
}

func (l Line) Draw(field *map[Point]int, part2 bool) {
	var condition bool
	if part2 {
		condition = (math.Abs(float64(l.end.x-l.start.x)) == math.Abs(float64(l.end.y-l.start.y)))
	}

	if (l.start.x == l.end.x) || (l.start.y == l.end.y) || condition {

		coord := l.start

		for {
			(*field)[Point{x: coord.x, y: coord.y}]++

			if (coord.x == l.end.x) && (coord.y == l.end.y) {
				break
			}

			if coord.x < l.end.x {
				coord.x++
			}

			if coord.y < l.end.y {
				coord.y++
			}

			if coord.x > l.end.x {
				coord.x--
			}

			if coord.y > l.end.y {
				coord.y--
			}
		}
	}
}

func drawLines(lines *[]Line, part2 bool) map[Point]int {
	field := make(map[Point]int)
	for _, l := range *lines {
		l.Draw(&field, part2)
	}
	return field
}

func getOverlapsCount(field *map[Point]int) int {
	var count int
	for _, el := range *field {
		if el > 1 {
			count++
		}
	}
	return count
}

func main() {
	file, err := os.ReadFile("./input")

	if err != nil {
		panic(err)
	}

	lines := make([]Line, 0)

	data := strings.Split(string(file), "\n")

	for _, l := range data[:len(data)-1] {
		var (
			x1, x2 int
			y1, y2 int
		)

		fmt.Sscanf(l, "%d,%d -> %d,%d", &x1, &y1, &x2, &y2)

		lines = append(lines, Line{
			start: Point{x: x1, y: y1},
			end:   Point{x: x2, y: y2},
		})
	}

	field1 := drawLines(&lines, false)
	ans1 := getOverlapsCount(&field1)

	field2 := drawLines(&lines, true)
	ans2 := getOverlapsCount(&field2)

	fmt.Println("1: ", ans1)
	fmt.Println("2: ", ans2)

}
