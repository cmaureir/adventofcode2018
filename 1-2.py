r = 0
reached = {0}
not_found = True

with open("1.input") as f:
    data = f.read().splitlines()

while not_found:
    for i in data:
        r += int(i)
        if r not in reached:
            reached.add(r)
        else:
            not_found = False
            break
print(r)
