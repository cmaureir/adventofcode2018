from operator import itemgetter

def print_header():
    print("{}".format(" "*13), end="")
    for i in range(6):
        print("{}".format(str(i)*10), end="")
    print()
    print("{}".format(" "*13), end="")
    for i in range(60):
        print("{}".format(str(i%10)), end="")
    print()

def get_sorted_logs(data):
    logs = []
    for log in data:
        info, msg = log.split("]")
        date, time = info.split()
        year, month, day = date.replace("[", "").split("-")
        hour, minute = (int(i) for i in time.split(":"))
        logs.append((year, month, day, hour, minute, msg))

    return sorted(logs)

def get_guards_schedule(logs):
    l = {}
    idx = None
    for _, month, day, hour, minute, msg in logs:
        if "Guard" in msg:
            guard = msg.split()[1].replace("#", "")
            idx = "{}-{}_{}".format(month, day, guard)
            l[idx] = []
        if "falls asleep" in msg:
            # begin sleeping
            l[idx].append([minute])
        if "wakes up" in msg:
            # wakes up
            l[idx][-1].append(minute)
    return l

def get_sleeping_hours(schedule, print_table=False):
    if print_table:
        print_header()
    d = {}
    for entry in schedule:
        date, guard = entry.split("_")
        if print_table:
            print("{:5}  {:>4} ".format(date, guard), end=" ")
        line = ["."]*60
        for begin, end in schedule[entry]:
            for i in range(begin, end):
                line[i] = "#"

        total = line.count("#")
        if guard in d:
            d[guard] += total
        else:
            d[guard] = total

        if print_table:
            print("".join(i for i in line))
    return d

def get_repeated_minutes(schedule, print_table=False):
    r = [0 for i in range(60)]
    for entry in schedule:
        data, guard = entry.split("_")
        if guard == sleepiest[0]:
            line = [0]*60
            for begin, end in schedule[entry]:
                for i in range(begin, end):
                    line[i] = 1
                    r[i] += 1
            if print_table:
                print("".join(str(i) for i in line))
    return r


if __name__ == "__main__":
    with open("4.input") as f:
        data = f.read().splitlines()

    logs = get_sorted_logs(data)
    schedule = get_guards_schedule(logs)
    sleeping_hours = get_sleeping_hours(schedule)
    sleepiest = sorted(sleeping_hours.items(), key=lambda x: x[1])[-1]
    print("Most hours sleeping: "
        "#{} with {} minutes".format(sleepiest[0], sleepiest[1]))
    repeated = get_repeated_minutes(schedule)
    minute = repeated.index(max(repeated))
    print("Most sleep minute: {}".format(minute))
    print(minute*int(sleepiest[0]))
