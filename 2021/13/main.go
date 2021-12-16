package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

type Dot struct {
	x, y    int
	visible bool
}

type Fold struct {
	axis rune
	val  int
}

func fold(f Fold, p *[]Dot, c *map[string][]Dot) {
	for i, d := range *p {
		val := d.x
		if f.axis == 'y' {
			val = d.y
		}

		if val > f.val {
			key := fmt.Sprintf("%d:%d", d.x, d.y)
			(*c)[key] = (*c)[key][:len((*c)[key])-1]

			switch f.axis {
			case 'x':
				(*p)[i].x = f.val - (d.x - f.val)
			case 'y':
				(*p)[i].y = f.val - (d.y - f.val)
			}

			new_key := fmt.Sprintf("%d:%d", (*p)[i].x, (*p)[i].y)
			(*c)[new_key] = append((*c)[new_key], (*p)[i])

		}

	}
}

func main() {
	path, _ := os.Getwd()
	file, err := os.ReadFile(filepath.Join(path, "./2021/13/input"))

	if err != nil {
		panic(err)
	}

	data := strings.Split(strings.TrimSuffix(string(file), "\n"), "\n")

	paper := make([]Dot, 0)
	folds := make([]Fold, 0)
	cache := make(map[string][]Dot)

	var rFolds bool

	for _, l := range data {
		if l == "" {
			rFolds = true
			continue
		}

		if !rFolds {
			var x, y int
			fmt.Sscanf(l, "%d,%d", &x, &y)

			d := Dot{x: x, y: y, visible: true}

			paper = append(paper, d)
			key := fmt.Sprintf("%d:%d", x, y)
			cache[key] = append(cache[key], d)
		} else {
			var (
				axis rune
				val  int
			)
			fmt.Sscanf(l, "fold along %c=%d", &axis, &val)
			folds = append(folds, Fold{axis: axis, val: val})
		}
	}

	var ans1 int

	for i, f := range folds {
		fold(f, &paper, &cache)
		if i == 0 {
			for _, v := range cache {
				if len(v) > 0 {
					ans1++
				}
			}

		}
	}

	fmt.Println("1: ", ans1)

	var disp [6][82]string

	for y := range disp {
		for x := range disp[y] {
			disp[y][x] = " "
		}
	}

	for _, v := range cache {
		if len(v) > 0 {
			disp[v[0].y][v[0].x] = "#"
		}
	}

	for _, r := range disp {
		l := ""
		for _, c := range r {
			l += c
		}
		fmt.Println(l)
	}

}
