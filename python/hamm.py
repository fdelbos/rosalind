#!/usr/bin/env python

l1 = raw_input()
l2 = raw_input()

d = 0
for i in range(0, len(l1)):
    if l1[i] != l2[i]:
        d += 1
print d

