from advent import get_input_content


def part1(s: str):
    a = 0
    for line in s.splitlines():
        x = int(line.strip())
        a += x
    return a


def part2(s: str):
    a = 0
    seen = set()
    passes = 0
    int_lines = [int(line.strip()) for line in s.splitlines() if line.strip()]
    while passes < 10000:  # avoid infinite loop just in case
        passes += 1
        for x in int_lines:
            a += x
            if a in seen:
                return a
            seen.add(a)


if __name__ == "__main__":
    print("----- Part 1 -----")
    r1 = part1(get_input_content("1"))
    print(r1)

    print("----- Part 2 -----")
    r2 = part2(get_input_content("1"))
    print(r2)
