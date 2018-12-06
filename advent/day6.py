from advent import get_input_content


def part1(s: str):
    positions = [line.split(", ") for line in s.splitlines()]
    positions = [(int(x), int(y)) for x, y in positions]
    # print(positions)

    min_x = min(positions, key=lambda p: p[0])[0]
    max_x = max(positions, key=lambda p: p[0])[0]
    min_y = min(positions, key=lambda p: p[1])[1]
    max_y = max(positions, key=lambda p: p[1])[1]
    # print(min_x, max_x, min_y, max_y)

    grid = [[]] * (max_y - min_y + 1)
    for y in range(max_y - min_y + 1):
        grid[y] = [None] * (max_x - min_x + 1)

    for p, (x, y) in enumerate(positions):
        grid[y - min_y][x - min_x] = (p, 0)

    one_grew = True
    still_growing = {p: True for p in range(len(positions))}
    dist = 0
    while one_grew:
        one_grew = False
        dist += 1
        for p, (x, y) in enumerate(positions):
            if not still_growing[p]:
                continue
            p_grew = False
            for dx, dy in list(zip(range(dist), range(-dist, 0))) + \
                          list(zip(range(dist, 0, -1), range(dist))) + \
                          list(zip(range(0, -dist, -1), range(dist, 0, -1))) + \
                          list(zip(range(-dist, 0), range(0, -dist, -1))):
                if x + dx < min_x or y + dy < min_y or x + dx > max_x or y + dy > max_y:
                    continue
                j = x + dx - min_x
                i = y + dy - min_y
                if grid[i][j] is not None and grid[i][j][1] == dist:
                    grid[i][j] = (-1, dist)
                    p_grew = True
                if grid[i][j] is None:
                    grid[i][j] = (p, dist)
                    p_grew = True
            if not p_grew:
                still_growing[p] = False
            one_grew = one_grew or p_grew
        # print(grid)

    infinite = {p: False for p in range(len(positions))}
    infinite[-1] = True

    for line in grid:
        infinite[line[0][0]] = True
        infinite[line[-1][0]] = True

    for (near, dist) in grid[0]:
        infinite[near] = True

    for (near, dist) in grid[-1]:
        infinite[near] = True

    # print("infinite:", infinite)

    count = {p: 0 for p in range(len(positions))}
    for line in grid:
        for (near, dist) in line:
            if not infinite[near]:
                count[near] += 1

    return max(count.values())


def part2(s: str):
    positions = [line.split(", ") for line in s.splitlines()]
    positions = [(int(x), int(y)) for x, y in positions]
    # print(positions)

    obj_less = 32 if len(positions) == 6 else 10000

    min_x = min(positions, key=lambda p: p[0])[0]
    max_x = max(positions, key=lambda p: p[0])[0]
    min_y = min(positions, key=lambda p: p[1])[1]
    max_y = max(positions, key=lambda p: p[1])[1]
    # print(min_x, max_x, min_y, max_y)

    grid = [[]] * (max_y - min_y + 1)
    for y in range(max_y - min_y + 1):
        grid[y] = [0] * (max_x - min_x + 1)

    for p, (x, y) in enumerate(positions):
        for dx in range(max_x - x + 1):
            for dy in range(max_y - y + 1):
                j = x + dx - min_x
                i = y + dy - min_y
                grid[i][j] += dx + dy
            for dy in range(1, y - min_y + 1):
                j = x + dx - min_x
                i = y - dy - min_y
                grid[i][j] += dx + dy
        for dx in range(1, x - min_x + 1):
            for dy in range(max_y - y + 1):
                j = x - dx - min_x
                i = y + dy - min_y
                grid[i][j] += dx + dy
            for dy in range(1, y - min_y + 1):
                j = x - dx - min_x
                i = y - dy - min_y
                grid[i][j] += dx + dy

    count = 0
    for line in grid:
        for d in line:
            if d < obj_less:
                count += 1

    return count


if __name__ == "__main__":
    day = __file__.split('day')[-1].split('.')[0]  # + "_example"
    input_content = get_input_content(day)

    print("----- Part 1 -----")
    r1 = part1(input_content)
    print(r1)

    print("----- Part 2 -----")
    r2 = part2(input_content)
    print(r2)
