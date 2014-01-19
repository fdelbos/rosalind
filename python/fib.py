#!/usr/bin/env python

n, k = raw_input().split(' ')

p2 = 1
p1 = 1
current = 1
for i in range(0, int(n)):
    if i >= 2:
        p2 = p1
        p1 = current
        current = p1 + (p2 * int(k))
print(current)
