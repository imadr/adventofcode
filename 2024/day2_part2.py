i = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

arr = [[int(y) for y in x.split(" ")] for x in i.split("\n")]

def check_safe(report):
    if report != sorted(report) and report != sorted(report, reverse=True):
        return False
    for i in range(1, len(report)):
        diff = abs(report[i]-report[i-1])
        if diff < 1 or diff > 3:
            return False
    return True

def check_safe_2(report_input):
    for x in range(-1, len(report_input)):
        report = report_input.copy()
        if x > -1:
            del report[x]
        if check_safe(report):
            return True
    return False

print(sum([check_safe_2(x) for x in arr]))