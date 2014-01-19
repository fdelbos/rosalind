#!/usr/bin/env python

line = raw_input()
res = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for c in line:
    res[c] += 1
print "%s %s %s %s" % (res['A'], res['C'], res['G'], res['T'])
    
