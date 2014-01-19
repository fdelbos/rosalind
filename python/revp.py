#!/usr/bin/env python
# result is wrong apprently, don't know why...
import sys

raw_input()
s = ""
for l in sys.stdin:
    s += l[:-1]
    

def rev(s):
    trad = {'A':'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(map(lambda x: trad[x], s[::-1]))

for i in range(0, len(s)):
    for j in range(12, 3, -1):
        if i + j > len(s):
            continue
        if s[i: i + j] == rev(s[i: i + j]):
            print "%i %i" % (i + 1 , j)
            break
