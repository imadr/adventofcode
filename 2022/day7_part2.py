input_ = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''

current_path = []
dirs = {}

input_ = input_.split("\n")
for i in range(0, len(input_)):
    line = input_[i].split(" ")
    if line[1] == "cd":
        if line[2] == "/":
            current_path = ["/"]
        elif line[2] == "..":
            current_path.pop()
        else:
            current_path.append(line[2])
        current_path_s = "/".join(current_path)
        if current_path_s not in dirs:
            dirs[current_path_s] = 0
    elif line[1] == "ls":
        i += 1
        line = input_[i].split(" ")
        ls = []
        while line[0] != "$":
            ls.append(input_[i])
            i += 1
            if i == len(input_):
                break
            line = input_[i].split(" ")
        i -= 1
        current_path_s = "/".join(current_path)
        for thing in ls:
            thing = thing.split(" ")
            if thing[0] != "dir":
                dirs[current_path_s] += int(thing[0])
        if len(current_path) > 1:
            for i in range(1, len(current_path)):
                parent_path_s = "/".join(current_path[:len(current_path)-i])
                dirs[parent_path_s] += dirs[current_path_s]

unused = 70000000-dirs["/"]
sorted_dirs = sorted(list(dirs.items()), key=lambda x: x[1])
for dir_ in sorted_dirs:
    if unused+dir_[1] >= 30000000:
        print(dir_[1])
        break