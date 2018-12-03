from advent import get_input_path

from collections import Counter

if __name__ == "__main__":
    print("----- Part 1 -----")

    twos = 0
    threes = 0
    with open(get_input_path("2")) as f:
        for line in f.readlines():
            count = Counter(line.strip())
            if any(v == 2 for v in count.values()):
                twos += 1
            if any(v == 3 for v in count.values()):
                threes += 1
    print(twos * threes)

    print("----- Part 2 -----")

    with open(get_input_path("2")) as f:
        lines = f.readlines()
        for i, line1 in enumerate(lines):
            for line2 in lines[i+1:]:
                diff = 0
                for x, y in zip(line1.strip(), line2.strip()):
                    if x != y:
                        diff += 1
                        if diff > 1:
                            break
                if diff == 1:
                    print("".join(x for x, y in zip(line1.strip(), line2.strip()) if x == y))
