from advent import get_input_content


def part1(s: str):
    # format: #123 @ 3,2: 5x4
    data = []
    for line in s.splitlines():
        i, x = line.split(" @ ")
        _id = i.strip("#")
        p, s = x.split(": ")
        pw, ph = p.split(",")
        w, h = s.split("x")
        data.append((int(pw), int(ph), int(w), int(h)))

    max_w = max(pw + w for (pw, ph, w, h) in data)
    max_h = max(ph + h for (pw, ph, w, h) in data)

    matrix = [None] * (max_h + 1)
    for i in range(max_h + 1):
        matrix[i] = [0] * (max_w + 1)

    for (pw, ph, w, h) in data:
        for i in range(ph+1, ph+h+1):
            for j in range(pw+1, pw+w+1):
                matrix[i][j] += 1

    return sum(1 if x >= 2 else 0 for line in matrix for x in line)


def part2(s: str):
    # format: #123 @ 3,2: 5x4
    data = []
    for line in s.splitlines():
        i, x = line.split(" @ ")
        _id = i.strip("#")
        p, s = x.split(": ")
        pw, ph = p.split(",")
        w, h = s.split("x")
        data.append((int(_id), int(pw), int(ph), int(w), int(h)))

    max_w = max(pw + w for (_id, pw, ph, w, h) in data)
    max_h = max(ph + h for (_id, pw, ph, w, h) in data)

    matrix = [None] * (max_h + 1)
    for i in range(max_h + 1):
        matrix[i] = [None] * (max_w + 1)
        for j in range(max_w + 1):
            matrix[i][j] = set()

    overlapped = {}

    for (_id, pw, ph, w, h) in data:
        overlapped[_id] = False
        for i in range(ph+1, ph+h+1):
            for j in range(pw+1, pw+w+1):
                matrix[i][j].add(_id)
                if len(matrix[i][j]) > 1:
                    for x in matrix[i][j]:
                        overlapped[x] = True

    for k, v in overlapped.items():
        if not v:
            return k


if __name__ == "__main__":
    print("----- Part 1 -----")
    r1 = part1(get_input_content("3"))
    print(r1)

    print("----- Part 2 -----")
    r2 = part2(get_input_content("3"))
    print(r2)
