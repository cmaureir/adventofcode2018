with open("2.input") as f:
    data = f.read().splitlines()

l = len(data)
for i in range(l):
    i_data = data[i]
    for j in range(i, l):
        j_data = data[j]
        diff = sum(1 for a, b in zip(i_data, j_data) if a != b)
        if diff == 1:
            print("".join(a for a, b in zip(i_data, j_data) if a == b))
            break
