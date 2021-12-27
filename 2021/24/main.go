package main

import (
	"container/list"
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"strconv"
	"strings"
)

func run(p []string, inputs []int) int {
	inputQueue := list.New()

	m := make(map[string]int)
	for _, el := range []string{"w", "x", "y", "z"} {
		m[el] = 0
	}

	for _, i := range inputs {
		inputQueue.PushBack(i)
	}

	for _, inst := range p {
		re := regexp.MustCompile("([a-z]){1}")
		splitted := strings.Split(inst, " ")
		op := splitted[0]
		a := splitted[1]

		var (
			b    string
			valb int
		)

		if len(splitted) > 2 {
			b = splitted[2]
			if re.FindString(b) != "" {
				valb = m[b]
			} else {
				i, _ := strconv.Atoi(b)
				valb = i
			}
		}

		switch op {
		case "inp":
			if inputQueue.Len() > 0 {
				e := inputQueue.Front()
				i := e.Value.(int)
				m[a] = i
				inputQueue.Remove(e)
			} else {
				return m["z"]
			}
		case "add":
			m[a] += valb
		case "mul":
			m[a] *= valb
		case "div":
			if valb == 0 {
				panic("division by zero")
			}
			m[a] /= valb
		case "mod":
			if valb <= 0 || m[a] < 0 {
				panic("invalid operands")
			}
			m[a] = m[a] % valb
		case "eql":
			if m[a] == valb {
				m[a] = 1
			} else {
				m[a] = 0
			}
		}

	}

	return m["z"]
}

func reverse(inputs []int) int {
	inputQueue := list.New()

	for _, i := range inputs {
		inputQueue.PushBack(i)
	}

	var z int
	var s int

	for inputQueue.Len() > 0 {
		e := inputQueue.Front()
		w := e.Value.(int)
		inputQueue.Remove(e)

		x := z % 26

		switch s {
		case 0:
			x += 12
		case 1:
			x += 13
		case 2:
			x += 13
		case 3:
			z = z / 26
			x += -2
		case 4:
			z = z / 26
			x += -10
		case 5:
			x += 13
		case 6:
			z = z / 26
			x += -14
		case 7:
			z = z / 26
			x += -5
		case 8:
			x += 15
		case 9:
			x += 15
		case 10:
			z = z / 26
			x += -14
		case 11:
			x += 10
		case 12:
			z = z / 26
			x += -14
		case 13:
			z = z / 26
			x += -5
		}

		// for every deduction of x, find w, which equals to x
		// if x <= 9 && x >= 1 && s == 13 {
		// 	fmt.Println(inputs, x, z, s)
		// 	break
		// }

		if x != w {
			y := w

			switch s {
			case 0:
				y += 7
			case 1:
				y += 8
			case 2:
				y += 10
			case 3:
				y += 4
			case 4:
				y += 4
			case 5:
				y += 6
			case 6:
				y += 11
			case 7:
				y += 13
			case 8:
				y += 1
			case 9:
				y += 8
			case 10:
				y += 4
			case 11:
				y += 13
			case 12:
				y += 4
			case 13:
				y += 14
			}

			z = 26*z + y
		}
		s++
		// fmt.Println(s, w, x, z)
	}
	return z
}

func main() {
	path, _ := os.Getwd()
	file, err := os.ReadFile(filepath.Join(path, "./2021/24/input_test"))

	if err != nil {
		panic(err)
	}

	data := strings.Split(strings.TrimSuffix(string(file), "\n"), "\n")

	// the more precision intervals are the less complicated calculation is
	for d0 := 1; d0 >= 1; d0-- {
		for d1 := 3; d1 >= 1; d1-- {
			for d2 := 9; d2 >= 1; d2-- {
				for d3 := 9; d3 >= 1; d3-- {
					for d4 := 1; d4 >= 1; d4-- {
						for d5 := 6; d5 >= 6; d5-- {
							for d6 := 9; d6 >= 1; d6-- {
								for d7 := 9; d7 >= 7; d7-- {
									for d8 := 3; d8 >= 1; d8-- {
										for d9 := 9; d9 >= 1; d9-- {
											for da := 9; da >= 1; da-- {
												for db := 4; db >= 1; db-- {
													// ?,?,1,?,?,9,[1,2,3],?,?,?,?,?,?,?
													inp := []int{d0, d1, 1, d2, d3, 9, d4, d5, d6, d7, d8, d9, da, db}
													if reverse(inp) == 0 && run(data, inp) == 0 {
														fmt.Println(inp)
													}
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
}
