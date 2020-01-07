lines = []
with open("input1.txt", "r") as f:
    lines = [x.strip() for x in f.readlines()]
    m = dict()
    with open("output2.txt", "r") as f1:
        output1 = [x.strip() for x in f1.readlines()][:10]
        for row in output1:
            r = row.split("\t")
            seqs = [int(x) for x in r[3].split(",")]
            for seq in seqs:
                m[seq] = r[4]

    for i in range(len(lines)):
        lines[i] = lines[i] + "\t" + m[i + 1]

body = "\n".join(lines)

with open("input3.txt", "w") as f:
    f.write(body)
