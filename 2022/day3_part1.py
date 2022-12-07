import re

stuff = [
"vJrwpWtwJgWrhcsFMMfFFhFp",
"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
"PmmdzqPrVvPwwTWBwg",
"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
"ttgJtRGJQctTZtZT",
"CrZsJsPPZsGzwwsLwLmpwMDw",
]

sum_ = 0
for s in stuff:
    first_half = s[0:int(len(s)/2)]
    second_half = s[int(len(s)/2):]
    i = list(set(first_half).intersection(set(second_half)))[0]
    upper = i.upper() == i
    if upper:
        sum_ += ord(i.upper())-65+27
    else:
        sum_ += ord(i.upper())-65+1

print(sum_)