s = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
i = 0
end = False


inst = []
while not end:
    if i >= len(s):
        break
    if s[i:i+4] == "mul(":
        start_i = i
        end_of_string = False
        wrong = False
        i += 4

        while s[i] != ")":
            i += 1
            if i >= len(s):
                end_of_string = True
                break
            if s[i] != "," and not s[i].isnumeric() and s[i] != ")":
                wrong = True
                break

        if end_of_string:
            break
        end_i = i
        if not wrong:
            ss = s[start_i+4:end_i]
            ss = ss.split(",")
            if len(ss) == 2:
                inst.append([int(ss[0]), int(ss[1])])
        else:
            i -= 1
    i += 1

total = 0
for i in range(0, len(inst)):
    total += inst[i][0]*inst[i][1]
print(total)