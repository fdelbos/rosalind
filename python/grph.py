#!/usr/bin/env python
import sys

nodes = {}
c = None
for line in sys.stdin:
    if line[0] == '>':
        c = line[1:-1]
        nodes[c] = ""
    else:
        nodes[c] += line[:-1]

for k in nodes:
    for l in nodes:
        if k != l and nodes[k][-3:] == nodes[l][:3]:
            print "%s %s" % (k, l)
