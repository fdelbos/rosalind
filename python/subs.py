#!/usr/bin/env python
import sys

l = raw_input()
s = raw_input()
size = len(s)
for i in range(0, len(l) - size):
    if l[i:i+size] == s:
        sys.stdout.write("%i " % (i + 1))
