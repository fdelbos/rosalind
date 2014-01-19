#!/usr/bin/env python
import sys

line = raw_input()
for c in line:
    if c == 'T':
        sys.stdout.write('U')
    else:
        sys.stdout.write(c)
