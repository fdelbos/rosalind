#!/usr/bin/env python
import sys

raw_input()
dna = ""
for line in sys.stdin:
    if line[0] == '>':
        break
    dna += line[:-1]

sub = ""
for line in sys.stdin:
    sub += line[:-1]

i = j = 0
while i < len(dna) and j < len(sub):
    if dna[i] == sub[j]:
        sys.stdout.write("%i " % (i + 1))
        j += 1
    i += 1
