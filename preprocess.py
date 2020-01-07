import random

lines = []
with open("Mall_Customers.csv", "r") as f:
    data = f.readlines()
    for line in data[1:]:
        line_split = line.strip().split(",")
        lines.append(("0" if (line_split[1] == "Male") else "1") + "\t" + line_split[2] + "\t" + line_split[3] + "\t" +
                     line_split[4])

body = "\n".join(lines)

with open("input1.txt", "w") as f:
    f.write(body)

with open("centroids1.txt", "w") as f:
    n = len(lines) - 1
    centroids = []
    for i in range(10):
        line = lines[random.randint(0, n)]
        centroids.append(line)
    f.write("\n".join(centroids))
