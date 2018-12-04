# get claim info
def get_info(claim):
    margins, dim = claim.split("@")[1].split(":")
    left, top = (int(v) for v in margins.split(","))
    w, h = (int(v) for v in dim.split("x"))
    return left, top, w, h

# Looking for maximum dimensions
def get_max(data):
    max_w = 0
    max_h = 0
    for claim in data:
        left, top, width, height = get_info(claim)
        w = left + width + 1
        h = top + height + 1
        max_w = w if w > max_w else max_w
        max_h = h if h > max_h else max_h
    return max_w, max_h

if __name__ == "__main__":
    with open("3.input") as f:
        data = f.read().splitlines()

    # Creating empty matrix
    w, h = get_max(data)
    matrix = [[0 for i in range(w)] for i in range(h)]

    # Filling matrix
    for claim in data:
        left, top, w, h = get_info(claim)
        for j in range(h):
            for i in range(w):
                matrix[top+j][left+i] += 1

    # Getting the total number of square inches that have more than
    # 1 claim on it
    total = sum(1 for j in matrix for i in j if i > 1)
    print(total, 100595)
