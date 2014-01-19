#!/usr/bin/env python
import sys, urllib2, re

reg = re.compile("N[^P][ST][^P]")
for line in sys.stdin:
    line = line[:-1]
    h = urllib2.urlopen("http://www.uniprot.org/uniprot/%s.fasta" % line)
    c = ''.join(h.read().split('\n')[1:])
    if reg.search(c) is None:
        continue
    print line
    begin = 0
    while True:
        m = reg.search(c[begin:])
        if m is None:
            sys.stdout.write("\n")
            break
        begin += m.start() + 1
        sys.stdout.write("%s " % int(begin))
