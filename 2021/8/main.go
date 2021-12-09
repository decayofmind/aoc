package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strconv"
	"strings"
)

func compare(a, b []string) (diff []string) {
	match := make(map[string]bool)
	for _, i := range b {
		match[i] = true
	}

	for _, i := range a {
		if _, ok := match[i]; !ok {
			diff = append(diff, i)
		}
	}

	return diff
}

func main() {
	path, _ := os.Getwd()
	file, _ := os.ReadFile(filepath.Join(path, "./input"))

	data := strings.Split(string(file), "\n")

	var ans1, ans2 int

	for _, l := range data[:len(data)-1] {
		parsed := strings.Split(l, " | ")

		in := strings.Fields(parsed[0])
		out := strings.Fields(parsed[1])

		h := make([]string, 3)
		v := make([]string, 4)

		possibles := make([][]string, 10)

		var output string

		for _, el := range in {
			count := len(el)
			switch count {
			case 2:
				possibles[1] = strings.Split(el, "")
			case 3:
				possibles[7] = strings.Split(el, "")
			case 4:
				possibles[4] = strings.Split(el, "")
			case 7:
				possibles[8] = strings.Split(el, "")
			}
		}

		comp := compare(possibles[7], possibles[1])
		h[0] = comp[0]

		for ok := true; ok; ok = len(strings.Join(h, "")) != 3 || len(strings.Join(v, "")) != 4 {
			for _, el := range in {
				count := len(el)

				if len(possibles[3]) > 0 && len(possibles[9]) > 0 && v[0] == "" {
					comp := compare(possibles[9], possibles[3])
					v[0] = comp[0]
				}

				switch count {
				case 5:
					if len(strings.Join(h, "")) == 3 && v[0] != "" {
						t := make([]string, 0)
						t = append(t, h[0], h[1], h[2], v[0])
						comp1 := compare(strings.Split(el, ""), t)
						if len(comp1) == 1 {
							v[3] = comp1[0]
							comp2 := compare(possibles[1], comp1)
							if len(comp2) == 1 {
								v[1] = comp2[0]
							}
						}
					} else {
						t := make([]string, 0)
						t = append(t, possibles[1]...)
						t = append(t, h[0], h[2])
						comp := compare(strings.Split(el, ""), t)

						if len(comp) == 1 {
							possibles[3] = strings.Split(el, "")
							h[1] = comp[0]
						}
					}

				case 6:
					if len(strings.Join(h, "")) == 3 && v[0] != "" {
						t := make([]string, 0)
						t = append(t, h[0], h[2], v[0])
						t = append(t, possibles[1]...)
						comp_t := compare(strings.Split(el, ""), t)
						if len(comp_t) == 1 && comp_t[0] != h[1] {
							v[2] = comp_t[0]
						}
					} else {
						w7 := compare(strings.Split(el, ""), possibles[4])
						if len(w7) == 2 {
							possibles[9] = strings.Split(el, "")
							for _, x := range w7 {
								if x != h[0] {
									h[2] = x
								}
							}
						}
					}

				}
			}

			if len(strings.Join(h, "")) == 3 && len(strings.Join(v, "")) == 4 {
				break
			}
		}

		for _, el := range out {
			p := strings.Split(el, "")

			switch len(p) {
			case 2:
				output += "1"
				ans1++
			case 3:
				output += "7"
				ans1++
			case 4:
				output += "4"
				ans1++
			case 5:
				ren2 := append(h, v[1], v[2])
				ren3 := append(h, v[1], v[3])
				ren5 := append(h, v[0], v[3])

				diff2 := compare(p, ren2)
				diff3 := compare(p, ren3)
				diff5 := compare(p, ren5)

				if len(diff2) == 0 {
					output += "2"
				}

				if len(diff3) == 0 {
					output += "3"
				}

				if len(diff5) == 0 {
					output += "5"
				}
			case 6:
				ren0 := append(v, h[0], h[2])
				ren6 := append(h, v[0], v[2], v[3])
				ren9 := append(h, v[0], v[1], v[3])

				diff0 := compare(p, ren0)
				diff6 := compare(p, ren6)
				diff9 := compare(p, ren9)

				if len(diff0) == 0 {
					output += "0"
				}

				if len(diff6) == 0 {
					output += "6"
				}

				if len(diff9) == 0 {
					output += "9"
				}

			case 7:
				output += "8"
				ans1++
			}

		}
		inc, _ := strconv.Atoi(output)
		ans2 += inc
	}

	fmt.Println("1: ", ans1)
	fmt.Println("2: ", ans2)
}
