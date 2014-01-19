#!/usr/bin/env python
import sys

s = []
for line in sys.stdin:
    if line[0] == '>':
        s.append("")
    else:
        s[-1] += line[:-1]

size = len(s[0])
count = {
    'A': [0] * size,
    'C': [0] * size,
    'G': [0] * size,
    'T': [0] * size}    

for line in s:
    for i in range(0, size):
        count[line[i]][i] += 1

for i in range(0, size):
    b = None
    c = -1
    for k in count:
        if count[k][i] > c:
            b = k
            c = count[k][i]
    sys.stdout.write(b)

for k in ['A', 'C', 'G', 'T']:
    sys.stdout.write("\n%s:" % k)
    for i in count[k]:
        sys.stdout.write(" %i" % i)

