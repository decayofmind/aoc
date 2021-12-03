package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("./data.txt")

	if err != nil {
		panic(err)
	}

	scanner := bufio.NewScanner(file)

	var data []string

	for scanner.Scan() {
		data = append(data, scanner.Text())
	}

	file.Close()

	var pos_x = 0
	var pos_y = 0
	var aim = 0

	for _, line := range data {
		parsed := strings.Split(line, " ")
		direction := parsed[0]
		step, _ := strconv.Atoi(parsed[1])

		switch direction {
		case "forward":
			pos_x += step
		case "up":
			pos_y += step
		case "down":
			pos_y -= step
		}
	}

	fmt.Println(pos_x * pos_y * -1)

	pos_x = 0
	pos_y = 0

	for _, line := range data {
		parsed := strings.Split(line, " ")
		direction := parsed[0]
		step, _ := strconv.Atoi(parsed[1])

		switch direction {
		case "forward":
			pos_x += step
			pos_y += (aim * step)
		case "up":
			aim += step
		case "down":
			aim -= step
		}
	}

	fmt.Println(pos_x * pos_y * -1)
}
