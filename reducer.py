#!/usr/bin/env python

import sys

import numpy as np

currentCluster = None
clusterElements = []
cluster = None

for line in sys.stdin:
    line = line.strip()

    cluster, data = line.split('\t', 1)
    try:
        data = np.array(data.strip().split(), dtype=float)
    except:
        continue
    if currentCluster == cluster:
        clusterElements.append(data)
    else:
        if currentCluster:
            newCentroid = np.mean(clusterElements, axis=0)
            newCentroid = "\t".join([str(a) for a in newCentroid])
            print '%s\t%s' % (currentCluster, newCentroid)
        clusterElements = [data]
        currentCluster = cluster

if currentCluster == cluster:
    newCentroid = np.mean(clusterElements, axis=0)
    newCentroid = "\t".join([str(a) for a in newCentroid])
    print '%s\t%s' % (currentCluster, str(newCentroid))
