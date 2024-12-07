s = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".split("\n")[1:]

equations = []
for line in s:
    line = line.split(":")
    numbers = [int(x) for x in line[1][1:].split(" ")]
    equations.append([int(line[0]), numbers])

total_total = 0
for equation in equations:
    operands = equation[1]
    equation_good = False
    for i in range(0, 2**(len(operands)-1)):
        operators = format(i, '0'+str(len(operands)-1)+'b')
        total = operands[0]
        for j in range(0, len(operators)):
            operator = operators[j]
            if operator == "0":
                total += operands[j+1]
            else:
                total *= operands[j+1]
        if total == equation[0]:
            equation_good = True
            break
    if equation_good:
        total_total += int(equation[0])
print(total_total)