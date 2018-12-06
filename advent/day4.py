from advent import get_input_content


def part1(s: str):
    times = sorted(s.splitlines())
    asleep = {}
    current_guard = 0
    last_asleep = 0
    for line in times:
        if line.endswith('t'):
            current_guard = int(line.split('#')[1].split(' ')[0])
        elif line.endswith('ep'):
            last_asleep = int(line.split(':')[1].split(']')[0])
        elif line.endswith('up'):
            asleep[current_guard] = asleep.get(current_guard, 0) + int(line.split(':')[1].split(']')[0]) - last_asleep

    # print(asleep)
    max_asleep = max(asleep.items(), key=lambda x: x[1])[0]
    # print(max_asleep)

    minutes = {i: 0 for i in range(60)}
    for line in times:
        if line.endswith('t'):
            current_guard = int(line.split('#')[1].split(' ')[0])
        if current_guard != max_asleep:
            continue
        if line.endswith('ep'):
            last_asleep = int(line.split(':')[1].split(']')[0])
        elif line.endswith('up'):
            for m in range(last_asleep, int(line.split(':')[1].split(']')[0])):
                minutes[m] += 1

    # print(minutes)
    max_minutes = max(minutes.items(), key=lambda x: x[1])[0]
    # print(max_minutes)

    return max_asleep * max_minutes


def part2(s: str):
    times = sorted(s.splitlines())
    asleep = {}
    current_guard = 0
    last_asleep = 0
    for line in times:
        if line.endswith('t'):
            current_guard = int(line.split('#')[1].split(' ')[0])
        elif line.endswith('ep'):
            last_asleep = int(line.split(':')[1].split(']')[0])
        elif line.endswith('up'):
            if current_guard not in asleep:
                asleep[current_guard] = {i: 0 for i in range(60)}
            for m in range(last_asleep, int(line.split(':')[1].split(']')[0])):
                asleep[current_guard][m] += 1

    max_guard = 0
    max_minute = 0
    max_minute_value = 0
    for guard, guard_asleep in asleep.items():
        for m, minutes_asleep in guard_asleep.items():
            if minutes_asleep > max_minute_value:
                max_minute_value = minutes_asleep
                max_guard = guard
                max_minute = m

    print(max_guard)
    print(max_minute)
    return max_guard * max_minute


if __name__ == "__main__":
    print("----- Part 1 -----")
    r1 = part1(get_input_content("4"))
    print(r1)

    print("----- Part 2 -----")
    r2 = part2(get_input_content("4"))
    print(r2)
