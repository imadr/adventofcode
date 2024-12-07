s_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

97,75,61""".split("\n\n")

sorting = []

s = s_input[0].split("\n")
for i in range(0, len(s)):
    line = [int(x) for x in s[i].split("|")]
    if line[0] in sorting:
        if line[1] in sorting:
            if sorting.index(line[0]) > sorting.index(line[1]):
                del sorting[sorting.index(line[0])]
                sorting.insert(sorting.index(line[1]), line[0])
        else:
            sorting.insert(sorting.index(line[0])+1, line[1])
    else:
        if line[1] in sorting:
            sorting.insert(sorting.index(line[1]), line[0])
        else:
            sorting.append(line[0])
            sorting.append(line[1])
total = 0
s2 = s_input[1].split("\n")
print(sorting)
print()
for line in s2:
    bad = False
    line = [int(x) for x in line.split(",")]
    # print(line)
    for i in range(0, len(line)-1):
        i1 = sorting.index(line[i])
        i2 = sorting.index(line[i+1])
        if i1 > i2:
            bad = True
            break
    print(str(line)+" "+str(not bad))
    if not bad:
        total += line[int(len(line)/2)]
# print(total)