#!/usr/bin/env python
import sys

cname = None
cstr = None
best = 0.0
bestname = None

def pc(l, name, best, bestname):
    count = 0
    for i in l:
        if i == 'C' or i == 'G':
            count += 1
    t = float(count) / len(l)
    if t > best: return (t, name)
    else: return (best, bestname)

for line in sys.stdin:
    if line[0] == '>':
        if cstr is not None:
            best, bestname = pc(cstr, cname, best, bestname)
        cname = line[1:]
        cstr = ""
    else:
        cstr += line[:-1]
best, bestname = pc(cstr, cname, best, bestname)
print "%s%f" % (bestname, best * 100)
