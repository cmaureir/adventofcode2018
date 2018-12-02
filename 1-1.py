f = 0
with open("1.input") as i:
    f += sum(int(line) for line in i.readlines())
print(f)
