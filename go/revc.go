package main

import (
	"os"
	"bufio"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	line, err := in.ReadBytes('\n')
	out := bufio.NewWriter(os.Stdout)

	if err == nil {
		
		for i := len(line) - 1; i >= 0 ; i-- {
			switch line[i] {
			case 'A': out.WriteByte('T')
			case 'C': out.WriteByte('G')
			case 'G': out.WriteByte('C')
			case 'T': out.WriteByte('A')
			}
		}
		out.Flush()
	}
}
