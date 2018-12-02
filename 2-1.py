with open("2.input") as f:
    data = f.read().splitlines()

a, b = 0, 0
for line in data:
    count = [line.count(i) for i in set(line)]
    if 2 in count:
        a += 1
    if 3 in count:
        b += 1
print(a*b)
