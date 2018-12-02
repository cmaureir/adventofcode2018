f = 0
reached = {0}
not_found = True
while not_found:
    with open("1.input") as i:
        for line in i.readlines():
            n = int(line)
            f += n
            if f in reached:
                print(f)
                not_found = False
                break
            else:
                reached.add(f)
