#!/usr/bin/env python
import sys

s = []
for line in sys.stdin:
    if line[0] == '>':
        s.append("")
    else:
        s[-1] += line[:-1]

res = s[0]
del s[0]
while len(s) != 0:
    i = 0
    while i < len(s):
        if s[i] in res:
            del s[i]
        else:
            size = len(s[i])
            for j in range(1, size / 2):
                if s[i][j:] == res[:size - j]:
                    res = s[i][:j] + res
                    del s[i]
                    break
                elif s[i][:-j] == res[-size + j:]:
                    res += s[i][-j:]
                    del s[i]
                    break
        i += 1
print res
        
