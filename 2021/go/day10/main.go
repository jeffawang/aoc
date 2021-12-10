package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var input string = "../../inputs/day10"

var d = map[rune]rune{
	'(': ')',
	'{': '}',
	'[': ']',
	'<': '>',
}

func main() {
	f, err := os.Open(input)
	if err != nil {
		panic("omg")
	}
	defer f.Close()
	scanner := bufio.NewScanner(f)

	var corrupt []rune
	var incomplete [][]rune
SCANLINE:
	for scanner.Scan() {
		var stack []rune
		for _, c := range scanner.Text() {
			if _, ok := d[c]; ok {
				stack = append(stack, c)
			} else {
				s := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				if c != d[s] {
					corrupt = append(corrupt, c)
					continue SCANLINE
				}
			}
		}
		if len(stack) > 0 {
			incomplete = append(incomplete, stack)
		}
	}

	s1 := scoreP1(corrupt)
	fmt.Printf("Part 2: %v\n", s1)

	s2 := scoreP2(incomplete)
	fmt.Printf("Part 2: %v\n", s2)
}

var valuesP1 = map[rune]int{
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137,
}

func scoreP1(corrupt []rune) int {
	var score int
	for _, c := range corrupt {
		score += valuesP1[c]
	}
	return score
}

var valuesP2 = map[rune]int{
	')': 1,
	']': 2,
	'}': 3,
	'>': 4,
}

func scoreP2(incomplete [][]rune) int {
	var scores []int
	for _, stack := range incomplete {
		score := 0
		for i, _ := range stack {
			c := stack[len(stack)-i-1]

			score *= 5
			score += valuesP2[d[c]]
		}
		scores = append(scores, score)
	}
	sort.Ints(scores)
	return scores[len(scores)/2]
}
