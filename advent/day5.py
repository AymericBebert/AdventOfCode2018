from advent import get_input_content


def part1(s: str):
    res = []
    for x in s:
        if res and abs(ord(res[-1]) - ord(x)) == 32:
            res.pop()
        else:
            res.append(x)
    return len(res)


def part2(s: str):
    min_length = 1000000000
    for rem in range(65, 91):
        res = []
        for x in s:
            if ord(x) == rem or ord(x) == rem + 32:
                continue
            if res and abs(ord(res[-1]) - ord(x)) == 32:
                res.pop()
            else:
                res.append(x)
        if len(res) < min_length:
            min_length = len(res)
    return min_length


if __name__ == "__main__":
    day = __file__.split("day")[-1].split(".")[0]
    input_content = get_input_content(day)

    print("----- Part 1 -----")
    r1 = part1(input_content)
    print(r1)

    print("----- Part 2 -----")
    r2 = part2(input_content)
    print(r2)
