# get claim info
def get_info(claim):
    margins, dim = claim.split("@")[1].split(":")
    left, top = (int(v) for v in margins.split(","))
    w, h = (int(v) for v in dim.split("x"))
    return left, top, w, h

# Looking for maximum dimensions
def get_max(data):
    max_width = 0
    max_height = 0
    for claim in data:
        left, top, w, h = get_info(claim)
        width = left + w + 1
        height = top + h + 1
        if width > max_width:
            max_width = width
        if height > max_height:
            max_height = height
    return max_width, max_height

if __name__ == "__main__":
    with open("3.input") as f:
        data = f.read().splitlines()

    #data = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]

    w, h = get_max(data)
    matrix = [[0 for i in range(w)] for i in range(h)]

    for idx, claim in enumerate(data):
        left, top, w, h = get_info(claim)
        for j in range(h):
            for i in range(w):
                matrix[top+j][left+i] += 1

    free = set()
    for idx, claim in enumerate(data):
        left, top, w, h = get_info(claim)
        nope = False
        for j in range(h):
            for i in range(w):
                if matrix[top+j][left+i] > 1:
                    nope = True
                    break
            if nope:
                break
        if not nope:
            free.add(idx+1)
    print(free, 415)
