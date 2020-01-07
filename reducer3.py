#!/usr/bin/env python
import sys
from operator import itemgetter

distances = []
estimate_eval = 0.0
k = 3

for lines in sys.stdin:
    lines = lines.strip()
    elements = lines.split('\t')
    gender = 100 * float(elements[0])
    age = 3 * float(elements[1])
    income = float(elements[2])
    score = float(elements[3])
    distances.append([gender + age + income + score, lines])
distances = sorted(distances, key=itemgetter(-1))

result = distances[:k]

labels = []
print("The top 3 results similar are:")
for r in result:
    s = r[1].split("\t")[-1]
    print(s)
    labels.append(s.split(","))

l1 = dict()
l2 = dict()
l3 = dict()
l4 = dict()

for l in labels:
    if l[0] in l1:
        l1[l[0]] += 1
    else:
        l1[l[0]] = 1
    if l[1] in l2:
        l2[l[1]] += 1
    else:
        l2[l[1]] = 1
    if l[2] in l3:
        l3[l[2]] += 1
    else:
        l3[l[2]] = 1
    if l[3] in l4:
        l4[l[3]] += 1
    else:
        l4[l[3]] = 1

res = []
res.append(max(l1, key=l1.get))
res.append(max(l2, key=l2.get))
res.append(max(l3, key=l3.get))
res.append(max(l4, key=l4.get))
print("Ans with majority voting is : "+str(res))
