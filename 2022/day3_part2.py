import re

stuff = [
"vJrwpWtwJgWrhcsFMMfFFhFp",
"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
"PmmdzqPrVvPwwTWBwg",
"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
"ttgJtRGJQctTZtZT",
"CrZsJsPPZsGzwwsLwLmpwMDw",
]
stuff_ = []
for i in range(0, len(stuff), 3):
    stuff_.append(stuff[i:i + 3])
stuff = stuff_

sum_ = 0
for s in stuff:
    s1 = set(s[0])
    s2 = set(s[1])
    s3 = set(s[2])
    i = list(s1.intersection(s2.intersection(s3)))[0]
    upper = i.upper() == i
    if upper:
        sum_ += ord(i.upper())-65+27
    else:
        sum_ += ord(i.upper())-65+1
print(sum_)