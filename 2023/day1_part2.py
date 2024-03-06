input_ = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

input_ = input_.split("\n")
s = 0
for line in input_:
    nums = []
    buffer = ""
    i = 0
    while i < len(line)-1:
        char = line[i]
        if char.isnumeric():
            nums.append(char)
        else:
            buffer += char
            number_exist = False
            for number in numbers:
                if number.startswith(buffer):
                    number_exist = True
                    break
            if not number_exist:
                buffer = ""
            if buffer in numbers:
                nums.append(str(numbers.index(buffer)+1))
                buffer = ""
        i += 1
    if len(nums) > 0:
        print(nums[0]," ",nums[len(nums)-1])
        s += int(nums[0]+nums[len(nums)-1])
print(s)