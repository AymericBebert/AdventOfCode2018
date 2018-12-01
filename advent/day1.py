from advent import get_input_path

if __name__ == "__main__":
    print("----- Part 1 -----")

    s = 0
    with open(get_input_path("1")) as f:
        for line in f.readlines():
            x = int(line.strip())
            s += x

    print(s)

    print("----- Part 2 -----")

    s = 0
    seen = set()
    searching = True
    while searching:
        with open(get_input_path("1")) as f:
            for line in f.readlines():
                x = int(line.strip())
                s += x
                if s in seen:
                    print(s)
                    searching = False
                    break
                seen.add(s)
