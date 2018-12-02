with open("2.input") as f:
    r = [0, 0]
    for line in f.readlines():
        count = [line.count(i) for i in set(line.strip())]
        if 2 in count:
            r[0] += 1
        if 3 in count:
            r[1] += 1
print(r[0]*r[1])
