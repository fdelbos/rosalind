#!/usr/bin/env python
import sys
line = raw_input()[::-1]
for c in line:
    if c == 'A':
        sys.stdout.write('T')
    if c == 'T':
        sys.stdout.write('A')
    if c == 'C':
        sys.stdout.write('G')
    if c == 'G':
        sys.stdout.write('C')
