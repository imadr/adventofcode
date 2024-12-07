s = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".split("\n")[1:]

s = [list(x) for x in s]

guard_direction_change = {
    "[-1, 0]": [0, 1],
    "[0, 1]": [1, 0],
    "[1, 0]": [0, -1],
    "[0, -1]": [-1, 0]
}
guard_char = {
    "[-1, 0]": "^",
    "[0, 1]": ">",
    "[1, 0]": "v",
    "[0, -1]": "<"
}
guard_direction = [-1, 0]
guard_position = [0, 0]
for row in range(len(s)):
    for column in range(len(s[row])):
        if s[row][column] == "^":
            guard_position = [row, column]

visited = []
visited.append(str(guard_position))
while 1:
    new_guard_position = [x + y for x, y in zip(guard_position, guard_direction)]
    if new_guard_position[0] < 0 or new_guard_position[1] < 0 or new_guard_position[0] >= len(s) or new_guard_position[1] >= len(s[0]):
        break
    new_cell = s[new_guard_position[0]][new_guard_position[1]]
    if new_cell == "#":
        guard_direction = guard_direction_change[str(guard_direction)]
    new_guard_position = [x + y for x, y in zip(guard_position, guard_direction)]
    new_cell = s[new_guard_position[0]][new_guard_position[1]]
    visited.append(str(new_guard_position))
    s[guard_position[0]][guard_position[1]] = "."
    s[new_guard_position[0]][new_guard_position[1]] = guard_char[str(guard_direction)]
    guard_position = new_guard_position
print(len(set(visited)))