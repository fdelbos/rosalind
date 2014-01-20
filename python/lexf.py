#!/usr/bin/env python
import sys

a = raw_input().split(' ')
s = int(raw_input())

def gen(a, r, s):
    if len(r) == s:
        print ''.join(r)
        return
    for i in range(0, len(a)):
        gen(a, r + [a[i]], s)

gen(a, [], s)
