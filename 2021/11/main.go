package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

type Octopus struct {
	x, y, energy int
	flashed      bool
}

func (o *Octopus) Neighbours(f *Field) (nbs []Octopus) {
	xc := o.x
	yc := o.y
	for x := -1; x <= 1; x++ {
		for y := -1; y <= 1; y++ {
			t := [2]int{xc + x, yc + y}
			if t[0] >= 0 && t[0] < len((*f)) && t[1] >= 0 && t[1] < len((*f)[0]) {
				nbs = append(nbs, (*f)[t[1]][t[0]])
			}
		}

	}
	return nbs
}

type Field [][]Octopus

func (f *Field) Print() {
	for y := 0; y < len(*f); y++ {
		for x := 0; x < len((*f)[0]); x++ {
			fmt.Print((*f)[y][x].energy)
		}
		fmt.Print("\n")
	}
	fmt.Println()
}

func (f *Field) Check() {
	toFlash := make([]Octopus, 0)
	for y := range *f {
		for x := range (*f)[y] {
			if (*f)[y][x].energy > 9 {
				toFlash = append(toFlash, (*f)[y][x])
			}
		}
	}

	if len(toFlash) > 0 {
		for _, o := range toFlash {
			(*f)[o.y][o.x].flashed = true
			(*f)[o.y][o.x].energy = 0
			for _, n := range o.Neighbours(f) {
				if !n.flashed {
					(*f)[n.y][n.x].energy++
				}
			}
		}
		f.Check()
	}
}

func main() {
	path, _ := os.Getwd()
	file, err := os.ReadFile(filepath.Join(path, "./2021/11/input"))

	if err != nil {
		panic(err)
	}

	data := strings.Split(strings.TrimSuffix(string(file), "\n"), "\n")

	var (
		field      Field
		ans1, ans2 int
		all        bool
	)

	steps := 100

	for i, r := range data {
		var l []Octopus
		for j, c := range r {
			l = append(l, Octopus{x: j, y: i, energy: int(c - '0')})
		}
		field = append(field, l)
	}

	for step := 1; !all; step++ {
		for y := range field {
			for x := range field[y] {
				field[y][x].energy++
			}
		}
		field.Check()

		flashed := 0

		for y := range field {
			for x := range field[y] {
				if field[y][x].flashed {
					if step <= steps {
						ans1++
					}
					flashed++
					field[y][x].flashed = false
				}
			}
		}
		if flashed == len(field)*len(field[0]) {
			ans2 = step
			all = true
			field.Print()
		}
	}

	fmt.Println("1: ", ans1)
	fmt.Println("2: ", ans2)

}
