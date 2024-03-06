i = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''

i = i.split("\n")
s = 0
for line in i:
    nums = []
    for char in line:
        if char.isnumeric():
            nums.append(char)
    if len(nums) > 0:
        s += int(nums[0]+nums[len(nums)-1])
print(s)