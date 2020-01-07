#!/usr/bin/env python
import math
import sys

inputval = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]
for lines in sys.stdin:
    avg = 0.0
    lines = lines.strip()
    features = lines.split('\t')
    d = []
    for i in range(len(features) - 1):
        if features[i] != '':
            avg += (float(features[i]) - float(inputval[i])) ** 2
            dist = math.sqrt(avg)
            d.append(dist)
    
    print '\t'.join([str(x) for x in d]) + "\t" + features[4]
