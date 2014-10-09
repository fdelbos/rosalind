package main

import (
	"fmt"
	"os"
	"bufio"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	a, c, g, t := 0, 0, 0, 0
	
	for i, err := in.ReadByte(); err == nil; i, err = in.ReadByte() {
		switch i {
		case 'A': a += 1
		case 'C': c += 1
		case 'G': g += 1
		case 'T': t += 1
		}
	}
	fmt.Println(a, c, g, t)
}
