package main

import (
	"os"
	"bufio"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	for c, err := in.ReadByte(); err == nil; c, err = in.ReadByte() {
		if c == 'T' {
			out.WriteByte('U')
		} else {
			out.WriteByte(c)
		}
		out.Flush()
	}
}
