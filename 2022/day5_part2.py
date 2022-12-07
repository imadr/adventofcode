input_ = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''

input_ = input_.split("\n")

stacks = []
moves = []

for line in input_:
    if "[" not in line:
        break
    stacks.append(line)

for line in input_:
    if "move" not in line:
        continue
    moves.append(line)

stacks_ = [x.split("    ") for x in stacks]
for i, stack in enumerate(stacks_):
    tmp_stack = []
    for s in stack:
        tmp_stack += s.split(" ")
    stacks_[i] = tmp_stack

stacks = []
for s in stacks_:
    for i in s:
        stacks.append([])
    break
for stack in stacks_:
    for i, e in enumerate(stack):
        if e != "":
            stacks[i].append(e.replace("[", "").replace("]", ""))

moves_ = []
for i, move in enumerate(moves):
    s = moves[i].split(" ")
    moves_.append([int(s[1]), int(s[3]), int(s[5])])
moves = moves_

for move in moves:
    tmp_stack = []
    for number_moves in range(0, move[0]):
        tmp_stack.insert(0, stacks[move[1]-1].pop(0))
    for i, e in enumerate(tmp_stack):
        stacks[move[2]-1].insert(0, e)
s = ""
for s_ in stacks:
    s += s_[0]
print(s)
