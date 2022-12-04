import re

a = '''A Y
B X
C Z
'''


d = {
    "X": "A",
    "Y": "B",
    "Z": "C",
}
shit_score = {
    "A": 1,
    "B": 2,
    "C": 3,
}
outcome = {
    "A": ["C", "B", "A"],
    "B": ["A", "C", "B"],
    "C": ["B", "A", "C"],
}
outcome_score = [
    0, 6, 3
]
def whatdo(a, b):
    if b == "X": #lose
        return outcome[a][0]
    elif b == "Y": #draw
        return outcome[a][2]
    elif b == "Z": #win
        return outcome[a][1]

def score(a, b):
    return outcome_score[outcome[a].index(b)]

a = a.split("\n")
a = [x.split(" ") for x in a]
s = 0
for line in a:
    if len(line) < 2:
        continue
    s += shit_score[whatdo(line[0], line[1])] + score(line[0], whatdo(line[0], line[1]))
print(s)