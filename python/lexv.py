#!/usr/bin/env python
import sys

a = raw_input().split(' ')
s = int(raw_input())

def gen(a, r, s):
    if r:
        print ''.join(r)
    if s == 0:
        return
    for i in range(0, len(a)):
        gen(a, r + [a[i]], s - 1)

gen(a, [], s)
