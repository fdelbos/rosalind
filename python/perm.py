#!/usr/bin/env python
import sys, math

nb = int(raw_input())
print "%i" % math.factorial(nb)

def display(l, a):
    if len(l) > 0:
        for i in range(0, len(l)):
            display(l[:i] + l[i + 1:], a + [l[i]])
    else:
        print '%s' % ' '.join(map(str, a))
        

display([x for x in range(1, nb + 1)], [])
