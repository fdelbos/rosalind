#!/usr/bin/env python
import sys

def inall(s, lines):
    for l in lines:
        if s not in l:
            return False
    return True

nodes = []
c = None
for line in sys.stdin:
    if line[0] == '>':
        if c is not None:
            nodes.append(c)
        c = ""
    else:
        c += line[:-1]
nodes.append(c)

nodes = sorted(nodes, key=len)
ref = nodes[0]
del nodes[0]

def lo(ref, nodes):
    for size in range(len(ref), 0, -1):
        for offset in range(0, len(ref)):
            if offset + size > len(ref):
                continue
            if inall(ref[offset:offset + size], nodes) == True:
                print "%s" % ref[offset:offset + size]
                return
lo(ref, nodes)
