from advent import get_input_content

from collections import Counter


def part1(s: str):
    twos = 0
    threes = 0
    for line in s.splitlines():
        count = Counter(line.strip())
        if any(v == 2 for v in count.values()):
            twos += 1
        if any(v == 3 for v in count.values()):
            threes += 1
    return twos * threes


def part2(s: str):
    lines = s.splitlines()
    for i, line1 in enumerate(lines):
        for line2 in lines[i+1:]:
            diff = 0
            for x, y in zip(line1.strip(), line2.strip()):
                if x != y:
                    diff += 1
                    if diff > 1:
                        break
            if diff == 1:
                return "".join(x for x, y in zip(line1.strip(), line2.strip()) if x == y)


if __name__ == "__main__":
    print("----- Part 1 -----")
    r1 = part1(get_input_content("2"))
    print(r1)

    print("----- Part 2 -----")
    r2 = part2(get_input_content("2"))
    print(r2)
