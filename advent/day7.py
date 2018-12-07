from advent import get_input_content


def part1(s: str):
    dependencies = [line.split(" ") for line in s.splitlines()]
    dependencies = [(d[1], d[7]) for d in dependencies]

    tasks = {}
    for before, after in dependencies:
        if before not in tasks:
            tasks[before] = []
        if after not in tasks:
            tasks[after] = []
        tasks[after].append(before)

    tasks = sorted(tasks.items(), key=lambda t: t[0])

    done_ord = []
    done = set()
    while len(done) != len(tasks):
        for after, befores in tasks:
            if after not in done and all(t in done for t in befores):
                done.add(after)
                done_ord.append(after)
                break

    return "".join(done_ord)


def part2(s: str):
    dependencies = [line.split(" ") for line in s.splitlines()]
    dependencies = [(d[1], d[7]) for d in dependencies]

    base_time = 60 if len(dependencies) != 7 else 0
    num_workers = 5 if len(dependencies) != 7 else 2

    tasks = {}
    for before, after in dependencies:
        if before not in tasks:
            tasks[before] = []
        if after not in tasks:
            tasks[after] = []
        tasks[after].append(before)

    tasks = sorted(tasks.items(), key=lambda t: t[0])

    time_cur = 0
    current = {}
    done = set()
    while len(done) != len(tasks):
        for after, befores in tasks:
            if after not in done and after not in current and all(t in done for t in befores):
                current[after] = base_time + ord(after) - 64
                if len(current) == num_workers:
                    break
        next_step = min(current.values())
        time_cur += next_step
        for t in current:
            current[t] -= next_step
            if current[t] == 0:
                done.add(t)

        for t in done:
            if t in current:
                del current[t]

    return time_cur


if __name__ == "__main__":
    day = __file__.split('day')[-1].split('.')[0]  # + "_example"
    input_content = get_input_content(day)

    print("----- Part 1 -----")
    r1 = part1(input_content)
    print(r1)

    print("----- Part 2 -----")
    r2 = part2(input_content)
    print(r2)
